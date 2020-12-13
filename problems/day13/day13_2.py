import time

if __name__ == '__main__':
	start = time.time()

	with open("input", "r") as file:
		array = file.read().split()
		lines = array[1].split(',')
		bus_lines = {}
		for i in range(0, len(lines)):
			if lines[i] == 'x':
				continue
			bus_lines[int(i)] = int(lines[i])

	counter = 0
	answer = 0
	check_time = 0
	iteration_step = bus_lines[0]

	for i in bus_lines:
		if i == 0:
			continue

		while (check_time + i) % bus_lines[i] != 0:
			check_time += iteration_step
		iteration_step *= bus_lines[i]

	answer = check_time

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
