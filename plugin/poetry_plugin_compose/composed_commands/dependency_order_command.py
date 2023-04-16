from typing import List

from cleo.io.io import IO

from poetry_plugin_compose.composed_commands.composed_command import ComposedCommand
from poetry_plugin_compose.packages.discover_packages import discover_packages
from poetry_plugin_compose.packages.get_package_dependencies import get_package_dependencies
from poetry_plugin_compose.packages.get_package_name import get_package_descriptor


class DependencyOrderCommand(ComposedCommand):
    name = "dependency-order"

    def __init__(self, io: IO):
        super(DependencyOrderCommand, self).__init__(io, "Find dependency order between packages")

    def handle(self, args: List[str]):
        packages = discover_packages(".")
        for package in packages:
            package_name = get_package_descriptor(package)
            dependencies = get_package_dependencies(package)
            print(package_name, dependencies)

    def run(self, args, package):
        pass
