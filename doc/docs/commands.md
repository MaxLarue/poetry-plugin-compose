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
poetry compose install -i entry_point.py -- --no-dev
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