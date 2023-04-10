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

- `-i,--ignore-missing`: Do not run command if 