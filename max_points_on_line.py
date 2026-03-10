"""
Problem 1: Collinear Points
===========================
max_points_on_line(X, p) returns the maximum number of points in X
that fall on the same straight line containing p.

Input:  X - list of 2-tuples (x, y) representing points
        p - query point as 2-tuple (p_x, p_y)
Output: Integer: max # of points on any line through p

Expected time: O(n)
"""

import math


def max_points_on_line(X, p):
    """
    Group points by slope from p; return size of largest group + points at p.
    Uses GCD for exact slope representation (avoids floating-point errors).
    """
    # Edge case: empty set -> return 0
    if not X:
        return 0

    p_x, p_y = p
    slopes = {}   # Hash map: (slope_x, slope_y) -> count of points on that line
    at_p = 0     # Count of points exactly coinciding with p (on every line)
    max_count = 0  # Max points on any single line (excluding points at p)

    for x, y in X:
        # Edge case: point coincides with query point -> count separately
        if x == p_x and y == p_y:
            at_p += 1
            continue

        # Direction vector from p to (x, y)
        dx = x - p_x
        dy = y - p_y

        # Reduce to canonical fraction using GCD (avoids floating-point precision issues)
        g = math.gcd(abs(dx), abs(dy))
        slope_x = dx // g
        slope_y = dy // g

        # Normalize: points on opposite sides of p on same line -> same key
        # Rule: dx >= 0; if dx=0 then dy >= 0
        if slope_x < 0 or (slope_x == 0 and slope_y < 0):
            slope_x = -slope_x
            slope_y = -slope_y

        # Update count for this slope and track maximum
        slope = (slope_x, slope_y)
        slopes[slope] = slopes.get(slope, 0) + 1
        max_count = max(max_count, slopes[slope])

    # Points at p lie on every line; add to max count
    return max_count + at_p


if __name__ == "__main__":
    # Example from assignment: X and p=(5,5) -> 4 points on line with slope -1/2
    X = [(1, 1), (3, 1), (5, 2), (3, 6), (1, 7), (7, 4), (9, 3), (9, 9)]
    p = (5, 5)
    print(max_points_on_line(X, p))  # Expected: 4

    # Edge case: empty set
    print(max_points_on_line([], (0, 0)))  # Expected: 0

    # Edge case: all points at p (each counts as on every line)
    print(max_points_on_line([(1, 1), (1, 1)], (1, 1)))  # Expected: 2
