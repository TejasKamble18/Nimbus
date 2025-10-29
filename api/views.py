# api/views.py
from datetime import timedelta
import requests
from django.utils import timezone
from django.db.models.functions import TruncDate
from django.db.models import Count
from rest_framework import viewsets, permissions, serializers  # + serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Note
from .serializers import NoteSerializer

# NEW: drf-spectacular helpers
from drf_spectacular.utils import (
    extend_schema, OpenApiParameter, OpenApiTypes, inline_serializer
)

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.AllowAny]
    search_fields = ["title", "content"]
    filterset_fields = ["priority"]
    ordering_fields = ["created_at", "updated_at", "priority"]

@extend_schema(
    summary="GitHub user lookup",
    parameters=[
        OpenApiParameter(
            name="username",
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description="GitHub username (default: octocat)"
        ),
    ],
    responses={200: OpenApiTypes.OBJECT}  # keep generic; GitHub schema varies
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def github_user(request):
    username = request.GET.get("username", "octocat")
    try:
        r = requests.get(
            f"https://api.github.com/users/{username}",
            headers={"Accept": "application/vnd.github+json"},
            timeout=10,
        )
        return Response(r.json(), status=r.status_code)
    except requests.RequestException as e:
        return Response({"error": str(e)}, status=500)

@extend_schema(
    summary="Daily notes count",
    parameters=[
        OpenApiParameter(
            name="days",
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description="Number of days to include (default 14)",
            required=False
        ),
    ],
    responses={
        200: inline_serializer(
            name="DailyNotesResponse",
            fields={
                "date": serializers.DateField(),
                "count": serializers.IntegerField()
            },
            many=True,
        )
    }
)
@api_view(["GET"])
@permission_classes([permissions.AllowAny])
def daily_notes(request):
    days = int(request.GET.get("days", 14))
    start = (timezone.now() - timedelta(days=days - 1)).date()
    qs = (
        Note.objects.filter(created_at__date__gte=start)
        .annotate(day=TruncDate("created_at"))
        .values("day")
        .annotate(count=Count("id"))
        .order_by("day")
    )
    day_map = {row["day"].isoformat(): row["count"] for row in qs}
    result = [{"date": (start + timedelta(days=i)).isoformat(),
               "count": day_map.get((start + timedelta(days=i)).isoformat(), 0)}
              for i in range(days)]
    return Response(result)
