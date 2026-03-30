import unittest
from app import app

class BasicTests(unittest.TestCase):
    # This setup function runs before each test
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    # This is our actual test!
    def test_main_page(self):
        # Simulate a user visiting the home page ('/')
        response = self.app.get('/')
        # Check if the website loaded successfully (HTTP 200)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()