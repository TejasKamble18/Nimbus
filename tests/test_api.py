from rest_framework.test import APITestCase
class NotesAPITest(APITestCase):
    def test_crud_and_report(self):
        r=self.client.post('/api/notes/', {"title":"A","content":"B","priority":2}, format='json')
        self.assertEqual(r.status_code,201)
        nid=r.json()["id"]
        self.assertEqual(self.client.get('/api/notes/').status_code,200)
        self.assertEqual(self.client.patch(f'/api/notes/{nid}/', {"title":"A2"}, format='json').status_code,200)
        self.assertEqual(self.client.get('/api/report/daily-notes/?days=7').status_code,200)
        self.assertEqual(self.client.delete(f'/api/notes/{nid}/').status_code,204)
