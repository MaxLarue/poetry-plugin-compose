import sys
from typing import List, Optional

from cleo.commands.command import Command
from cleo.io.inputs.argument import Argument
from cleo.io.io import IO

from poetry_plugin_compose.composed_commands.composed_add_command import (
    ComposedAddCommand,
)
from poetry_plugin_compose.composed_commands.composed_build_command import (
    ComposedBuildCommand,
)
from poetry_plugin_compose.composed_commands.composed_check_command import (
    ComposedCheckCommand,
)
from poetry_plugin_compose.composed_commands.composed_command import ComposedCommand
from poetry_plugin_compose.composed_commands.composed_install_command import (
    ComposedInstallCommand,
)
from poetry_plugin_compose.composed_commands.composed_lock_command import (
    ComposedLockCommand,
)
from poetry_plugin_compose.composed_commands.composed_publish_command import (
    ComposedPublishCommand,
)
from poetry_plugin_compose.composed_commands.composed_remove_command import (
    ComposedRemoveCommand,
)
from poetry_plugin_compose.composed_commands.composed_run_command import (
    ComposedRunCommand,
)
from poetry_plugin_compose.composed_commands.composed_update_command import (
    ComposedUpdateCommand,
)


class ComposeCommand(Command):
    name = "compose"
    arguments = [Argument(name="sub command", is_list=True)]
    sub_command_classes = [
        ComposedInstallCommand,
        ComposedAddCommand,
        ComposedBuildCommand,
        ComposedCheckCommand,
        ComposedLockCommand,
        ComposedPublishCommand,
        ComposedRemoveCommand,
        ComposedUpdateCommand,
        ComposedRunCommand,
    ]
    sub_commands: List[ComposedCommand] = []
    _io: IO

    def __init__(self):
        super().__init__()
        self.usages = ["compose <sub-command>"]
        self.description = "Manage multiple packages from a single root"
        self._ignore_validation_errors = True

    def handle(self) -> int:
        self._build_sub_commands()
        subcommand_args = sys.argv[2:]
        for command in self.sub_commands:
            if command.match(subcommand_args):
                if len(subcommand_args) > 1 and subcommand_args[1] in ["--help", "-h"]:
                    command.print_help()
                    return 0
                else:
                    return command.handle(subcommand_args)
        self.__print_help(subcommand_args)
        return 1

    def _build_sub_commands(self):
        self.sub_commands = [command(self._io) for command in self.sub_command_classes]

    def set_io(self, io: IO):
        self._io = io

    def __print_help(self, subcommand_args):
        command_name = subcommand_args[0] if subcommand_args else ""
        self._io.write_line(
            "<error>" + "could not find command '" + command_name + "'</error>"
        )
        self._io.write_line("Available commands:")
        for command in self.sub_commands:
            self._io.write_line(
                "    <comment>" + command.name + "</comment>: " + command.description
            )


def compose_command_factory():
    return ComposeCommand()
