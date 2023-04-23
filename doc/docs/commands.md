# Commands
## install
> Run install in multiple sub-packages
```bash
usage: poetry compose install [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

```
```bash
usage: poetry compose install [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

Run install in multiple sub-packages

optional arguments:
  -h, --help            show this help message and exit
  -i IGNORE_MISSING, --ignore-missing IGNORE_MISSING
                        Only run in packages that have this dependency
  -c CONTAINS, --contains CONTAINS
                        Only run in packages that include this file
  -d DIRECTORY, --directory DIRECTORY
                        Only run in selected directory

```
#### Examples:
run poetry install in every sub-package
```bash
poetry compose install
```
run poetry install in the integration_test package
```bash
poetry compose install -d integration_test --
```
## add
> Add a dependency to every sub-packages
```bash
usage: poetry compose add [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

```
```bash
usage: poetry compose add [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

Add a dependency to every sub-packages

optional arguments:
  -h, --help            show this help message and exit
  -i IGNORE_MISSING, --ignore-missing IGNORE_MISSING
                        Only run in packages that have this dependency
  -c CONTAINS, --contains CONTAINS
                        Only run in packages that include this file
  -d DIRECTORY, --directory DIRECTORY
                        Only run in selected directory

```
#### Examples:
add flake8 to every sub-packages
```bash
poetry compose add flake8
```
add flake8 to every subpackage where black is installed
```bash
poetry compose install -i black -- flake8
```
add flake8 as a dev dependency to every subpackage where black is installed
```bash
poetry compose install -i black -- flake8 --group-dev
```
## build
> Build sub packages
```bash
usage: poetry compose build [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

```
```bash
usage: poetry compose build [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

Build sub packages

optional arguments:
  -h, --help            show this help message and exit
  -i IGNORE_MISSING, --ignore-missing IGNORE_MISSING
                        Only run in packages that have this dependency
  -c CONTAINS, --contains CONTAINS
                        Only run in packages that include this file
  -d DIRECTORY, --directory DIRECTORY
                        Only run in selected directory

```
#### Examples:
run poetry build in every sub-package
```bash
poetry compose build
```
run poetry build in the integration_test package
```bash
poetry compose build -d integration_test --
```
## check
> Run poetry check in sub-packages
```bash
usage: poetry compose check [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

```
```bash
usage: poetry compose check [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

Run poetry check in sub-packages

optional arguments:
  -h, --help            show this help message and exit
  -i IGNORE_MISSING, --ignore-missing IGNORE_MISSING
                        Only run in packages that have this dependency
  -c CONTAINS, --contains CONTAINS
                        Only run in packages that include this file
  -d DIRECTORY, --directory DIRECTORY
                        Only run in selected directory

```
#### Examples:
run poetry check in every sub-package
```bash
poetry compose check
```
run poetry check in the integration_test package
```bash
poetry compose check -d integration_test --
```
## lock
> Lock sub packages
```bash
usage: poetry compose lock [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

```
```bash
usage: poetry compose lock [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

Lock sub packages

optional arguments:
  -h, --help            show this help message and exit
  -i IGNORE_MISSING, --ignore-missing IGNORE_MISSING
                        Only run in packages that have this dependency
  -c CONTAINS, --contains CONTAINS
                        Only run in packages that include this file
  -d DIRECTORY, --directory DIRECTORY
                        Only run in selected directory

```
#### Examples:
run poetry lock in every sub-package
```bash
poetry compose lock
```
run poetry lock in the integration_test package
```bash
poetry compose lock -d integration_test --
```
## publish
> Publish sub packages
```bash
usage: poetry compose publish [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

```
```bash
usage: poetry compose publish [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

Publish sub packages

optional arguments:
  -h, --help            show this help message and exit
  -i IGNORE_MISSING, --ignore-missing IGNORE_MISSING
                        Only run in packages that have this dependency
  -c CONTAINS, --contains CONTAINS
                        Only run in packages that include this file
  -d DIRECTORY, --directory DIRECTORY
                        Only run in selected directory

```
#### Examples:
run poetry publish in every sub-package
```bash
poetry compose publish
```
run poetry publish in the integration_test package
```bash
poetry compose publish -d integration_test --
```
## remove
> Removes a dependency from every sub-packages
```bash
usage: poetry compose remove [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

```
```bash
usage: poetry compose remove [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

Removes a dependency from every sub-packages

optional arguments:
  -h, --help            show this help message and exit
  -i IGNORE_MISSING, --ignore-missing IGNORE_MISSING
                        Only run in packages that have this dependency
  -c CONTAINS, --contains CONTAINS
                        Only run in packages that include this file
  -d DIRECTORY, --directory DIRECTORY
                        Only run in selected directory

```
#### Examples:
remove flake8 from every sub-packages
```bash
poetry compose remove flake8
```
remove flake8 from every subpackage where black is installed
```bash
poetry compose install -i black -- flake8
```
remove flake8 as a dev dependency from every subpackage where black is installed
```bash
poetry compose install -i black -- flake8 --group-dev
```
## update
> Updates dependencies in every sub-packages
```bash
usage: poetry compose update [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

```
```bash
usage: poetry compose update [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

Updates dependencies in every sub-packages

optional arguments:
  -h, --help            show this help message and exit
  -i IGNORE_MISSING, --ignore-missing IGNORE_MISSING
                        Only run in packages that have this dependency
  -c CONTAINS, --contains CONTAINS
                        Only run in packages that include this file
  -d DIRECTORY, --directory DIRECTORY
                        Only run in selected directory

```
#### Examples:
run poetry update in every sub-package
```bash
poetry compose update
```
run poetry update in the integration_test package
```bash
poetry compose update -d integration_test --
```
## run
> Run multiple commands in parallel
```bash
usage: poetry compose run [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

```
```bash
usage: poetry compose run [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

Run multiple commands in parallel

optional arguments:
  -h, --help            show this help message and exit
  -i IGNORE_MISSING, --ignore-missing IGNORE_MISSING
                        Only run in packages that have this dependency
  -c CONTAINS, --contains CONTAINS
                        Only run in packages that include this file
  -d DIRECTORY, --directory DIRECTORY
                        Only run in selected directory

```
#### Examples:
run poetry run pytest in every sub-package
```bash
poetry compose run pytest
```
run pytest in every sub-package where it is installed
```bash
poetry compose run -i pytest -- pytest -s
```
## dependency-order
> Find dependency order between packages
```bash
usage: poetry compose dependency-order [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

```
```bash
usage: poetry compose dependency-order [-h] [-i IGNORE_MISSING] [-c CONTAINS] [-d DIRECTORY]

Find dependency order between packages

optional arguments:
  -h, --help            show this help message and exit
  -i IGNORE_MISSING, --ignore-missing IGNORE_MISSING
                        Only run in packages that have this dependency
  -c CONTAINS, --contains CONTAINS
                        Only run in packages that include this file
  -d DIRECTORY, --directory DIRECTORY
                        Only run in selected directory

```
#### Examples:
get a valid dependency order of every sub package
```bash
poetry compose dependency-order
```
