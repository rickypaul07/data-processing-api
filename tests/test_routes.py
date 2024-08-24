import unittest
from app import create_app

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = create_app()
        cls.client = cls.app.test_client()

    def test_upload(self):
        # Example test for the /upload endpoint
        response = self.client.post('/upload', data={'file': (open('test_file.csv', 'rb'), 'test_file.csv')})
        self.assertEqual(response.status_code, 200)
        self.assertIn('message', response.json)
        self.assertIn('file_id', response.json)

if __name__ == '__main__':
    unittest.main()
