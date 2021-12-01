# @Author: karserasl
# @Date:   01/12/2021

with open("input", 'r') as f:
    input_puzzle = f.read().splitlines()

res = len([a for (a, b) in zip(input_puzzle, input_puzzle[1:]) if int(a) < int(b)])
print(res)
