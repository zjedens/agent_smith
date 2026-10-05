
import os
import subprocess
from pprint import pprint

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run a python script (.py).  Assume the file exists.  Allows to pass in cmd args to script",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The python file (.py) to run as a script"
                },
                "args": {
                    "type": "array",
                    "description": "A list of (string) arguments to be passed to the executing Python script (i.e. file_path.py)"
                }
            },
            "required": ["file_path", "args"]
        }
    }
}

def run_python_file(working_directory: str, file_path: str, args: list[str] | None = None) -> str:
    try:
        absolute_working_dir = os.path.abspath(working_directory)
        full_file_path: str = os.path.normpath(os.path.join(absolute_working_dir, file_path))

        in_working_path: bool = os.path.commonpath([absolute_working_dir, full_file_path]) == absolute_working_dir
        is_file = os.path.isfile(full_file_path)
        has_py_ext = full_file_path.endswith('.py')

        if not in_working_path: raise Exception(f"Error: Cannot execute \"{file_path}\" as it is outside the permitted working directory")
        if not is_file: raise Exception(f'Error: "{file_path}" does not exist or is not a regular file')
        if not has_py_ext: raise Exception(f'Error: "{file_path}" is not a Python file')

        command = ['python', full_file_path]
        if args is not None and len(args) > 0:
            command.extend(args)

        proc_complete = subprocess.run(
            command,
            cwd=working_directory,
            capture_output=True,
            text=True,
            timeout=30
        )

        output = []

        if proc_complete.returncode != 0:
            output.append(f'Process exited with code {proc_complete.returncode}')
        if len(proc_complete.stdout) == 0 and len(proc_complete.stderr) == 0:
            output.append("No output produced")
        if len(proc_complete.stdout) > 0:
            output.append(f'STDOUT: {proc_complete.stdout}')
        if len(proc_complete.stderr) > 0:
            output.append(f'STDERR: {proc_complete.stderr}')

        return "\n".join(output)
    except Exception as e:
        return f'Error: executing Python file: {e}'