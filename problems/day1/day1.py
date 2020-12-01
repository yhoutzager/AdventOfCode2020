import time

if __name__ == '__main__':
	start = time.time()

	with open("input", "r") as file:
		array = [int(x) for x in file.readlines()]
	length = len(array)
	answer = 0
	try:
		for i in range(0, length):
			for j in range(i + 1, length):
				entry_sum = array[i] + array[j]
				if entry_sum == 2020:
					answer = array[i] * array[j]
					print('{} {}'.format(array[i], array[j]))
					raise StopIteration
	except StopIteration:
		pass

	print('Answer part 1: {}'.format(answer))

	try:
		for i in range(0, length):
			for j in range(i + 1, length):
				entry_sum = array[i] + array[j]
				if entry_sum >= 2020:
					continue
				for k in range(j + 1, length):
					total_sum = entry_sum + array[k]
					if total_sum == 2020:
						answer = array[i] * array[j] * array[k]
						print('{} {} {}'.format(array[i], array[j], array[k]))
						raise StopIteration
	except StopIteration:
		pass

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
