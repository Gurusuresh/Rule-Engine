def evaluate_ast(node, data):
    if node['type'] == 'operator':
        left = evaluate_ast(node['left'], data)
        right = evaluate_ast(node['right'], data)
        if node['value'] == 'AND':
            return left and right
        elif node['value'] == 'OR':
            return left or right
        else:
            return evaluate_comparison(left, right, node['value'])

    elif node['type'] == 'operand':
        return data.get(node['value'], None)

    return False

def evaluate_comparison(left, right, operator):
    if operator == '>':
        return left > right
    elif operator == '<':
        return left < right
    elif operator == '=':
        return left == right
    elif operator == '>=':
        return left >= right
    elif operator == '<=':
        return left <= right
    else:
        return False
