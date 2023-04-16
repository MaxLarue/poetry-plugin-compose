import os

import tomli


def get_package_descriptor(package: str):
    with open(os.path.join(package, 'pyproject.toml'), 'rb') as f:
        pyproject = tomli.load(f)
        name = pyproject.get("tool", {}).get("poetry", {}).get("name")
        return {"name": name, "dir": package}
