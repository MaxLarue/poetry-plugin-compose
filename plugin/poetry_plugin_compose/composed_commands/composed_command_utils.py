from typing import List


def split_root_command_and_sub_command(args: List[str]):
    if "--" in args:
        index = args.index("--")
        return args[1:index], args[index + 1 :]
    return args[:1], args[1:]
