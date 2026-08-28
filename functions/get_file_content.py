
import os
import config

def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        full_file_path = os.path.join(working_directory, file_path)
        in_working_path = os.path.exists(full_file_path)
        if not in_working_path: return f"Error: Cannot read \"{file_path}\" as it is outside the permitted working directory"
        if not os.path.isfile(full_file_path): return f"Error: File not found or is not a regular file: \"{file_path}\""

        file = open(full_file_path)
        file_contents = file.read(config.READ_FILE_CHAR_LIMIT)

        if file.read(1):
            file_contents += f"[...File \"{file_path}\" truncated at {config.READ_FILE_CHAR_LIMIT} characters]"

        return file_contents

    except Exception as e:
        print(f"Error: Function get_file_content() encountered an error, {e}")