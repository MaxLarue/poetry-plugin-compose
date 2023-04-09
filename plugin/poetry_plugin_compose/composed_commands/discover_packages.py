import os


def discover_packages(directory):
    stack = [directory]
    packages = []
    while stack:
        current = stack.pop()
        content = os.listdir(current)
        if 'pyproject.toml' in content and current != directory:
            packages.append(current)
        else:
            for file in [directory for directory in content if os.path.isdir(directory)]:
                stack.append(os.path.join(current, file))
    return packages
