# @Author: karserasl
# @Date:   07/12/2021
import pandas as pd
from numpy import ceil, floor

with open("input") as f:
    puzzle_inputs = pd.Series(map(int, f.read().strip().split(",")))

# First Puzzle
print(puzzle_inputs.sub(puzzle_inputs.median()).abs().sum())

# Second Puzzle
floor = puzzle_inputs.sub(floor(puzzle_inputs.mean())).abs().apply(lambda x: (1 + x) * x / 2).sum()
ceil = puzzle_inputs.sub(ceil(puzzle_inputs.mean())).abs().apply(lambda x: (1 + x) * x / 2).sum()
print(min(floor, ceil))
