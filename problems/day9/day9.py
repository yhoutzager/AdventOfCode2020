import time

if __name__ == '__main__':
	start = time.time()
	with open("input", "r") as file:
		array = [int(x) for x in file.readlines()]

	answer = 0
	answer_index = 0
	step_size = 25

	for i in range(step_size, len(array)):

		found_pair = False
		for j in range(i - step_size, i):
			for k in range(j + 1, i):
				if array[i] == array[j] + array[k]:
					found_pair = True
					break
			if found_pair:
				break

		if not found_pair:
			answer = array[i]
			answer_index = i
			break

	print('Answer part 1: {}'.format(answer))

	answer2 = 0
	found_sum = False
	min_index, max_index = 0, 0
	for i in range(0, answer_index):
		counter = answer
		for temp_index in range(i, answer_index):
			counter -= array[temp_index]
			if counter < 0:
				break
			if counter == 0:
				min_index = i
				max_index = temp_index
				found_sum = True
		if found_sum:
			break

	answer2 = min(array[min_index:max_index]) + max(array[min_index:max_index])

	print('Answer part 2: {}'.format(answer2))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
