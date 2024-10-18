import unittest
from app import app

class TestEvaluateRule(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_evaluate_rule(self):
        ast_tree = {
            "type": "operator",
            "left": {
                "type": "operand",
                "value": "age"
            },
            "right": {
                "type": "operand",
                "value": 30
            },
            "value": ">"
        }
        response = self.app.post('/evaluate_rule', json={
            "ast": ast_tree,
            "attributes": {"age": 35}
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.json['result'])

if __name__ == '__main__':
    unittest.main()
