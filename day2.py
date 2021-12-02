import numpy as np

test_case = """
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

def parse(input):
  moves = [line.split(' ') for line in input.strip().splitlines()]
  return [[move[0], int(move[1])] for move in moves]

def first_task(moves):
  dy = np.array([0, 1])
  dx = np.array([1, 0])
  moves_map = {
      'up': -dy,
      'down': dy,
      'forward': dx
  }

  coords = np.array([0, 0])
  for direction, distance in moves:
    coords += distance * moves_map[direction]
  return coords[0] * coords[1]

def second_task(moves):
  """
  - down X increases your aim by X units.
  - up X decreases your aim by X units.
  - forward X does two things:
      - It increases your horizontal position by X units.
      - It increases your depth by your aim multiplied by X.
  """
  aim = 0
  coords = np.array([0, 0])
  for direction, distance in moves:
    if direction == 'forward':
      coords += np.array([distance, distance * aim])
    elif direction == 'down':
      aim += distance
    else:
      aim -= distance
  return coords[0] * coords[1]


def main():
  with open('data/day2.txt') as file:
    contents = file.read()
  moves = parse(contents)
  test_moves = parse(test_case)

  print(first_task(moves)) # 1698735
  assert first_task(test_moves) == 150

  print(second_task(moves)) # 1594785890
  assert second_task(test_moves) == 900

if __name__ == '__main__':
  main()
