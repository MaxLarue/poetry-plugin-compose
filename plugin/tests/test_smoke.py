import os
from typing import List

import pytest

from poetry_plugin_compose.composed_commands.sub_command_runner import (
    run_sub_command_sync,
)


def run_poetry(args: List[str]):
    root_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
    # use the env var $POETRY_EXEC so we don't end up using one in a virtual env
    return run_sub_command_sync(["$POETRY_EXEC", *args], root_path)


@pytest.mark.slow
def test_smoke_run_command():
    assert run_poetry(["compose", "run", "black", "."]) == 0


@pytest.mark.slow
def test_smoke_run_ignore_command():
    assert run_poetry(["compose", "-i", "mkdocs", "--", "black", "."]) == 0


@pytest.mark.slow
def test_smoke_run_contains():
    assert run_poetry(["compose", "-c", "tests", "--", "black", "."]) == 0
