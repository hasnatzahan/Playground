# solution of https://adventofcode.com/2024/day/2

from example_input import input_data


# def _is_report_safe_under_original_rules(levels):
#     """Return True when a report satisfies the original safety rules."""
#     if len(levels) < 2:
#         return True

#     differences = [levels[index + 1] - levels[index] for index in range(len(levels) - 1)]

#     is_increasing = all(difference > 0 for difference in differences)
#     is_decreasing = all(difference < 0 for difference in differences)

#     if not is_increasing and not is_decreasing:
#         return False

#     return all(1 <= abs(difference) <= 3 for difference in differences)


# def is_report_safe(levels):
#     """
#     Determine whether a report is safe.

#     A report is considered safe when either:
#     - it already satisfies the original safety rules, or
#     - removing exactly one level makes it satisfy those rules.
#     """
#     if _is_report_safe_under_original_rules(levels):
#         return True

#     for index in range(len(levels)):
#         reduced_levels = levels[:index] + levels[index + 1 :]
#         if _is_report_safe_under_original_rules(reduced_levels):
#             return True

#     return False


# def count_safe_reports(input_data):
#     """Read a block of reports and return how many are safe."""
#     safe_report_count = 0

#     reports = input_data.strip().split("\n")

#     for report in reports:
#         levels = [int(value) for value in report.split()]

#         if is_report_safe(levels):
#             safe_report_count += 1

#     return safe_report_count

def is_report_safe(levels):
    """
    Checks whether a report is safe.

    A report is safe when:
    1. Levels are either strictly increasing or strictly decreasing.
    2. The difference between adjacent levels is between 1 and 3.
    """

    differences = []

    # Calculate the difference between adjacent levels
    for i in range(len(levels) - 1):
        difference = levels[i + 1] - levels[i]
        differences.append(difference)

    # Check if all levels are increasing
    is_increasing = True

    for difference in differences:
        if difference <= 0:
            is_increasing = False
            break

    # Check if all levels are decreasing
    is_decreasing = True

    for difference in differences:
        if difference >= 0:
            is_decreasing = False
            break

    # Report must be either increasing or decreasing
    if not is_increasing and not is_decreasing:
        return False

    # Check the difference between levels is valid
    for difference in differences:
        if abs(difference) < 1 or abs(difference) > 3:
            return False

    return True


def is_report_safe_with_dampener(levels):
    """
    Checks if a report is safe with the Problem Dampener.

    A report is safe if:
    - It is already safe
    - OR removing exactly one level makes it safe
    """

    # First check the original report
    if is_report_safe(levels):
        return True

    # Try removing each level one at a time
    for index in range(len(levels)):

        modified_levels = []

        # Create a new report without the current level
        for i in range(len(levels)):
            if i != index:
                modified_levels.append(levels[i])

        # Check if removing this level makes it safe
        if is_report_safe(modified_levels):
            return True

    return False


def count_safe_reports(input_data):
    """
    Counts how many reports are safe using the Problem Dampener rule.
    """

    safe_report_count = 0

    reports = input_data.strip().split("\n")

    for report in reports:

        # Convert string values into integers
        levels = []

        for value in report.split():
            levels.append(int(value))

        # Check with dampener rules
        if is_report_safe_with_dampener(levels):
            safe_report_count += 1

    return safe_report_count


if __name__ == "__main__":
    result = count_safe_reports(input_data)
    print(f"Number of safe reports: {result}")