"""Grade calculator."""

PASS_MARK = 10


def has_passed(grade):
    return grade >= PASS_MARK


def average(grades):
    return sum(grades) / len(grades)
