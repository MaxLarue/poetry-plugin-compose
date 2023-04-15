from typing import List

from cleo.io.io import IO

from poetry_plugin_compose.composed_commands.composed_command import ComposedCommand
from poetry_plugin_compose.composed_commands.composed_command_utils import split_root_command_and_sub_command
from poetry_plugin_compose.composed_commands.sub_command_runner import (
    run_sub_command_sync,
)


class ComposedInstallCommand(ComposedCommand):
    name = "install"

    def __init__(self, io: IO):
        super().__init__(io, "RUn install in multiple sub-packages")

    def split_args(self, args: List[str]):
        if "--" in args:
            return split_root_command_and_sub_command(args)
        return args, []

    def run(self, args, package):
        import pdb; pdb.set_trace()
        self._write_line("installing dependencies in " + " in " + package)
        return_code = run_sub_command_sync(["poetry", "install", *args[1:]], package)
        self._write_line("success" if return_code == 0 else "failure")
        return return_code
