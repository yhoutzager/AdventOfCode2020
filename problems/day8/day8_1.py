import time

if __name__ == '__main__':
	start = time.time()
	with open("input", "r") as file:
		array = [x.split() for x in file.readlines()]
		for x in array:
			temp = x[1]
			if temp[0] == '+':
				x[1] = ['+', temp[1:]]
			else:
				x[1] = ['-', temp[1:]]

	answer = 0

	i = 0
	already_used_index = []
	while i not in already_used_index:
		# print('{} {}'.format(i, answer))
		already_used_index.append(i)
		command = array[i][0]
		sign = array[i][1][0]
		number = int(array[i][1][1])
		if command == 'jmp':
			if sign == '+':
				i += number
			else:
				i -= number
		elif command == 'acc':
			i += 1
			if sign == '+':
				answer += number
			else:
				answer -= number
		else:
			i += 1

	print('Answer part 1: {}'.format(answer))

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
