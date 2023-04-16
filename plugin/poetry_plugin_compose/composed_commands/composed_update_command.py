from typing import IO
from shlex import join

from poetry_plugin_compose.composed_commands.composed_command import ComposedCommand
from poetry_plugin_compose.composed_commands.sub_command_runner import (
    run_sub_command_sync,
)


class ComposedUpdateCommand(ComposedCommand):
    name = "update"

    def __init__(self, io: IO):
        super().__init__(io, "Updates dependencies in every sub-packages")

    def run(self, args, package):
        self._write_line("Running update in " + " in " + package)
        return_code = run_sub_command_sync(["poetry", "update", *args], package)
        self._write_line("success" if return_code == 0 else "failure")
        return return_code
