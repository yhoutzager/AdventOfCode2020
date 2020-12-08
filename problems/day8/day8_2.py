import time


def jmp(i, number):
	return i + process_number(number)


def acc(i, acc, number):
	return i + 1, acc + process_number(number)


def nop(i):
	return i + 1


def process_number(number):
	if number[0] == '+':
		return int(number[1])
	return -int(number[1])


def success_with_replace(i, already_used_index, array):
	switched_first = False
	while i not in already_used_index:
		# print('{} {}'.format(i, answer))
		already_used_index.append(i)
		command = array[i][0]
		number = array[i][1]
		if not switched_first:
			if command == 'jmp':
				i = nop(i)
				switched_first = True
				continue
			elif command == 'nop':
				i = jmp(i, number)
				switched_first = True
				continue
		if command == 'jmp':
			i = jmp(i, number)
		elif command == 'acc':
			i += 1
		elif command == 'nop':
			i = nop(i)

		if i >= len(array):
			check_for_switch = False
			return True

	return False


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
	check_for_switch = True
	while i < len(array):
		# print('{} {}'.format(i, answer))
		temp = i
		command = array[i][0]
		number = array[i][1]
		if command == 'jmp':
			if check_for_switch and success_with_replace(i, already_used_index.copy(), array):
				check_for_switch = False
				print('switched jmp at {}'.format(i))
				i = nop(i)
			else:
				i = jmp(i, array[i][1])
		elif command == 'acc':
			i, answer = acc(i, answer, number)
		elif command == 'nop':
			if check_for_switch and success_with_replace(i, already_used_index.copy(), array):
				check_for_switch = False
				print('switched nop at {}'.format(i))
				i = jmp(i, array[i][1])
			else:
				i = nop(i)
		else:
			print('{} {}'.format(i, command))
			break

		already_used_index.append(temp)

		if i in already_used_index:
			print('{}'.format(already_used_index))
			break

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
