# Study planner

The study planner reads tasks from CSV, ranks them by urgency and importance,
allocates the available study time, and prints a short plan.

## Run the planner

From the repository root, run:

```bash
python -m shared.study_planner samples/tasks.csv --hours 2
```

Example output:

```text
Tonight (1.5 h):
1. Assignment: 1.5 h
```

The allocator schedules a task only when the whole task fits in the remaining
time. In this example, the six-hour `DS exam` task does not fit after the
assignment.

## CSV format

The input file must contain these columns:

```csv
title,importance,effort_h,deadline
DS exam,5,6,2026-10-30
Assignment,4,1.5,2026-10-27
```

- `importance` is an integer from 1 to 5.
- `effort_h` is the estimated number of hours.
- `deadline` uses the `YYYY-MM-DD` format.

## Workflow

The command-line entry point connects the core modules in this order:

```text
parse_csv -> prioritise -> allocate -> render
```

Other modules provide validation, upcoming-task filtering, error handling,
statistics, JSON storage, and Markdown or text export for callers that need
those features.

If the CSV file is missing or invalid, the command prints a clear error to
standard error and exits with status code 1.

## Verify the project

```bash
pytest -q tests/test_e2e.py
pytest -q
ruff check . --select E4,E7,E9,F
```

See [`docs/demo.md`](../../docs/demo.md) for a short execution demo.
