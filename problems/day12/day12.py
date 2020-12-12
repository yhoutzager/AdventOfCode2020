import time

if __name__ == '__main__':
	start = time.time()
	with open("input", "r") as file:
		array = [[x[0], int(x[1:])] for x in file.readlines()]

	answer = 0
	position = [0, 0]
	directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]  # ['E', 'S', 'W', 'N']
	current_dir_index = 0

	for instruction in array:
		mag = instruction[1]
		if instruction[0] == 'F':
			position[0] += mag * directions[current_dir_index][0]
			position[1] += mag * directions[current_dir_index][1]
		elif instruction[0] == 'E':
			position[0] += mag
		elif instruction[0] == 'S':
			position[1] -= mag
		elif instruction[0] == 'W':
			position[0] -= mag
		elif instruction[0] == 'N':
			position[1] += mag
		elif instruction[0] == 'R':
			current_dir_index = (current_dir_index + mag // 90) % 4
		elif instruction[0] == 'L':
			current_dir_index = ((current_dir_index - mag // 90) + 4) % 4

	answer = abs(position[0]) + abs(position[1])
	print('Answer part 1: {}'.format(answer))

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
