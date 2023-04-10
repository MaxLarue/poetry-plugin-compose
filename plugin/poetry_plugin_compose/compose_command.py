import sys
from typing import List, Optional

from cleo.commands.command import Command
from cleo.io.inputs.argument import Argument

from poetry_plugin_compose.composed_commands.composed_command import ComposedCommand
from poetry_plugin_compose.composed_commands.composed_run_command import (
    ComposedRunCommand,
)


class ComposeCommand(Command):
    name = "compose"
    arguments = [Argument(name="sub command", is_list=True)]
    sub_command_classes = [ComposedRunCommand]
    sub_commands: List[ComposedCommand] = []
    default_sub_command_class = ComposedRunCommand
    default_sub_command: Optional[ComposedCommand] = None

    def __init__(self):
        super().__init__()
        self.usages = ["compose <sub-command>"]
        self.description = "Manage multiple packages from a single root"
        self._ignore_validation_errors = True

    def handle(self) -> int:
        self._build_sub_commands()
        args = sys.argv[2:]
        for command in self.sub_commands:
            if command.match(args):
                return command.handle(args)

        return self.default_sub_command.handle(args)

    def _build_sub_commands(self):
        self.sub_commands = [command(self.io) for command in self.sub_command_classes]
        self.default_sub_command = self.default_sub_command_class(self.io)


def compose_command_factory():
    return ComposeCommand()
