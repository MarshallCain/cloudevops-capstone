import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        # Send a GET request to the index page
        response = self.app.get('/')
        
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)
        
        # Check if the response contains expected content
        self.assertIn(b"Kushal's Travel Blog", response.data)

    def test_nonexistent_page(self):
        # Send a GET request to a nonexistent page (e.g., /nonexistent)
        response = self.app.get('/nonexistent')
        
        # Check if the response status code is 404 Not Found
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()