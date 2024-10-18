import ast

class ASTNode:
    def __init__(self, type, left=None, right=None, value=None):
        self.type = type  # "operator" or "operand"
        self.left = left  # left child for binary operators
        self.right = right  # right child for binary operators
        self.value = value  # value for operand nodes (like age, salary, etc.)

    def to_dict(self):
        return {
            "type": self.type,
            "left": self.left.to_dict() if self.left else None,
            "right": self.right.to_dict() if self.right else None,
            "value": self.value
        }

def create_ast(rule_string):
    try:
        tree = ast.parse(rule_string, mode='eval')
        return convert_ast(tree.body).to_dict()
    except Exception as e:
        raise ValueError(f"Failed to parse rule: {str(e)}")

def convert_ast(node):
    if isinstance(node, ast.BoolOp):
        operator_type = "AND" if isinstance(node.op, ast.And) else "OR"
        left = convert_ast(node.values[0])
        right = convert_ast(node.values[1])
        return ASTNode("operator", left, right, operator_type)

    elif isinstance(node, ast.Compare):
        left = convert_ast(node.left)
        right = convert_ast(node.comparators[0])
        operator_type = get_operator(node.ops[0])
        return ASTNode("operator", left, right, operator_type)

    elif isinstance(node, ast.Constant):
        return ASTNode("operand", value=node.value)

    elif isinstance(node, ast.Name):
        return ASTNode("operand", value=node.id)

    else:
        raise ValueError(f"Unsupported node type: {type(node)}")

def get_operator(op):
    if isinstance(op, ast.Gt):
        return ">"
    elif isinstance(op, ast.Lt):
        return "<"
    elif isinstance(op, ast.Eq):
        return "="
    elif isinstance(op, ast.GtE):
        return ">="
    elif isinstance(op, ast.LtE):
        return "<="
    else:
        raise ValueError(f"Unsupported operator: {type(op)}")
