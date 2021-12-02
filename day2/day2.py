# @Author: karserasl
# @Date:   02/12/2021

# First Puzzle
depth = horizontal = 0
with open("input") as f:
    line_list = f.readlines()

for line in line_list:
    key, value = line.split()
    value = int(value)
    if key == 'down':
        depth += value
    elif key == 'up':
        depth -= value
    elif key == 'forward':
        horizontal += value

print(depth * horizontal)

# Second Puzzle
depth = horizontal = aim = 0
for line in line_list:
    key, value = line.split()
    value = int(value)
    if key == 'down':
        aim += value
    elif key == 'up':
        aim -= value
    elif key == 'forward':
        horizontal += value
        depth += aim * value

print(depth * horizontal)
