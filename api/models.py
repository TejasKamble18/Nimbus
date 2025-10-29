from django.db import models
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    priority = models.IntegerField(default=3)  # 1=high,5=low
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        ordering = ["-created_at"]
    def __str__(self): return self.title
