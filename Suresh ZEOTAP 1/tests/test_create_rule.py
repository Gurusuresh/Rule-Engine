import unittest
from app import app

class TestCreateRule(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_create_rule(self):
        response = self.app.post('/create_rule', json={
            "rule": "age > 30 AND salary > 50000"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('ast', response.json)

if __name__ == '__main__':
    unittest.main()
