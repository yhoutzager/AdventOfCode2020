import time

if __name__ == '__main__':
	start = time.time()
	# with open("input", "r") as file:
	with open("testinput", "r") as file:
		array = file.read().split()

	answer = 0

	print('Answer part 1: {}'.format(answer))

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
