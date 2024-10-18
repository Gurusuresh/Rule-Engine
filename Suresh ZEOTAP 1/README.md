# Rule Engine with AST

## Project Overview

The **Rule Engine with Abstract Syntax Tree (AST)** is designed to allow users to define and evaluate custom rules dynamically. The project uses Python’s AST module to safely parse and execute user-defined logic. This rule engine provides flexibility by allowing users to write rules in Python syntax and apply them to datasets or input variables.

## Features

- Create dynamic rules using Python expressions.
- Parse and evaluate rules using AST for safe execution.
- Support for conditional statements, mathematical operations, and logical comparisons.
- Lightweight and fast rule evaluation engine.
- Easily extendable for additional operations or functionalities.

## Project Structure

![image](https://github.com/user-attachments/assets/6fd7a255-01e6-4152-98d3-fc054286e772)



## Getting Started

### Prerequisites

Before starting, ensure you have:

- Python 3.10 or higher installed.

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Gurusuresh/Rule-Engine-with-AST.git
    cd Rule-Engine-with-AST
    ```

2. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Run the application**:

    The rule engine is designed to be imported into other projects or run as a standalone tool. You can try out the example rule evaluation by running:

    ```bash
    python rule_engine.py
    ```

## How It Works

1. The user defines a rule in Python-like syntax (e.g., `'x > 10 and y < 20'`).
2. The `rule_engine.py` script parses the rule into an AST for safe evaluation.
3. The engine then applies the rule to the input variables and returns the result (True/False or calculated values).
4. The configuration allows defining safe operators and functions that can be used within the rules.

### Example Usage

```python
from rule_engine import RuleEngine

# Define the rule
rule = "x > 10 and y < 20"

# Input data for the rule
data = {'x': 15, 'y': 18}

# Initialize the Rule Engine
engine = RuleEngine(rule)

# Evaluate the rule with the provided data
result = engine.evaluate(data)
print(result)  # Output: True
