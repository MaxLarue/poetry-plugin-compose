from typing import IO
from shlex import join

from poetry_plugin_compose.composed_commands.composed_command import ComposedCommand
from poetry_plugin_compose.composed_commands.sub_command_runner import (
    run_sub_command_sync,
)


class ComposedRemoveCommand(ComposedCommand):
    name = "remove"

    def __init__(self, io: IO):
        super().__init__(io, "Removes a dependency to every sub-packages")

    def run(self, args, package):
        self._write_line("Running remove " + join(args) + " in " + " in " + package)
        return_code = run_sub_command_sync(["poetry", "remove", *args], package)
        self._write_line("success" if return_code == 0 else "failure")
        return return_code
