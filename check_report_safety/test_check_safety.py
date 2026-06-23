import sys
from pathlib import Path

import pytest

sys.path.append(str(Path(__file__).resolve().parent))

from check_safety import (
    count_safe_reports,
    is_report_safe_with_dampener,
)
from example_input import input_data


@pytest.mark.parametrize(
    ("levels", "expected"),
    [
        ([1, 3, 5, 8], True),
        ([8, 6, 4, 2], True),
        ([1, 3, 2, 4], True),
        ([1, 2, 6], True),
        ([1, 2, 2], True),
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], True),
        ([8, 6, 4, 4, 1], True),
        ([1, 3, 6, 7, 9], True),
    ],
)
def test_is_report_safe_with_dampener(levels, expected):
    assert is_report_safe_with_dampener(levels) is expected


def test_count_safe_reports_matches_full_advent_input():
    assert count_safe_reports(input_data) == 700
