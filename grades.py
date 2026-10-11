"""Grade calculator."""

PASS_MARK = 10


def has_passed(grade):
    return grade >= PASS_MARK


def average(grades):
    if not grades:
        return 0.0
    return sum(grades) / len(grades)
