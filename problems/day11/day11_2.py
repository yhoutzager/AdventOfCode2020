import copy
import time


def has_occupied_surrounding_seats(seats, x_pos, y_pos):
	for x in [-1, 0, 1]:
		for y in [-1, 0, 1]:
			if x == 0 and y == 0:
				continue
			if occupied_in_direction(seats, x_pos, y_pos, x, y):
				return True
	return False
	# for x in range(x_pos - 1, x_pos + 2):
	# 	if x < 0 or x >= len(seats[0]):
	# 		continue
	# 	for y in range(y_pos - 1, y_pos + 2):
	# 		if (y == y_pos and x == x_pos) or y < 0 or y >= len(seats):
	# 			continue
	# 		if seats[y][x] == '#':
	# 			return True
	# return False


def five_occupied_in_sight(seats, x_pos, y_pos):
	count = 0
	for x in [-1, 0, 1]:
		for y in [-1, 0, 1]:
			if x == 0 and y == 0:
				continue
			if occupied_in_direction(seats, x_pos, y_pos, x, y):
				count += 1
	return count >= 5


def occupied_in_direction(seats, x_pos, y_pos, x, y):
	while True:
		x_pos += x
		y_pos += y
		if x_pos < 0 or x_pos >= len(seats[0]):
			return False
		if y_pos < 0 or y_pos >= len(seats):
			return False
		if seats[y_pos][x_pos] == '#':
			return True
		if seats[y_pos][x_pos] == 'L':
			return False


if __name__ == '__main__':
	start = time.time()
	with open("input", "r") as file:
		array = [list(x) for x in file.read().split()]

	while True:
		new_array = copy.deepcopy(array)
		change_seat = False
		for y in range(0, len(array)):
			for x in range(0, len(array[0])):
				if array[y][x] == '.':
					continue
				elif array[y][x] == 'L':
					if not has_occupied_surrounding_seats(array, x, y):
						new_array[y][x] = '#'
						change_seat = True
				elif array[y][x] == '#':
					if five_occupied_in_sight(array, x, y):
						new_array[y][x] = 'L'
						change_seat = True
		if not change_seat:
			array = new_array
			break
		array = new_array
		# print('step')
		# [print(''.join(x)) for x in array]

	answer = 0

	for x in array:
		answer += x.count('#')

	print('Answer part 1: {}'.format(answer))

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
