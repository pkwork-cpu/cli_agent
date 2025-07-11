import os

def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    target_file = abs_working_dir
    if file_path:
        target_file = os.path.abspath(os.path.join(working_directory, file_path))
    else:
        return "Error: No file specified"
    if not target_file.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        MAX_CHARS = 10000
        file_content = []
        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS + 1)
            truncated = len(content) > MAX_CHARS
            file_content_string = content[:MAX_CHARS]
            file_content.append(file_content_string)
            if truncated:
                file_content.append(f'...File "{file_path}" truncated at 10000 characters')
        return "\n".join(file_content)
    except Exception as e:
        return f"Error reading file: {e}"