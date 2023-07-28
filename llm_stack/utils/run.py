import subprocess
from llm_stack import llm_stack_DEBUG


def run_terminal_commands(command: str, stream_output: bool = llm_stack_DEBUG):
    process = subprocess.Popen(
        command,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        universal_newlines=True,
    )

    if stream_output:
        for line in process.stdout:
            print(line, end="")

    process.wait()  # Wait for the subprocess to complete
