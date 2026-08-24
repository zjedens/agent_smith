
import os
from pprint import pprint

def get_files_info(working_directory: str, directory: str = ".") -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, directory))

        valid_target = os.path.commonpath([target_dir, abs_path]) == abs_path
        is_target_dir = os.path.isdir(target_dir)

        if not valid_target: return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
        if not is_target_dir: return f"Error: \"{directory}\" is not a directory."

        contents: list[str] = []
        print(f"Printing contents of {target_dir}")
        for item in os.listdir(target_dir):
            full_path = os.path.join(target_dir, item)
            contents.append(f"{item}: file_size={os.path.getsize(full_path)}, is_dir={os.path.isdir(full_path)}")

        return "\n".join(contents)
    except Exception as e:
        pprint(f"Error: {e}")