"""
This module contains the function that adds the score to the database in the end of a gameloop
"""
import sqlite3


def add_score(score):
    """
    connects to the scores database and inserts the value of the parameter to the database

    Args:
        score: the value that will be added to the database
    """

    scores = sqlite3.connect("data/scores.db")
    scores.isolation_level = None

    scores.execute(f"INSERT INTO Scores (score) VALUES ({score})")


if __name__ == "__main__":
    pass
