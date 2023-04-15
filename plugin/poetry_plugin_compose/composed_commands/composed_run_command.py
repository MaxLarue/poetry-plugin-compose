import argparse
from typing import List

from cleo.io.io import IO

from poetry_plugin_compose.composed_commands.composed_command import ComposedCommand
from poetry_plugin_compose.composed_commands.composed_command_utils import (
    split_root_command_and_sub_command,
)
from poetry_plugin_compose.composed_commands.discover_packages import discover_packages
from poetry_plugin_compose.composed_commands.package_filter import (
    PackageContainsFileFilter,
    PackageHasDependencyFilter,
)
from poetry_plugin_compose.composed_commands.sub_command_runner import (
    run_sub_command_sync,
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
        filters = self.__get_package_filters(options)
        packages = discover_packages(".")
        return_code = 0
        full_command = ["poetry", "run", *normal_args]
        for package in packages:
            if self.filter_pacakge(package, filters):
                return_code += self.run_sub_command_in_package(full_command, package)
        return return_code

    def filter_pacakge(self, package, filters):
        for filter in filters:
            can_run, msg = filter.filter(package)
            if not can_run:
                self._write_line(msg + " skipping")
                return False
        return True

    def run_sub_command_in_package(self, full_command, package):
        self._write_line("running command " + " ".join(full_command) + " in " + package)
        return_code = run_sub_command_sync(full_command, package)
        self._write_line("success" if return_code == 0 else "failure")
        return return_code

    def __get_package_filters(self, options):
        filters = []
        if options.contains:
            filters.append(PackageContainsFileFilter(options.contains))
        if options.ignore_missing:
            filters.append(PackageHasDependencyFilter(options.ignore_missing))
        return filters
