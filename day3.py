test_case = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

def parse(input):
  return input.strip().splitlines()

def first_task(inputs):
  size = len(inputs[0])
  counts = [0] * size
  for num in inputs:
    for i, bit in enumerate(num):
      if bit == '1':
        counts[i] += 1
  gamma = int(''.join(['1' if count >= len(inputs) // 2
                else '0' for count in counts]), base=2)
  epsilon = gamma ^ (2 ** size - 1)
  return epsilon * gamma

class Node:
  def __init__(self, zero = None, one = None, count=0):
    self.count = count
    self.children = {'0': zero, '1': one}

  def __getitem__(self, idx):
    return self.children[idx]
  
  def __setitem__(self, idx, item):
    self.children[idx] = item

def second_task(inputs):
  root = Node()
  
  def insert(number):
    node = root
    for bit in number:
      if not node[bit]:
        node[bit] =  Node()
      node[bit].count += 1
      node = node[bit]

  def get_result(a, b):
    node = root
    result = ''
    while node['0'] or node['1']:
      try:
        if node['0'].count > node['1'].count:
          node = node[a]
          result += a
        else:
          node = node[b]
          result += b
      except:
        if node['0']:
          node = node['0']
          result += '0'
        elif node['1']:
          node = node['1']
          result += '1'
    return result

  for number in inputs:
    insert(number)
  
  oxygen = int(get_result('0', '1'), 2)
  co2 = int(get_result('1', '0'), 2)
  return co2 * oxygen

def main():
  with open('data/day3.txt') as file:
    contents = file.read()
  inputs = parse(contents)
  test_inputs = parse(test_case)

  print('---TASK 1---')
  print('RESULT:', first_task(inputs)) # 3912944
  print('TEST RESULT:', first_task(test_inputs))
  assert first_task(test_inputs) == 198

  print('---TASK 2---')
  print('RESULT:', second_task(inputs)) # 4996233
  print('TEST RESULT:', second_task(test_inputs))
  assert second_task(test_inputs) == 230


if __name__ == '__main__':
  main()
