# @Author: karserasl
# @Date:   05/12/2021

from collections import defaultdict
import re

with open("input") as f:
    lines = [list(map(int, re.findall("\d+", x))) for x in f.readlines()]


def ranges(a, b, c, d):
    if a == b:
        return [a] * (abs(c - d) + 1)
    if a > b:
        return range(a, b - 1, -1)
    return range(a, b + 1)


def is_horizontal_or_vertical(x1, y1, x2, y2):
    return x1 == x2 or y1 == y2


def points(x1, y1, x2, y2):
    return zip(ranges(x1, x2, y1, y2), ranges(y1, y2, x1, x2))


horizontal_or_vertical_overlaps = defaultdict(int)
diagonal_overlaps = defaultdict(int)
for line in lines:
    for point in points(*line):
        diagonal_overlaps[point] += 1
        horizontal_or_vertical_overlaps[point] += is_horizontal_or_vertical(*line)

print(sum(overlap > 1 for overlap in horizontal_or_vertical_overlaps.values()))
print(sum(overlap > 1 for overlap in diagonal_overlaps.values()))
