"""
this module contains the function that is used in scoreloop to
fetch highest scores from the database
"""
import sqlite3


def fetch_scores():
    """
    this function simply connects to the scores.db database and queries it for 10 highest scores,
    cleans the returned list from the query and then it retruns the list

    Retrun:
        the list containing top 10 scores in order
    """

    scores = sqlite3.connect("data/scores.db")
    scores.isolation_level = None

    high_scores = scores.execute(
        "SELECT score FROM Scores ORDER BY -score LIMIT 10").fetchall()

    high_scores = [score[0] for score in high_scores]

    return high_scores


if __name__ == "__main__":

    print(fetch_scores())
