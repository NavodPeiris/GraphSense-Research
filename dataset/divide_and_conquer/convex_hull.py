
from __future__ import annotations

from collections.abc import Iterable


class Point:

    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x:
            return self.y > other.y
        return False

    def __lt__(self, other):
        return not self > other

    def __ge__(self, other):
        if self.x > other.x:
            return True
        elif self.x == other.x:
            return self.y >= other.y
        return False

    def __le__(self, other):
        if self.x < other.x:
            return True
        elif self.x == other.x:
            return self.y <= other.y
        return False

    def __repr__(self):
        return f"({self.x}, {self.y})"

    def __hash__(self):
        return hash(self.x)


def _construct_points(
    list_of_tuples: list[Point] | list[list[float]] | Iterable[list[float]],
) -> list[Point]:

    points: list[Point] = []
    if list_of_tuples:
        for p in list_of_tuples:
            if isinstance(p, Point):
                points.append(p)
            else:
                try:
                    points.append(Point(p[0], p[1]))
                except (IndexError, TypeError):
                    print(
                        f"Ignoring deformed point {p}. All points"
                        " must have at least 2 coordinates."
                    )
    return points


def _validate_input(points: list[Point] | list[list[float]]) -> list[Point]:

    if not hasattr(points, "__iter__"):
        msg = f"Expecting an iterable object but got an non-iterable type {points}"
        raise ValueError(msg)

    if not points:
        msg = f"Expecting a list of points but got {points}"
        raise ValueError(msg)

    return _construct_points(points)


def _det(a: Point, b: Point, c: Point) -> float:

    det = (a.x * b.y + b.x * c.y + c.x * a.y) - (a.y * b.x + b.y * c.x + c.y * a.x)
    return det


def convex_hull_bf(points: list[Point]) -> list[Point]:

    points = sorted(_validate_input(points))
    n = len(points)
    convex_set = set()

    for i in range(n - 1):
        for j in range(i + 1, n):
            points_left_of_ij = points_right_of_ij = False
            ij_part_of_convex_hull = True
            for k in range(n):
                if k not in {i, j}:
                    det_k = _det(points[i], points[j], points[k])

                    if det_k > 0:
                        points_left_of_ij = True
                    elif det_k < 0:
                        points_right_of_ij = True
                    
                    
                    
                    
                    elif points[k] < points[i] or points[k] > points[j]:
                        ij_part_of_convex_hull = False
                        break

                if points_left_of_ij and points_right_of_ij:
                    ij_part_of_convex_hull = False
                    break

            if ij_part_of_convex_hull:
                convex_set.update([points[i], points[j]])

    return sorted(convex_set)


def convex_hull_recursive(points: list[Point]) -> list[Point]:
    points = sorted(_validate_input(points))
    n = len(points)

    
    
    
    
    

    
    
    
    
    
    

    left_most_point = points[0]
    right_most_point = points[n - 1]

    convex_set = {left_most_point, right_most_point}
    upper_hull = []
    lower_hull = []

    for i in range(1, n - 1):
        det = _det(left_most_point, right_most_point, points[i])

        if det > 0:
            upper_hull.append(points[i])
        elif det < 0:
            lower_hull.append(points[i])

    _construct_hull(upper_hull, left_most_point, right_most_point, convex_set)
    _construct_hull(lower_hull, right_most_point, left_most_point, convex_set)

    return sorted(convex_set)


def _construct_hull(
    points: list[Point], left: Point, right: Point, convex_set: set[Point]
) -> None:
    if points:
        extreme_point = None
        extreme_point_distance = float("-inf")
        candidate_points = []

        for p in points:
            det = _det(left, right, p)

            if det > 0:
                candidate_points.append(p)

                if det > extreme_point_distance:
                    extreme_point_distance = det
                    extreme_point = p

        if extreme_point:
            _construct_hull(candidate_points, left, extreme_point, convex_set)
            convex_set.add(extreme_point)
            _construct_hull(candidate_points, extreme_point, right, convex_set)


def convex_hull_melkman(points: list[Point]) -> list[Point]:
    points = sorted(_validate_input(points))
    n = len(points)

    convex_hull = points[:2]
    for i in range(2, n):
        det = _det(convex_hull[1], convex_hull[0], points[i])
        if det > 0:
            convex_hull.insert(0, points[i])
            break
        elif det < 0:
            convex_hull.append(points[i])
            break
        else:
            convex_hull[1] = points[i]
    i += 1

    for j in range(i, n):
        if (
            _det(convex_hull[0], convex_hull[-1], points[j]) > 0
            and _det(convex_hull[-1], convex_hull[0], points[1]) < 0
        ):
            
            continue

        convex_hull.insert(0, points[j])
        convex_hull.append(points[j])
        while _det(convex_hull[0], convex_hull[1], convex_hull[2]) >= 0:
            del convex_hull[1]
        while _det(convex_hull[-1], convex_hull[-2], convex_hull[-3]) <= 0:
            del convex_hull[-2]

    
    return sorted(convex_hull[1:] if len(convex_hull) > 3 else convex_hull)


def main():
    points = [
        (0, 3),
        (2, 2),
        (1, 1),
        (2, 1),
        (3, 0),
        (0, 0),
        (3, 3),
        (2, -1),
        (2, -4),
        (1, -3),
    ]
    
    
    results_bf = convex_hull_bf(points)

    results_recursive = convex_hull_recursive(points)
    assert results_bf == results_recursive

    results_melkman = convex_hull_melkman(points)
    assert results_bf == results_melkman

    print(results_bf)


if __name__ == "__main__":
    main()
