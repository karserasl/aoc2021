# @Author: karserasl
# @Date:   06/12/2021


from collections import Counter

with open("input") as f:
    puzzle_inputs = Counter(map(int, f.read().strip().split(",")))

for i in range(256):
    puzzle_inputs[(i + 7) % 9] += puzzle_inputs[i % 9]
    if i + 1 in (80, 256):
        print(sum(puzzle_inputs.values()))
