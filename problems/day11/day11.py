import copy
import time


def has_occupied_surrounding_seats(seats, x_pos, y_pos):
	for x in range(x_pos-1, x_pos+2):
		if x < 0 or x >= len(seats[0]):
			continue
		for y in range(y_pos-1, y_pos+2):
			if (y == y_pos and x == x_pos) or y < 0 or y >= len(seats):
				continue
			if seats[y][x] == '#':
				return True
	return False


def four_surrounding_occupied(seats, x_pos, y_pos):
	count = 0
	for x in range(x_pos-1, x_pos+2):
		if x < 0 or x >= len(seats[0]):
			continue
		for y in range(y_pos-1, y_pos+2):
			if (y == y_pos and x == x_pos) or y < 0 or y >= len(seats):
				continue
			if seats[y][x] == '#':
				count += 1
	return count >= 4

if __name__ == '__main__':
	start = time.time()
	with open("input", "r") as file:
		array = [list(x) for x in file.read().split()]
	# [print(x) for x in array]

	answer = 0
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
					if four_surrounding_occupied(array, x, y):
						new_array[y][x] = 'L'
						change_seat = True
		if not change_seat:
			array = new_array
			break
		array = new_array
		# print('step')
		# [print(''.join(x)) for x in array]

	for x in array:
		answer += x.count('#')

	print('Answer part 1: {}'.format(answer))

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
