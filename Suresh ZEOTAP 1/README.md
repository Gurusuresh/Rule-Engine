# Rule Engine with AST

## Overview
This project implements a simple rule engine that evaluates user eligibility based on dynamically created rules using an Abstract Syntax Tree (AST). The rules can be defined, combined, and evaluated against user attributes like age, department, income, etc.

## Project Structure
- **app.py**: The Flask API with endpoints for creating and evaluating rules.
- **rule_engine.py**: Contains the core logic for rule creation, rule combination, and rule evaluation using AST.
- **tests.py**: Unit tests to ensure the rule engine works correctly.
- **database.sql**: SQL schema for storing rules and user data.
- **requirements.txt**: Python dependencies for the project.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/rule_engine_ast.git
   cd rule_engine_ast
