# Python Bootcamp - CSC10014 (Team 06)

This repository covers a 3-week Python homework track that teaches Python
by comparison with C++ for 7 team members. Each member works in
`members/<username>/w1|w2|w3/`, the team code lives in `shared/`, and every
exercise is submitted through a pull request.

## Structure

```text
python-bootcamp/
|-- README.md
|-- PROGRESS.md
|-- members/
|   |-- akagikay/
|   |   |-- w1/  w2/  w3/
|   |-- ilovecats123abc/
|   |   |-- w1/  w2/  w3/
|   |-- mcrvc/
|   |   |-- w1/  w2/  w3/
|   |-- n3ykh/
|   |   |-- w1/  w2/  w3/
|   |-- tba0407/
|   |   |-- w1/  w2/  w3/
|   |-- tbanh2516_dot/
|   |   |-- w1/  w2/  w3/
|   |-- truonghuy0411/
|       |-- w1/  w2/  w3/
|-- shared/
|   |-- contract.py
|   |-- study_planner/
|-- tests/
    |-- .gitkeep
```

> Folder names use **underscores** and **lowercase**
> (`mcrvc`, `ilovecats123abc`) because Python cannot import
> a module with a hyphen or mixed case.

## Rules

### Branch naming

| Prefix | Use for | Example |
|---|---|---|
| `py/w<N>-` | Weekly Python homework | `py/w1-minh_nv` |

### Commit messages

Follow **Conventional Commits**: `<type>(<scope>): <summary>`

| Type | Meaning |
|---|---|
| `feat` | new capability |
| `fix` | bug fix |
| `docs` | documentation only |
| `test` | tests / benchmark cases |
| `refactor` | restructure, no behaviour change |
| `perf` | faster or cheaper, same behaviour |
| `style` | formatting only |
| `chore` | tooling, dependencies, CI |

**Example:** `feat(py-w1): W1-2 word counter`

### Pull requests

- **Title:** `py-w<N>: <username>` — e.g. `py-w1: minh_nv`
- **Link the issue:** write `Closes #<N>` in the PR description
- **Request review** from your rotation reviewer
- **Merge only when:** CI is green **and** at least 1 approval is given
- **After merge:** delete the branch

### Where to write code

- Individual exercises → **only** in `members/<your_folder>/`
- Team exercises → in `shared/`
- Never edit another member's folder
- Pair work → add a `Co-authored-by:` trailer

### Review rotation

Follow the rotation table in `docs/team.md`.

### Weekly tags

Pushed by the Tech Lead after all members have merged:

`py-w1-done` · `py-w2-done` · `py-w3-done`

### Never commit

- `.env`, API keys, secrets
- Real personal data
- Files larger than 5 MB
- Generated files or virtual environments

### Every PR must

- [ ] link its issue (`Closes #N`)
- [ ] pass CI (`pytest -q`, `ruff check`)
- [ ] get 1 approval from another member
- [ ] disclose AI use, or write `None`
- [ ] be small and focused (≈ 100–300 changed lines)

### Review etiquette

- Review within 24 hours
- Label comments: `Blocking` / `Question` / `Suggestion` / `Nit` / `Praise`
- Approve only what you actually read and understood

## How to run tests

### Create the environment

```bash
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\Activate.ps1
```

### Setup

```bash
pip install pytest ruff
```

### Run all bootcamp tests

```bash
pytest -q python-bootcamp
```

### Run one week's test

```bash
pytest -q python-bootcamp/tests/test_w1.py
```

### Run one member's test with variant

```bash
pytest -q python-bootcamp/tests/test_w1.py --member minh_nv --variant 1
```

> The `--member` and `--variant` flags are provided by
> `python-bootcamp/tests/conftest.py` (instructor-supplied).

### Check code style

```bash
ruff check python-bootcamp
```

### Check your own progress

```bash
# Commits per member
git shortlog -sne --no-merges -- python-bootcamp/members/

# One member's commits
git log --no-merges --oneline --author="Lan" -- python-bootcamp/

# Merged PRs with a weekly label
gh pr list --state merged --label w2 --json author,number,title
```

### Run tests before every push

```bash
pytest -q python-bootcamp && ruff check python-bootcamp
```