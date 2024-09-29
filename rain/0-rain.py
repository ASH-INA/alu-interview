#!/usr/bin/python3
"""
Given a list of non-negative integers representing the heights of
walls with unit width 1, as if viewing the cross-section of a
relief map, calculate how many square units of water will be
retained after it rains.

    Prototype: def rain(walls)
    walls is a list of non-negative integers.
    Return: Integer indicating total amount of rainwater retained.
    Assume that the ends of the list (before index 0 and after
    index walls[-1]) are not walls, meaning they will not retain water.
    If the list is empty return 0.
"""


def rain(walls):
    """
    Args:
        walls - is a list of non-negative integers.
    Returns:
        If the list is empty return 0.
    """
    n = len(walls)
    total_water = 0

    for i in range(1, n - 1):
        left = walls[i]
        for j in range(i):
            left = max(left, walls[j])
        right = walls[i]

        for j in range(i + 1, n):
            right = max(right, walls[j])

        total_water = total_water + (min(left, right) - walls[i])
    return total_water
