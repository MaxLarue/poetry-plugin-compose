import sys
from typing import List

from cleo.commands.command import Command
from cleo.io.inputs.argument import Argument

from poetry_plugin_compose.composed_commands.discover_packages import discover_packages
from poetry_plugin_compose.composed_commands.run_sub_command import run_sub_command


class ComposeCommand(Command):
    name = "compose"
    arguments = [Argument(name='sub command')]

    def __init__(self):
        super().__init__()
        self.usages = ['compose <sub-command>']
        self.description = 'Manage multiple packages from a single root'
        self._ignore_validation_errors = True

    def handle(self) -> int:
        self.compose(sys.argv[2:])
        return 0

    def compose(self, command: List[str]):
        packages = discover_packages('.')
        return_code = 0
        full_command = ['poetry', 'run', *command]
        for package in packages:
            self.line('\033[0;34m')
            self.line("[poetry run multi] running command " + " ".join(full_command) + " in " + package)
            self.line('')
            return_code += run_sub_command(full_command, package)
            self.line('')
            self.line("[poetry run multi] " + ('success' if return_code == 0 else 'failure'))
            self.line('\033[0m')
        return return_code


def compose_command_factory():
    return ComposeCommand()