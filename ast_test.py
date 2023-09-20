# Simple ast tree test on single function program
# Returns imports and functions separately

import ast

# Sample Python code
code = """
import math

def square(x):
    return x * x

print(square(5))
"""

# Parse the code using ast
parsed_code = ast.parse(code)

# Function to extract functions from AST


def extract_functions(node):
    functions = []
    for item in node.body:
        if isinstance(item, ast.FunctionDef):
            functions.append(item.name)
    return functions


# Extract functions
functions = extract_functions(parsed_code)
print("Functions:", functions)

# Function to extract imports from AST
def extract_imports(node):
    imports = []
    for item in node.body:
        if isinstance(item, ast.Import):
            for alias in item.names:
                imports.append(alias.name)
        elif isinstance(item, ast.ImportFrom):
            for alias in item.names:
                imports.append(alias.name)
    return imports


# Extract imports
imports = extract_imports(parsed_code)
print("Imports:", imports)
