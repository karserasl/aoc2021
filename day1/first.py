# @Author: karserasl
# @Date:   01/12/2021

# First Puzzle
with open("input", 'r') as f:
    input_puzzle = f.read().splitlines()

res = len([a for (a, b) in zip(input_puzzle, input_puzzle[1:]) if int(a) < int(b)])
print(res)

# Second Puzzle
import pandas as pd

series = pd.Series(input_puzzle)
series = pd.to_numeric(series)
res2 = series[series.rolling(3).sum().diff().ge(1)].count()
print(res2)
