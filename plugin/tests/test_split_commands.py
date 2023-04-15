from poetry_plugin_compose.composed_commands.composed_command_utils import split_root_command_and_sub_command


def test_with_simple_run():
    assert split_root_command_and_sub_command(["run", "pytest"]) == ["run"], ["pytest"]