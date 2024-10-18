from flask import Flask, request, jsonify
import ast

app = Flask(__name__)

# Define a Node class for AST representation
class Node:
    def __init__(self, type, value=None, left=None, right=None):
        self.type = type  # 'operator' or 'operand'
        self.value = value
        self.left = left
        self.right = right

    def to_dict(self):
        return {
            'type': self.type,
            'value': self.value,
            'left': self.left.to_dict() if self.left else None,
            'right': self.right.to_dict() if self.right else None
        }

    @staticmethod
    def from_dict(data):
        if not data:
            return None
        node = Node(data['type'], data.get('value'))
        node.left = Node.from_dict(data.get('left'))
        node.right = Node.from_dict(data.get('right'))
        return node

# Function to parse rule string to AST
def create_ast(rule_string):
    try:
        expr = ast.parse(rule_string, mode='eval').body
        return parse_expr(expr)
    except Exception as e:
        raise ValueError(f"Error parsing rule: {str(e)}")

def parse_expr(expr):
    if isinstance(expr, ast.BoolOp):
        op = 'AND' if isinstance(expr.op, ast.And) else 'OR'
        left = parse_expr(expr.values[0])
        right = parse_expr(expr.values[1])
        return Node('operator', op, left, right)
    elif isinstance(expr, ast.Compare):
        left = expr.left.id if isinstance(expr.left, ast.Name) else parse_expr(expr.left)
        op = expr.ops[0]
        if isinstance(op, ast.Gt):
            op_str = '>'
        elif isinstance(op, ast.Lt):
            op_str = '<'
        elif isinstance(op, ast.Eq):
            op_str = '=='
        elif isinstance(op, ast.GtE):
            op_str = '>='
        elif isinstance(op, ast.LtE):
            op_str = '<='
        else:
            raise ValueError(f"Unsupported operator: {type(op)}")
        comparator = expr.comparators[0]
        if isinstance(comparator, ast.Constant):
            right = comparator.value
        elif isinstance(comparator, ast.Num):  # For older Python versions
            right = comparator.n
        elif isinstance(comparator, ast.Str):  # For older Python versions
            right = comparator.s
        else:
            raise ValueError(f"Unsupported comparator type: {type(comparator)}")
        return Node('operand', f"{left} {op_str} {right}")
    else:
        raise ValueError(f"Unsupported expression type: {type(expr)}")

# Function to evaluate AST against data
def evaluate_ast(node, data):
    if node.type == 'operator':
        left_val = evaluate_ast(node.left, data)
        right_val = evaluate_ast(node.right, data)
        if node.value == 'AND':
            return left_val and right_val
        elif node.value == 'OR':
            return left_val or right_val
        else:
            raise ValueError(f"Unsupported logical operator: {node.value}")
    elif node.type == 'operand':
        parts = node.value.split()
        if len(parts) != 3:
            raise ValueError(f"Invalid operand format: {node.value}")
        key, operator, value = parts
        if key not in data:
            return False  # If the attribute is missing, return False
        try:
            # Attempt to convert to float for numeric comparison
            value = float(value)
            user_val = float(data[key])
        except ValueError:
            # If conversion fails, treat as string comparison
            value = str(value)
            user_val = str(data[key])
        if operator == '>':
            return user_val > value
        elif operator == '<':
            return user_val < value
        elif operator == '==':
            return user_val == value
        elif operator == '>=':
            return user_val >= value
        elif operator == '<=':
            return user_val <= value
        else:
            raise ValueError(f"Unsupported comparison operator: {operator}")
    else:
        raise ValueError(f"Unsupported node type: {node.type}")

# Home route
@app.route('/', methods=['GET'])
def home():
    return jsonify(message="Welcome to the Rule Engine API!"), 200

# Endpoint to create a rule and return its AST
@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    data = request.get_json()
    rule = data.get('rule')
    if not rule:
        return jsonify({'error': 'Rule is required'}), 400
    try:
        ast_tree = create_ast(rule)
        return jsonify({'ast': ast_tree.to_dict()}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

# Endpoint to evaluate a rule against data
@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    data = request.get_json()
    ast_data = data.get('ast')
    attributes = data.get('attributes')
    if not ast_data or not attributes:
        return jsonify({'error': 'AST or data missing'}), 400
    try:
        ast_tree = Node.from_dict(ast_data)
        result = evaluate_ast(ast_tree, attributes)
        return jsonify({'eligible': result}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
