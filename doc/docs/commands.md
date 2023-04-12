# Commands

## Compose (default)

Default to run command
```bash
poetry compose pytest
```

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