import argparse
from typing import List

from cleo.io.io import IO

from poetry_plugin_compose.composed_commands.composed_command_utils import (
    split_compose_command_and_sub_command,
)
from poetry_plugin_compose.packages.discover_packages import discover_packages
from poetry_plugin_compose.composed_commands.package_filter import (
    PackageContainsFileFilter,
    PackageHasDependencyFilter,
)


class ComposedCommand:
    name: str
    io: IO
    parser: argparse.ArgumentParser
    description: str

    def __init__(self, io: IO, description: str):
        self.io = io
        self.description = description
        self.parser = argparse.ArgumentParser(
            prog="poetry compose " + self.name, description=description
        )
        self.parser.add_argument(
            "-i",
            "--ignore-missing",
            action="store",
            help="Only run in packages that have this dependency",
        )
        self.parser.add_argument(
            "-c",
            "--contains",
            action="store",
            help="Only run in packages that include this file",
        )

    def match(self, args: List[str]):
        return args and args[0] == self.name

    def print_help(self):
        self.parser.print_help()

    def split_args(self, args: List[str]):
        return split_compose_command_and_sub_command(args)

    def handle(self, args: List[str]):
        root_command, sub_command = self.split_args(args)
        options = self.parser.parse_args(root_command[1:])
        filters = self._get_package_filters(options)
        packages = discover_packages(".")
        return_code = 0
        for package in packages:
            if self.filter_package(package, filters):
                return_code += self.run(sub_command, package)
        return return_code

    def run(self, args, package):
        raise NotImplementedError()

    def filter_package(self, package, filters):
        for filter in filters:
            can_run, msg = filter.filter(package)
            if not can_run:
                self._write_line(msg + " skipping")
                return False
        return True

    def _write_empty(self):
        self.io.write_line("")

    def _write_line(self, line: str):
        self.io.write_line("<info>[poetry compose] " + line + "</info>")

    def _get_package_filters(self, options):
        filters = []
        if options.contains:
            filters.append(PackageContainsFileFilter(options.contains))
        if options.ignore_missing:
            filters.append(PackageHasDependencyFilter(options.ignore_missing))
        return filters
