import traceback
import shutil
import os
from mako.template import Template


def generate_commands():
    from poetry_plugin_compose.composed_command_list import (
        ALL_COMPOSED_COMMAND_CLASSES,
    )
    command_metas = []
    for command_cls in ALL_COMPOSED_COMMAND_CLASSES:
        command_meta = {}
        command = command_cls()
        command_meta["name"] = command.name
        command_meta["description"] = command.description
        parser = command.get_parser()
        command_meta["help"] = parser.format_help()
        command_meta["usage"] = parser.format_usage()
        command_metas.append(command_meta)
        command_meta["examples"] = command.examples
    command_file_content = Template(
        """# Commands
% for command in command_metas:
${'##'} ${command["name"]}
> ${command["description"]}
```bash
${command["usage"]}
```
```bash
${command["help"]}
```
${"####"} Examples:
% for example in command["examples"]:
${example["description"]}
```bash
${example["output"]}
```
% endfor
% endfor
"""
    ).render(command_metas=command_metas)
    with open(
            os.path.normpath(
                os.path.join(__file__, "..", "..", "doc", "docs", "commands.md")
            ),
            "w",
    ) as f:
        f.write(command_file_content)


def copy_readmes():
    root_readme = os.path.normpath(os.path.join(
        __file__,
        "..",
        "..",
        "README.md"
    ))
    plugin_readme = os.path.normpath(os.path.join(
        __file__,
        "..",
        "..",
        "plugin",
        "README.md"
    ))
    docs_readme = os.path.normpath(os.path.join(
        __file__,
        "..",
        "..",
        "doc",
        "docs",
        "index.md"
    ))
    shutil.copyfile(root_readme, plugin_readme)
    shutil.copyfile(root_readme, docs_readme)


if __name__ == "__main__":
    try:
        generate_commands()
        copy_readmes()
    except Exception as e:
        print(e)
        print(traceback.format_exc())
