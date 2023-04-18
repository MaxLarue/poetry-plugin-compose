from typing import List

from cleo.io.io import IO

from poetry_plugin_compose.composed_commands.composed_command import ComposedCommand
from poetry_plugin_compose.packages.build_dependency_graph import build_dependency_graph


class DependencyOrderCommand(ComposedCommand):
    name = "dependency-order"

    def __init__(self, io: IO):
        super(DependencyOrderCommand, self).__init__(
            io, "Find dependency order between packages"
        )

    def handle(self, args: List[str]):
        order, _ = build_dependency_graph()
        self._write_line(", ".join(order))

    def run(self, args, package):
        pass
