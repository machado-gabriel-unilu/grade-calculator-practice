"""Quick checks for grades.py. Run with: python3 test_grades.py"""

import grades


def test_pass_mark():
    assert grades.PASS_MARK == 10


if __name__ == "__main__":
    test_pass_mark()
    print("All tests passed")
