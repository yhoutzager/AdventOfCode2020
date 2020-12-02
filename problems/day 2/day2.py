import time

if __name__ == '__main__':
	start = time.time()

	counter = 0
	with open("input", "r") as file:
		file_lines = file.readlines()

	for line in file_lines:
		split_line = line.split()
		min_max = [int(x) for x in split_line[0].split('-')]
		letter = split_line[1][0]
		password = split_line[2]
		if min_max[0] <= password.count(letter) <= min_max[1]:
			counter += 1

	answer = counter

	print('Answer part 1: {}'.format(answer))

	counter = 0
	for line in file_lines:
		split_line = line.split()
		min_max = [int(x)-1 for x in split_line[0].split('-')]
		letter = split_line[1][0]
		password = split_line[2]
		position_counter = 0
		for pos in min_max:
			if password[pos] == letter:
				position_counter += 1
		if position_counter == 1:
			counter += 1

	answer = counter

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
