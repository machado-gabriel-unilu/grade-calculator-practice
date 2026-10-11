"""Simulates "three weeks later": 12 small commits by three teammates.

Commit 7 secretly breaks the pass mark (>= becomes >).
Run it ONCE, on your own branch, right after tagging v1.0:

    python3 simulate_three_weeks.py

It never pushes anything. Change the three names below if you like.
"""
import subprocess
import sys

TEAM = ["Presenter 1", "Presenter 2", "Presenter 3"]


def git(*args):
    return subprocess.run(["git", *args], check=True,
                          capture_output=True, text=True).stdout.strip()


def commit(author, message):
    email = author.replace(" ", "").lower() + "@example.com"
    git("-c", f"user.name={author}", "-c", f"user.email={email}",
        "commit", "-q", "-am", message)


def add_line(path, text):
    with open(path, "a", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


# Safety: never run this on main.
if git("branch", "--show-current") == "main":
    sys.exit("You're on main. Switch to your own branch first.")

p1, p2, p3 = TEAM

add_line("NOTES.md", "# Team notes")
git("add", "NOTES.md")
commit(p1, "Start team notes")                                  # 1
add_line("NOTES.md", "Grades are out of 20.")
commit(p2, "Note the grading scale")                            # 2
add_line("NOTES.md", "Team: " + ", ".join(TEAM))
commit(p3, "Add contributors to notes")                         # 3
add_line("grades.py", "\n\ndef best(grades):\n    return max(grades)")
commit(p1, "Add best grade")                                    # 4
add_line("grades.py", "\n\ndef worst(grades):\n    return min(grades)")
commit(p2, "Add worst grade")                                   # 5
add_line("NOTES.md", "Run the tests with: python3 test_grades.py")
commit(p3, "Explain how to run the tests")                      # 6

# --- 7: the bad commit ---
with open("grades.py", encoding="utf-8", newline="") as f:
    code = f.read()
with open("grades.py", "w", encoding="utf-8", newline="") as f:
    f.write(code.replace("grade >= PASS_MARK", "grade > PASS_MARK"))
commit(p1, "Tidy up has_passed")                                # 7

add_line("NOTES.md", "Fixed a typo.")
commit(p2, "Fix typo in notes")                                 # 8
add_line("grades.py", "\n\ndef count(grades):\n    return len(grades)")
commit(p3, "Add number of grades")                              # 9
add_line("NOTES.md", "Example: average([12, 15, 9]) is 12.0")
commit(p1, "Add example grades to notes")                       # 10
add_line("NOTES.md", "These notes help new teammates get started.")
commit(p2, "Reword the notes intro")                            # 11
add_line("NOTES.md", "Todo: export grades to a file.")
commit(p3, "Add a todo list to notes")                          # 12

print("Done: 12 new commits since v1.0.")
print(git("log", "--oneline", "v1.0..HEAD"))
