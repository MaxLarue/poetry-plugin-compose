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
from poetry_plugin_compose.composed_commands.sub_package_contains import (
    sub_package_contains,
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
        self.parser.add_argument("-c", "--contains", action="store")

    def handle(self, args: List[str]):
        root_command, sub_command = split_root_command_and_sub_command(args)
        normal_args = sub_command[1:] if sub_command[0] == self.name else sub_command
        options = self.parser.parse_args(root_command)
        packages = discover_packages(".")
        return_code = 0
        full_command = ["poetry", "run", *normal_args]
        for package in packages:
            if self.__ignore_missing(package, options):
                self.output_skipping_missing_package(options, package)
                continue
            if self.__ignore_not_contains(package, options):
                self.output_skipping_missing_file(options, package)
                continue
            return_code += self.run_sub_command_in_package(full_command, package)
        return return_code

    def output_skipping_missing_package(self, options, package):
        self._write_line(
            "package "
            + package
            + " missing dependency "
            + options.ignore_missing
            + " skipping"
        )

    def output_skipping_missing_file(self, options, package):
        self._write_line(
            "package "
            + package
            + " does not contain file "
            + options.contains
            + " skipping"
        )

    def run_sub_command_in_package(self, full_command, package):
        self._write_empty()
        self._write_line("running command " + " ".join(full_command) + " in " + package)
        self._write_empty()
        return_code = run_sub_command_sync(full_command, package)
        self._write_empty()
        self._write_line("success" if return_code == 0 else "failure")
        self._write_empty()
        return return_code

    def __ignore_missing(self, package, options):
        return options.ignore_missing and not sub_package_has_dependency(
            package, options.ignore_missing
        )

    def __ignore_not_contains(self, package, options):
        return options.contains and not sub_package_contains(package, options.contains)
