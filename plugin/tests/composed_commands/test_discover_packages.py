import os

import pytest

from poetry_plugin_compose.composed_commands.discover_packages import (
    discover_packages_matching,
    is_directory_containing_file,
)


@pytest.fixture
def discovered_root_txt_packages():
    FIXTURE_PATH = os.path.join(os.getcwd(), "tests", "fixtures", "not-a-project")
    print("fixture path", FIXTURE_PATH)
    return discover_packages_matching(
        FIXTURE_PATH,
        lambda directory: is_directory_containing_file(directory, "root.txt"),
    )


@pytest.fixture
def directory_names(discovered_root_txt_packages):
    return [os.path.basename(directory) for directory in discovered_root_txt_packages]


def test_discover_packages_based_on_containing_root_txt_found_2(
    discovered_root_txt_packages,
):
    assert len(discovered_root_txt_packages) == 2


def test_discover_packages_based_on_containing_root_txt_contains_sub1(directory_names):
    assert "sub1" in directory_names


def test_discover_packages_based_on_containing_root_txt_contains_sub2(directory_names):
    assert "sub2" in directory_names


def test_discover_packages_based_on_containing_root_txt_not_contains_root(
    directory_names,
):
    assert "not-a-project" not in directory_names
