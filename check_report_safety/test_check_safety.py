import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parent))

from check_safety import count_safe_reports, is_report_safe
from example_input import input_data


@pytest.mark.parametrize(
    ("levels", "expected"),
    [
        ([1, 3, 5, 8], True),
        ([8, 6, 4, 2], True),
        ([1, 3, 2, 4], False),
        ([1, 2, 6], False),
        ([1, 2, 2], False),
    ],
)
def test_is_report_safe(levels, expected):
    assert is_report_safe(levels) is expected


def test_count_safe_reports_matches_full_advent_input():
    assert count_safe_reports(input_data) == 670
