
from __future__ import annotations

from collections import deque
from enum import Enum
from math import atan2, degrees
from sys import maxsize




class Direction(Enum):
    left = 1
    straight = 2
    right = 3

    def __repr__(self):
        return f"{self.__class__.__name__}.{self.name}"


def angle_comparer(point: tuple[int, int], minx: int, miny: int) -> float:
    
    x, y = point
    return degrees(atan2(y - miny, x - minx))


def check_direction(
    starting: tuple[int, int], via: tuple[int, int], target: tuple[int, int]
) -> Direction:
    x0, y0 = starting
    x1, y1 = via
    x2, y2 = target
    via_angle = degrees(atan2(y1 - y0, x1 - x0))
    via_angle %= 360
    target_angle = degrees(atan2(y2 - y0, x2 - x0))
    target_angle %= 360
    
    
    
    
    
    
    
    if target_angle > via_angle:
        return Direction.left
    elif target_angle == via_angle:
        return Direction.straight
    else:
        return Direction.right


def graham_scan(points: list[tuple[int, int]]) -> list[tuple[int, int]]:

    if len(points) <= 2:
        
        raise ValueError("graham_scan: argument must contain more than 3 points.")
    if len(points) == 3:
        return points
    
    minidx = 0
    miny, minx = maxsize, maxsize
    for i, point in enumerate(points):
        x = point[0]
        y = point[1]
        if y < miny:
            miny = y
            minx = x
            minidx = i
        if y == miny and x < minx:
            minx = x
            minidx = i

    
    points.pop(minidx)

    sorted_points = sorted(points, key=lambda point: angle_comparer(point, minx, miny))
    
    
    
    sorted_points.insert(0, (minx, miny))

    stack: deque[tuple[int, int]] = deque()
    stack.append(sorted_points[0])
    stack.append(sorted_points[1])
    stack.append(sorted_points[2])
    
    
    current_direction = Direction.left

    for i in range(3, len(sorted_points)):
        while True:
            starting = stack[-2]
            via = stack[-1]
            target = sorted_points[i]
            next_direction = check_direction(starting, via, target)

            if next_direction == Direction.left:
                current_direction = Direction.left
                break
            if next_direction == Direction.straight:
                if current_direction == Direction.left:
                    
                    
                    
                    break
                elif current_direction == Direction.right:
                    
                    
                    stack.pop()
            if next_direction == Direction.right:
                stack.pop()
        stack.append(sorted_points[i])
    return list(stack)
