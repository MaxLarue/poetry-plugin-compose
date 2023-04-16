import os

import tomli


class DependenciesDetectionException(Exception):
    def __init__(self, package: str):
        super(DependenciesDetectionException, self).__init__(f"Could not determine package {package} dependencies")
        self.package = package


def get_package_dependencies(package: str):
    with open(os.path.join(package, 'pyproject.toml'), 'rb') as f:
        pyproject = tomli.load(f)
        return pyproject.get("tool", {}).get("poetry", {}).get("dependencies", [])