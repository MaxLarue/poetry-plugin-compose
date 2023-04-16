from poetry_plugin_compose.composed_commands.composed_command_utils import (
    split_compose_command_and_sub_command,
)


def test_with_simple_run():
    assert split_compose_command_and_sub_command(["run", "pytest"]) == (
        ["run"],
        ["pytest"],
    )


def test_with_run_with_filter():
    assert split_compose_command_and_sub_command(
        ["run", "-i", "pytest", "--", "pytest"]
    ) == (["run", "-i", "pytest"], ["pytest"])


def test_with_run_with_args():
    assert split_compose_command_and_sub_command(["run", "pytest", "-m'not slow'"]) == (
        ["run"],
        ["pytest", "-m'not slow'"],
    )


def test_with_run_with_args_and_filters():
    assert split_compose_command_and_sub_command(
        ["run", "-i", "pytest", "--", "pytest", "-m'not slow'"]
    ) == (["run", "-i", "pytest"], ["pytest", "-m'not slow'"])


def test_with_install_no_args():
    assert split_compose_command_and_sub_command(["install"]) == (["install"], [])


def test_with_install_with_filters():
    assert split_compose_command_and_sub_command(["install", "-i", "pytest", "--"]) == (
        ["install", "-i", "pytest"],
        [],
    )


def test_with_install_with_args():
    assert split_compose_command_and_sub_command(["install", "--no-root"]) == (
        ["install"],
        ["--no-root"],
    )


def test_with_install_with_args_and_filters():
    assert split_compose_command_and_sub_command(
        ["install", "-i", "pytest", "--", "--no-root"]
    ) == (
        ["install", "-i", "pytest"],
        ["--no-root"],
    )
