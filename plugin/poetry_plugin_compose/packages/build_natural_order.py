from poetry_plugin_compose.packages.discover_packages import discover_packages
from poetry_plugin_compose.packages.get_package_descriptor import get_package_descriptor


def build_natural_order():
    packages = discover_packages(".")
    package_map = {}
    for package in packages:
        package_descriptor = get_package_descriptor(package)
        package_map[package_descriptor.name] = package_descriptor
    return package_map.keys(), package_map
