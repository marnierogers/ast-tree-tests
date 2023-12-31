import ast

# Sample Python code
code = """
import math
from datetime import datetime

def square(x):
    return x * x

def cube(x):
    return x * x * x

print(square(5))
print(cube(3))
"""

# Parse the code using ast
parsed_code = ast.parse(code)

# Initialize a dictionary to store functions and their corresponding packages
function_packages = {}

# Function to extract functions and their packages from AST


def extract_functions_with_packages(node):
    for item in node.body:
        if isinstance(item, ast.FunctionDef):
            function_name = item.name
            # Store the function and its corresponding package
            function_packages[function_name] = None

# Function to extract imports and update the corresponding package for each function
def extract_imports(node):
    for item in node.body:
        if isinstance(item, ast.Import):
            for alias in item.names:
                package_name = alias.name
                # Update the package for each function
                for function_name in function_packages:
                    if f"{function_name}(" in code:
                        function_packages[function_name] = package_name
        elif isinstance(item, ast.ImportFrom):
            package_name = item.module
            for alias in item.names:
                # Update the package for each function
                for function_name in function_packages:
                    if f"{function_name}(" in code:
                        function_packages[function_name] = package_name


# Extract functions and their packages
extract_functions_with_packages(parsed_code)
extract_imports(parsed_code)

# Print functions and their corresponding packages
print("Functions and their corresponding packages:")
for function_name, package_name in function_packages.items():
    print(f"Function: {function_name}, Package: {package_name}")
