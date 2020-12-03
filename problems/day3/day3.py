import time
from math import floor

if __name__ == '__main__':
	start = time.time()
	with open("input", "r") as file:
		array = [line.strip() for line in file.readlines()]

	answer = 0

	print('{} {}'.format(len(array), len(array[0])))

	for y in range(1, len(array)):
		x = y * 3 % len(array[0])
		if array[y][x] == '#':
			answer += 1

	print('Answer part 1: {}'.format(answer))

	trees = {0.5: 0, 1: 0, 3: 0, 5: 0, 7: 0}

	for y in range(1, len(array)):
		for slope in range(1, 8, 2):
			x = y * slope % len(array[0])
			if array[y][x] == '#':
				trees[slope] += 1
		if y % 2 == 0:
			x = floor(y * 0.5) % len(array[0])
			if array[y][x] == '#':
				trees[0.5] += 1

	answer2 = 1
	for x in trees.values():
		answer2 *= x
	print('Answer part 2: {}'.format(answer2))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
