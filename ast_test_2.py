# Import ast
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
                    function_packages[function_name] = package_name
        elif isinstance(item, ast.ImportFrom):
            for alias in item.names:
                package_name = item.module
                # Update the package for each function
                for function_name in function_packages:
                    function_packages[function_name] = package_name


# Extract functions and their packages
extract_functions_with_packages(parsed_code)
extract_imports(parsed_code)

# Print functions and their corresponding packages
for function_name, package_name in function_packages.items():
    print(f"Function: {function_name}, Package: {package_name}")
