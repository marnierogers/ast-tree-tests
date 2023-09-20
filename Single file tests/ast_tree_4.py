# Simple ast tree test on program containing 2 functions + libraries
# Returns imports and some related functions
# Datetime doesn't work - don't know why?
# Pandas and pd not related

import ast

# Read the contents from the file
file_path = "test_code.py"
with open(file_path, "r") as file:
    code = file.read()

# Parse the code using ast
parsed_code = ast.parse(code)

# Initialize a dictionary to store imported modules and used functions
info_dict = {}

# Function to extract import names and used functions from the AST
def extract_info_from_ast(node):
    for item in node.body:
        if isinstance(item, ast.Import):
            for alias in item.names:
                module_name = alias.name
                info_dict[module_name] = []

        elif isinstance(item, ast.ImportFrom):
            module_name = item.module
            for alias in item.names:
                full_function_name = f"{module_name}.{alias.name}"
                info_dict[module_name] = info_dict.get(module_name, [])
                info_dict[module_name].append(full_function_name)

        elif isinstance(item, ast.Expr) and isinstance(item.value, ast.Call):
            if isinstance(item.value.func, ast.Attribute):
                module_name = item.value.func.value.id
                function_name = item.value.func.attr
                full_function_name = f"{module_name}.{function_name}"
                info_dict[module_name] = info_dict.get(module_name, [])
                info_dict[module_name].append(full_function_name)


# Extract import names and used functions from the AST
extract_info_from_ast(parsed_code)

# Print the extracted information
print("\nImported modules and used functions:")
for module, functions in info_dict.items():
    print(f"{module}: {', '.join(functions)}")
