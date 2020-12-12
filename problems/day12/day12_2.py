import time

if __name__ == '__main__':
	start = time.time()
	with open("input", "r") as file:
		array = [[x[0], int(x[1:])] for x in file.readlines()]

	answer = 0
	position = [0, 0]
	waypoint_position = [10, 1]
	# directions = [[1, 0], [0, -1], [-1, 0], [0, 1]]  # ['E', 'S', 'W', 'N']
	current_dir_index = 0

	for instruction in array:
		mag = instruction[1]
		if instruction[0] == 'F':
			position[0] += mag * waypoint_position[0]
			position[1] += mag * waypoint_position[1]
		elif instruction[0] == 'E':
			waypoint_position[0] += mag
		elif instruction[0] == 'S':
			waypoint_position[1] -= mag
		elif instruction[0] == 'W':
			waypoint_position[0] -= mag
		elif instruction[0] == 'N':
			waypoint_position[1] += mag
		elif instruction[0] == 'R':
			mag //= 90
			for i in range(0, mag):
				temp_position = [0, 0]
				temp_position[0] = waypoint_position[1]
				temp_position[1] = - waypoint_position[0]
				waypoint_position = temp_position
		elif instruction[0] == 'L':
			mag //= 90
			for i in range(0, mag):
				temp_position = [0, 0]
				temp_position[0] = - waypoint_position[1]
				temp_position[1] = waypoint_position[0]
				waypoint_position = temp_position


	answer = abs(position[0]) + abs(position[1])
	print('Answer part 1: {}'.format(answer))

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
