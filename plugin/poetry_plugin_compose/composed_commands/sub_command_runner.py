import subprocess
from typing import List


def run_sub_command_sync(command: List[str], root: str):
    completed = subprocess.call(" ".join(command), cwd=root, shell=True)
    return completed
