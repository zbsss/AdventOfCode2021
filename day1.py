test_case = [
    199,
    200,
    208,
    210,
    200,
    207,
    240,
    269,
    260,
    263
]

def first_task(nums):
  count = 0
  for i, num in enumerate(nums[1:]):
    if num > nums[i]:
      count += 1
  return count


def second_task(nums):
  count = 0
  for i in range(3, len(nums)):
    if nums[i] > nums[i - 3]:
      count += 1
  return count


def main():
  with open('data/day1.txt') as file:
    lines = file.readlines()
  numbers = [int(line.strip()) for line in lines]

  print(first_task(numbers)) # 1288
  assert first_task(test_case) == 7

  print(second_task(numbers)) # 1311
  assert second_task(test_case) == 5

if __name__ == '__main__':
  main()
