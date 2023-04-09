import subprocess


def run_sub_command(command, root):
    completed = subprocess.call(command, cwd=root)
    return completed
