"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!
import random


def main():
    score = float(input("Enter score: "))
    print(score)
    print(score_result(score))
    random_score = random.randint(1, 100)
    print(random_score)


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
