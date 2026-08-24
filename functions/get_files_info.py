
import os
from pprint import pprint

def get_files_info(working_directory: str, directory:str = ".") -> str:
    try:
        abs_path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(abs_path, directory))

        valid_target = os.path.commonpath([target_dir, abs_path]) == abs_path

        if not valid_target: return f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory"
        if not os.path.isdir(directory): return f"Error: \"{directory}\" is not a directory."

        return f"Success: \"{directory}\" is within the working directory."
    except Exception as e:
        pprint(f"Error: {e}")