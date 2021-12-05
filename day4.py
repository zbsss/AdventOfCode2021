from collections import defaultdict

test_case = """
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

class Board:
  def __init__(self, nums):
    self.nums = nums # number: [row, col]
    self.rows = defaultdict(lambda: 5) # row: number of unmarked
    self.cols = defaultdict(lambda: 5) # row: number of unmarked
    self.unmarked = set(nums.keys())
    self.won = False

  def bingo(self, number):
    if number in self.unmarked:
      self.unmarked.remove(number)
      row, col = self.nums[number]
      if self.rows[row] == 1 or self.cols[col] == 1:
        self.won = True
        return True
      self.rows[row] -= 1
      self.cols[col] -= 1
    return False

  @staticmethod
  def parse_board(raw_board):
    nums = {}
    for row, line in enumerate(raw_board):
      for col, num in enumerate(line.replace('  ', ' ').split(' ')):
        nums[int(num)] = [row, col]
    return Board(nums)

def parse(input):
  lines = input.strip().splitlines()
  numbers = [int(num) for num in lines[0].split(',')]

  boards = []
  for i in range(2, len(lines), 6):
    boards.append([line.strip() for line in lines[i:i+5]])
  boards = [Board.parse_board(board) for board in boards]
  return numbers, boards


def first_task(inputs):
  numbers, boards = inputs

  for number in numbers:
    for board in boards:
      if board.bingo(number):
        return sum(board.unmarked) * number

def second_task(inputs):
  numbers, boards = inputs
  last_winner, last_number = None, None

  for number in numbers:
    for board in boards:
      if not board.won and board.bingo(number):
        last_winner = board
        last_number = number
  return sum(last_winner.unmarked) * last_number


def main():
  with open('data/day4.txt') as file:
    contents = file.read()

  print('---TASK 1---')
  print('RESULT:', first_task(parse(contents))) # 27027
  print('TEST RESULT:', first_task(parse(test_case)))
  assert first_task(parse(test_case)) == 4512

  print('---TASK 2---')
  print('RESULT:', second_task(parse(contents))) # 36975
  print('TEST RESULT:', second_task(parse(test_case)))
  assert second_task(parse(test_case)) == 1924


if __name__ == '__main__':
  main()
