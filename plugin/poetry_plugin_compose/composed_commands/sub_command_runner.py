import subprocess
from typing import List


def run_sub_command_sync(command: List[str], root: str):
    completed = subprocess.call(" ".join(command), cwd=root, shell=True)
    return completed


def run_sub_command_sync_silent(command: List[str], root: str):
    completed = subprocess.call(
        " ".join(command),
        cwd=root,
        shell=True,
        stderr=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
    )
    return completed
