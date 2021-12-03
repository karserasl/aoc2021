# @Author: karserasl
# @Date:   03/12/2021
import pandas as pd

with open("input") as f:
    input_puzzle = f.read().splitlines()

df = pd.DataFrame(input_puzzle)[0].str.split('', expand=True)
res = df.mode().apply(''.join, axis=1).values[0]

# First Puzzle
gamma = int(res, 2)
epsilon = int(''.join([str(1 - int(x)) for x in res]), 2)
print(gamma * epsilon)

# Second Puzzle
df = df.drop([0, 13], 1)
ox = df.copy()
co = df.copy()
res2 = {}
for c in df.columns:

    ox = ox.loc[ox[c] == ox[c].value_counts().idxmax()]
    if len(ox) == 1:
        res2['oxygen'] = ox
        continue

    if len(co) > 1:
        co = co.loc[~(co[c] == co[c].value_counts().idxmax())]
    else:
        res2['co2'] = co
        continue

oxygen = int(res2['oxygen'].apply(''.join, axis=1).values[0], 2)
co2 = int(res2['co2'].apply(''.join, axis=1).values[0], 2)

print(oxygen * co2)
