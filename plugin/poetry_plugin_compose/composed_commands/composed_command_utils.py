from typing import List


def split_root_command_and_sub_command(args: List[str]):
    if "--" in args:
        index = args.index("--")
        return args[:index], args[index + 1 :]
    return [], args
