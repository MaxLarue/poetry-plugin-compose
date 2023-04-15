from cleo.io.io import IO

from poetry_plugin_compose.composed_commands.composed_command import ComposedCommand
from poetry_plugin_compose.composed_commands.sub_command_runner import (
    run_sub_command_sync,
)


class ComposedRunCommand(ComposedCommand):
    name = "run"

    def __init__(self, io: IO):
        super().__init__(io, "Run multiple commands in parallel")

    def run(self, full_command, package):
        self._write_line("running command " + " ".join(full_command) + " in " + package)
        return_code = run_sub_command_sync(full_command, package)
        self._write_line("success" if return_code == 0 else "failure")
        return return_code
