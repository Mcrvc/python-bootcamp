import pytest
from datetime import date
from shared.contract import Task
from shared.study_planner.parse import parse_csv


def test_parse_csv_valid(tmp_path):
    csv_file = tmp_path / "tasks.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        "DS exam,5,6.0,2026-10-30\n"
        "Assignment,4,1.5,2026-10-27\n",
        encoding="utf-8"
    )

    tasks = parse_csv(csv_file)

    assert len(tasks) == 2
    assert isinstance(tasks[0], Task)
    assert tasks[0].title == "DS exam"
    assert tasks[0].importance == 5
    assert tasks[0].effort_h == 6.0
    assert tasks[0].deadline == date(2026, 10, 30)


def test_parse_csv_empty_rows(tmp_path):
    csv_file = tmp_path / "empty.csv"
    csv_file.write_text("title,importance,effort_h,deadline\n", encoding="utf-8")

    tasks = parse_csv(csv_file)
    assert tasks == []


def test_parse_csv_file_not_found():
    with pytest.raises(FileNotFoundError):
        parse_csv("path/does_not_exist.csv")


def test_parse_csv_invalid_header(tmp_path):
    csv_file = tmp_path / "bad_header.csv"
    csv_file.write_text("name,priority,hours,due\n1,2,3,4\n", encoding="utf-8")

    with pytest.raises(ValueError, match="CSV file header error or column missing."):
        parse_csv(csv_file)


def test_parse_csv_invalid_data_types(tmp_path):
    csv_file = tmp_path / "corrupted.csv"
    csv_file.write_text(
        "title,importance,effort_h,deadline\n"
        "Good Task,3,2.0,2026-10-25\n"
        "Bad Task,abc,2.0,30-10-2026\n",  
        encoding="utf-8"
    )

    with pytest.raises(ValueError, match="data"):
        parse_csv(csv_file)