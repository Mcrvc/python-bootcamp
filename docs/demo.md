# Study planner demo

Run all commands from the repository root.

## Generate a plan

The repository includes `samples/tasks.csv`, so the planner can be tried
without creating another input file:

```bash
python -m shared.study_planner samples/tasks.csv --hours 2
```

Expected output:

```text
Tonight (1.5 h):
1. Assignment: 1.5 h
```

The assignment is scheduled first because its deadline is closer. The
six-hour exam does not fit in the remaining half hour, so it is skipped.

## Check error handling

```bash
python -m shared.study_planner missing.csv --hours 2
```

Expected error:

```text
Error: file not found: missing.csv
```

The command returns exit status 1 for the missing file.
