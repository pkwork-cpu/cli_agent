import os
def get_files_info(working_directory, directory=None):
    try:
        if directory not in os.listdir(working_directory) and directory != '.':
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        dirpath = os.path.join(working_directory, directory)
        if not os.path.isdir(dirpath):
            return f'Error: "{directory}" is not a directory'
        contents = os.listdir(dirpath)
        string_to_return = ''
        for item in contents:
            new_path = os.path.join(dirpath, item)
            string_to_return += f'- {item}: file_size:{os.path.getsize(new_path)}, is_dir={os.path.isdir(new_path)}\n'
        return string_to_return
    except Exception as e:
        return f'Error: {str(e)}'