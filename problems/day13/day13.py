import time

if __name__ == '__main__':
	start = time.time()
	with open("input", "r") as file:
		array = file.read().split()
		start_time = int(array[0])
		bus_lines = [int(x) for x in array[1].split(',') if x != 'x']

	answer = 0

	check_time = start_time
	found = False
	first_line = 0
	while not found:
		for line in bus_lines:
			if check_time % line == 0:
				first_line = line
				found = True
				break
		check_time += 1

	answer = (check_time - start_time - 1) * first_line

	print('Answer part 1: {}'.format(answer))

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
