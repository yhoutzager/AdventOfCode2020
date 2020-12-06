import time

if __name__ == '__main__':
	start = time.time()
	with open("input", "r") as file:
		array = [''.join(x.split()) for x in file.read().split('\n\n')]
	with open("input", "r") as file:
		array2 = [x.split() for x in file.read().split('\n\n')]

	answer = 0

	for x in array:
		counter = {x[0]}
		counter.update(x)
		answer += len(counter)

	print('Answer part 1: {}'.format(answer))

	answer = 0

	for x in array2:
		counter = {}
		for letter in x[0]:
			counter[letter] = True
		for y in range(1, len(x)):
			new_counter = {}
			for letter in x[y]:
				if letter in counter:
					new_counter[letter] = True
			counter = new_counter
		answer += len(counter)

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
