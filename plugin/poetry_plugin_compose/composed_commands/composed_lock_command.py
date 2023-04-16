from typing import IO

from poetry_plugin_compose.composed_commands.composed_command import ComposedCommand
from poetry_plugin_compose.composed_commands.sub_command_runner import (
    run_sub_command_sync,
)


class ComposedLockCommand(ComposedCommand):
    name = "lock"

    def __init__(self, io: IO):
        super().__init__(io, "Lock sub packages")

    def run(self, args, package):
        self._write_line("building " + package)
        return_code = run_sub_command_sync(["poetry", "lock", *args], package)
        self._write_line("success" if return_code == 0 else "failure")
        return return_code
