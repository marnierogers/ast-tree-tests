import ast
import os

# Function to extract import names and used functions from the AST for a given file
def extract_info_from_file(file_path):
    with open(file_path, "r") as file:
        code = file.read()
    parsed_code = ast.parse(code)
    info_dict = {}

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


    extract_info_from_ast(parsed_code)
    return info_dict


# Directory containing your codebase
codebase_directory = "Multi file tests\codebase"

# Initialize a dictionary to store imported modules and used functions across the codebase
codebase_info_dict = {}

# Iterate over the files in the codebase directory
for root, dirs, files in os.walk(codebase_directory):

    for file in files:
        if file.endswith(".py"):
            print("file" + file)
            file_path = os.path.join(root, file)
            file_info = extract_info_from_file(file_path)

            # Merge the information extracted from the current file into the codebase_info_dict
            for module, functions in file_info.items():
                codebase_info_dict[module] = codebase_info_dict.get(module, [])
                codebase_info_dict[module].extend(functions)

# Print the extracted information for the entire codebase
print("\nImported modules and used functions across the codebase:")
for module, functions in codebase_info_dict.items():
    print(f"{module}: {', '.join(functions)}")
