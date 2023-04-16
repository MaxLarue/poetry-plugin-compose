from cleo.io.io import IO

from poetry_plugin_compose.composed_commands.composed_command import ComposedCommand
from poetry_plugin_compose.composed_commands.sub_command_runner import (
    run_sub_command_sync,
)


class ComposedInstallCommand(ComposedCommand):
    name = "install"

    def __init__(self, io: IO):
        super().__init__(io, "RUn install in multiple sub-packages")

    def run(self, args, package):
        self._write_line("installing dependencies in " + " in " + package)
        return_code = run_sub_command_sync(["poetry", "install", *args], package)
        self._write_line("success" if return_code == 0 else "failure")
        return return_code
