import argparse
from typing import List

from cleo.io.io import IO

from poetry_plugin_compose.composed_commands.composed_command import ComposedCommand
from poetry_plugin_compose.composed_commands.composed_command_utils import (
    split_root_command_and_sub_command,
)
from poetry_plugin_compose.composed_commands.discover_packages import discover_packages
from poetry_plugin_compose.composed_commands.sub_command_runner import (
    run_sub_command_sync,
)
from poetry_plugin_compose.composed_commands.sub_package_has_dependency import (
    sub_package_has_dependency,
)


class ComposedRunCommand(ComposedCommand):
    name = "run"
    parser: argparse.ArgumentParser

    def __init__(self, io: IO):
        super().__init__(io)
        self.parser = argparse.ArgumentParser(
            description="Run multiple commands in parallel"
        )
        self.parser.add_argument("-i", "--ignore-missing", action="store")

    def handle(self, args: List[str]):
        root_command, sub_command = split_root_command_and_sub_command(args)
        normal_args = sub_command[1:] if sub_command[0] == self.name else sub_command
        options = self.parser.parse_args(root_command)
        packages = discover_packages(".")
        return_code = 0
        full_command = ["poetry", "run", *normal_args]
        for package in packages:
            if options.ignore_missing:
                if not sub_package_has_dependency(package, options.ignore_missing):
                    self._write_line(
                        "package "
                        + package
                        + " missing dependency "
                        + options.ignore_missing
                        + " skipping"
                    )
                    continue
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
