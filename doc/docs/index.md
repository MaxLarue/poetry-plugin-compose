# Poetry compose

A poetry plugin to manage multiple project from a single root, a-la monorepo

## Getting started

Install plugin

```bash
poetry self add poetry-plugin-compose
```

Start linting all sub projects in a single line

```bash
poetry compose flake8 .
```
or
```bash
poetry compose run flake8 .
```