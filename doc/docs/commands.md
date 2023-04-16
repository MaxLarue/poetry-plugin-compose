# Commands


## Run

Runs a poetry (run) command in every sub-directory containing a `pyproject.toml` file
```bash
poetry compose run pytest
```

#### options

##### ignore-missing
`-i,--ignore-missing`
Do not run command if a package is not installed in the sub package

eg: run pytest in every package where pytest is installed
```bash
poetry compose -i pytest -- pytest
```

##### contains
`-c,--contains`
Only runs command if sub-package contains a specific file

eg: run pytest in every package that has `entry_point.py` file
```bash
poetry compose -c entry_point.py -- pytest
```

## install

Runs poetry install in every subdirectory containing a `pyproject.toml` file
```bash
poetry compose install -- --no-dev
```
every argument past the separator is passed to the install command

run the same command in every sub-package with a filter

```bash
poetry compose install -c entry_point.py -- --no-dev
```

In order to differentiate between compose's own arguments and 
the arguments passed to the sub(composed command)
you might have to include the separator `--` even
if you don't pass extra arguments to the sub command

#### options

##### ignore-missing
`-i,--ignore-missing`
Do not run command if a package is not installed in the sub package

eg: install only if boto3 is installed
```bash
poetry compose install -i boto3 --
```

##### contains
`-c,--contains`
Only runs install if sub-package contains a specific file

eg: install in every package that has `entry_point.py` file
```bash
poetry compose install -c entry_point.py
```

## add

Add a dependency in every subdirectory containing a `pyproject.toml` file
```bash
poetry compose add flake8
```

run the same command in every sub-package with a filter

```bash
poetry compose add -i pytest -- flake8
```

#### options

##### ignore-missing
`-i,--ignore-missing`
Do not run command if a package is not installed in the sub package

eg: add only if boto3 is installed
```bash
poetry compose add -i boto3 --
```

##### contains
`-c,--contains`
Only runs add if sub-package contains a specific file

eg: add in every package that has `entry_point.py` file
```bash
poetry compose add -c entry_point.py
```

## build

Runs poetry build in every subdirectory containing a `pyproject.toml` file
```bash
poetry compose build
```
every argument past the separator is passed to the install command

run the same command in every sub-package with a filter

```bash
poetry compose build -c entry_point.py --
```

when passing arguments to build
```bash
poetry compose build -i pytest -- --no-cache
```

In order to differentiate between compose's own arguments and 
the arguments passed to the sub(composed command)
you might have to include the separator `--` even
if you don't pass extra arguments to the sub command

#### options

##### ignore-missing
`-i,--ignore-missing`
Do not run command if a package is not installed in the sub package

eg: build only if boto3 is installed
```bash
poetry compose build -i boto3 --
```

##### contains
`-c,--contains`
Only runs build if sub-package contains a specific file

eg: build in every package that has `entry_point.py` file
```bash
poetry compose build -c entry_point.py
```


## check

Runs poetry check in every subdirectory containing a `pyproject.toml` file
```bash
poetry compose check
```
every argument past the separator is passed to the install command

run the same command in every sub-package with a filter

```bash
poetry compose check -c entry_point.py --
```

when passing arguments to check
```bash
poetry compose check -i pytest -- --quiet
```

In order to differentiate between compose's own arguments and 
the arguments passed to the sub(composed command)
you might have to include the separator `--` even
if you don't pass extra arguments to the sub command

#### options

##### ignore-missing
`-i,--ignore-missing`
Do not run command if a package is not installed in the sub package

eg: install only if boto3 is installed
```bash
poetry compose check -i boto3 --
```

##### contains
`-c,--contains`
Only runs check if sub-package contains a specific file

eg: check in every package that has `entry_point.py` file
```bash
poetry compose check -c entry_point.py
```


## lock

Runs poetry lock in every subdirectory containing a `pyproject.toml` file
```bash
poetry compose lock
```
every argument past the separator is passed to the install command

run the same command in every sub-package with a filter

```bash
poetry compose lock -c entry_point.py --
```

when passing arguments to lock
```bash
poetry compose lock -i pytest -- --check
```

In order to differentiate between compose's own arguments and 
the arguments passed to the sub(composed command)
you might have to include the separator `--` even
if you don't pass extra arguments to the sub command

#### options

##### ignore-missing
`-i,--ignore-missing`
Do not run command if a package is not installed in the sub package

eg: install only if boto3 is installed
```bash
poetry compose lock -i boto3 --
```

##### contains
`-c,--contains`
Only runs lock if sub-package contains a specific file

eg: lock in every package that has `entry_point.py` file
```bash
poetry compose lock -c entry_point.py
```

## remove

Removes a dependency in every subdirectory containing a `pyproject.toml` file
```bash
poetry compose remove flake8
```

run the same command in every sub-package with a filter

```bash
poetry compose remove -i pytest -- flake8
```

#### options

##### ignore-missing
`-i,--ignore-missing`
Do not run command if a package is not installed in the sub package

eg: remove only if boto3 is installed
```bash
poetry compose remove -i boto3 --
```

##### contains
`-c,--contains`
Only runs remove if sub-package contains a specific file

eg: remove in every package that has `entry_point.py` file
```bash
poetry compose remove -c entry_point.py
```

## update

Update dependencies in every subdirectory containing a `pyproject.toml` file
```bash
poetry compose update flake8
```

run the same command in every sub-package with a filter

```bash
poetry compose update -i pytest -- flake8
```

#### options

##### ignore-missing
`-i,--ignore-missing`
Do not run command if a package is not installed in the sub package

eg: update only if boto3 is installed
```bash
poetry compose update -i boto3 --
```

##### contains
`-c,--contains`
Only runs update if sub-package contains a specific file

eg: update in every package that has `entry_point.py` file
```bash
poetry compose update -c entry_point.py
```
