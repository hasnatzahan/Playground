# solution of https://adventofcode.com/2024/day/2

from example_input import input_data

def is_report_safe(levels):
    """
    Determines whether a report is safe.

    A report is safe when:
    1. Levels are either strictly increasing or strictly decreasing.
    2. The difference between adjacent levels is between 1 and 3.
    """

    differences = []

    # Calculate the difference between every pair of adjacent levels
    for i in range(len(levels) - 1):
        difference = levels[i + 1] - levels[i]
        differences.append(difference)

    # Check if the report is consistently increasing
    is_increasing = True
    for difference in differences:
        if difference <= 0:
            is_increasing = False
            break

    # Check if the report is consistently decreasing
    is_decreasing = True
    for difference in differences:
        if difference >= 0:
            is_decreasing = False
            break

    # If the levels are neither increasing nor decreasing, it is unsafe
    if not is_increasing and not is_decreasing:
        return False

    # Check that every step changes by at least 1 and at most 3
    for difference in differences:
        if abs(difference) < 1 or abs(difference) > 3:
            return False

    return True


def count_safe_reports(input_data):
    """
    Reads all reports and returns the number of safe reports.
    """

    safe_report_count = 0

    # Each line represents one report
    reports = input_data.strip().split("\n")

    for report in reports:

        # Convert the string values into integers
        levels = []
        for value in report.split():
            levels.append(int(value))

        # Count the report if it is safe
        if is_report_safe(levels):
            safe_report_count += 1

    return safe_report_count

result = count_safe_reports(input_data)

print(f"Number of safe reports: {result}")