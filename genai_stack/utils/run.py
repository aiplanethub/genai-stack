import os
import subprocess
from typing import List


def run_terminal_commands(command: str, stream_output: bool = False):
    try:
        result = subprocess.run(
            command,
            shell=True,  # Use shell to handle complex commands
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,  # Specify the encoding explicitly (Python 3.7+)
            check=True,  # Raise an exception if the subprocess returns non-zero exit code
        )

        if stream_output:
            print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error executing command: {e}")
        print(f"Command output:\n{e.output}")
    except Exception as e:
        print(f"An error occurred: {e}")


def execute_command_in_directory(target_directory, commands: List[str]):
    try:
        os.makedirs(target_directory, exist_ok=True)
        os.chdir(target_directory)
        print(f"Current working directory: {os.getcwd()}")

        # Run the provided commands here
        for cmd in commands:
            run_terminal_commands(cmd)

    except FileNotFoundError:
        print(f"Directory not found: {target_directory}")
    except Exception as e:
        print(f"An error occurred: {e}")
