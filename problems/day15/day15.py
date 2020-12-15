import time

if __name__ == '__main__':
	start = time.time()
	with open("input", "r") as file:
		array = [int(x) for x in file.readlines()[0].split(',')]

	last_index = {}
	for i, v in enumerate(array[:-1]):
		last_index[v] = i

	last = array[-1]
	# for i in range(len(array), 2020):
	for i in range(len(array), 30000000):
		new = 0
		if last in last_index:
			new = i - last_index[last] - 1
		last_index[last] = i - 1

		last = new

	answer = last

	print('Answer part 1: {}'.format(answer))

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
