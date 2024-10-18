import requests

# Test create_rule endpoint
url_create_rule = "http://127.0.0.1:5000/create_rule"
rule_data = {
    "rule": "age > 30 AND salary > 50000"
}
response = requests.post(url_create_rule, json=rule_data)
print("Create Rule Response:", response.json())

# Test evaluate_rule endpoint
url_evaluate_rule = "http://127.0.0.1:5000/evaluate_rule"
ast_data = {
    "ast": {
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
    },
    "attributes": {
        "age": 35
    }
}
response = requests.post(url_evaluate_rule, json=ast_data)
print("Evaluate Rule Response:", response.json())
