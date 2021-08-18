"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!


def main():
    score = float(input("Enter score: "))
    print(score)
    print(score_result(score))


def score_result(score):
    if score < 0:
        return "Invalid score"
    else:
        if score > 100:
            return "Invalid score"
        elif score >= 50:
            return "Passable"
        elif score >= 90:
            return "Excellent"
    if score < 50:
        return "Bad"


main()
