
import os
from pprint import pprint

def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        absolute_working_dir = os.path.abspath(working_directory)
        full_file_path: str = os.path.normpath(os.path.join(absolute_working_dir, file_path))

        in_working_path: bool = os.path.commonpath([absolute_working_dir, full_file_path]) == absolute_working_dir
        is_existing_dir = os.path.exists(full_file_path) and os.path.isdir(full_file_path)

        if not in_working_path: raise Exception(f"Error: Cannot write to \"{file_path}\" as it is outside the permitted working directory")
        if is_existing_dir: raise Exception(f"Error: Cannot write to \"{file_path}\" as it is a directory")

        os.makedirs(os.path.dirname(full_file_path), exist_ok=True)

        with open(full_file_path, mode="w") as file:
            file.write(content)

        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    
    except Exception as e:
        return f'Error: an unexpected exception was raised, {e}'
