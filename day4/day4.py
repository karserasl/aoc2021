# @Author: karserasl
# @Date:   04/12/2021

with open("input") as f:
    draw_numbers = list(map(int, f.readline().split(',')))
    inputs = [int(i) for i in f.read().split() if i != '']

puzzles = [[inputs[x:x + 5] for x in range(0, len(inputs), 5)][j:j + 5] for j in range(0, len(inputs), 5)]


class Board:
    def __init__(self, puzzle):
        self.position = {}
        self.puzzle = puzzle
        self.bingo = {
            "row": [0, 0, 0, 0, 0],
            "col": [0, 0, 0, 0, 0],
        }
        self.create_board()

    def create_board(self):
        for i, r in enumerate(self.puzzle):
            for j, c in enumerate(r):
                self.position[c] = (i, j)

    def update_board(self, val):
        pos = self.position.pop(val, None)
        if pos:
            x, y = pos
            self.update_bingo(x, y)

    def update_bingo(self, x, y):
        self.bingo["row"][x] += 1
        self.bingo["col"][y] += 1

    def check_bingo(self):
        return 5 in self.bingo["row"] or 5 in self.bingo["col"]

    def calc_res(self):
        return sum(self.position.keys())

    def __eq__(self, other):
        return self.puzzle == other[0].puzzle


# First Puzzle
def first_puzzle():
    boards = []
    for p in puzzles:
        boards.append(Board(p))
    for n in draw_numbers:
        for b in boards:
            b.update_board(n)
            if b.check_bingo():
                return n * b.calc_res()


# Second Puzzle
def second_puzzle():
    boards = []
    for p in puzzles:
        boards.append(Board(p))
    winning_boards = []
    for n in draw_numbers:
        for b in boards:
            if b in winning_boards:
                continue
            b.update_board(n)
            if b.check_bingo():
                winning_boards.append((b, n))

    last_win, num = winning_boards[-1]
    return num * last_win.calc_res()


if __name__ == '__main__':
    print(first_puzzle())
    print(second_puzzle())
