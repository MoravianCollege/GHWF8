
from grades import compute_hw_average


def test_zero_grades():

""" What is Computer Science

I also want to know what is the absolute truth?
"""

    grades = []
    assert compute_hw_average(grades) == 0


def test_single_grade():
    grades = [42]
    assert compute_hw_average(grades) == 42
