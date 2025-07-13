import os

def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = abs_working_dir
    if file_path:
        abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    else:
        return "Error: No file path specified"
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        directory = os.path.dirname(abs_file_path)
        os.makedirs(directory, exist_ok=True)
        with open(abs_file_path, 'w') as file:
            file.write(content)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing file: {e}"