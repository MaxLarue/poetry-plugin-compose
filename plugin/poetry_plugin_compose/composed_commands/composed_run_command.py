from typing import List

from poetry_plugin_compose.composed_commands.composed_command import ComposedCommand
from poetry_plugin_compose.composed_commands.discover_packages import discover_packages
from poetry_plugin_compose.composed_commands.sub_command_runner import (
    run_sub_command_sync,
)


class ComposedRunCommand(ComposedCommand):
    name = "run"

    def handle(self, args: List[str]):
        normal_args = args[1:] if args[0] == self.name else args
        packages = discover_packages(".")
        return_code = 0
        full_command = ["poetry", "run", *normal_args]
        for package in packages:
            self._write_empty()
            self._write_line(
                "running command " + " ".join(full_command) + " in " + package
            )
            self._write_empty()
            return_code += run_sub_command_sync(full_command, package)
            self._write_empty()
            self._write_line("success" if return_code == 0 else "failure")
            self._write_empty()
        return return_code
