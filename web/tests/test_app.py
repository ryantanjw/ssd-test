
import unittest
from app import app

class WebAppTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_home_page_loads(self):
        res = self.client.get('/')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'Login', res.data)

if __name__ == "__main__":
    unittest.main()
