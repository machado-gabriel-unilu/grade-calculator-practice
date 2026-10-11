"""Grade calculator."""

PASS_MARK = 10


def average(grades):
    return sum(grades) / len(grades)


def has_passed(grade):
    return grade >= PASS_MARK
