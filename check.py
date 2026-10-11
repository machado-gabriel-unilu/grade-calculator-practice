"""Bug check: a grade of exactly 10/20 must be a pass."""
import sys
from grades import has_passed

if has_passed(10):
    print("PASS: 10/20 counts as passed")
    sys.exit(0)
print("FAIL: 10/20 is shown as failed")
sys.exit(1)
