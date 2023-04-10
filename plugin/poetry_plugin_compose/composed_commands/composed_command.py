from typing import List

from cleo.io.io import IO


class ComposedCommand:
    name: str
    io: IO

    def __init__(self, io: IO):
        self.io = io

    def match(self, args: List[str]):
        return args and args[0] == self.name

    def handle(self, args: List[str]):
        pass

    def _write_empty(self):
        self.io.write_line("")

    def _write_line(self, line: str):
        self.io.write_line("<info>[poetry compose] " + line + "</info>")
