import time

def is_valid(array_to_check):
	for i in range(1, len(array_to_check)):
		if array_to_check[i] - array_to_check[i - 1] > 3:
			return False
	return True

def check_perm(sub_array):
	print(sub_array)
	if not is_valid(sub_array):
		return 1

	if len(sub_array) == 1:
		return 1
	sum = 1
	for i in range(1, len(sub_array) - 1):
		copy_arr = sub_array.copy()
		del copy_arr[i]
		sum += check_perm(copy_arr)
	# print(sub_array, sum)
	return sum


if __name__ == '__main__':
	start = time.time()
	with open("testinput2", "r") as file:
		array = [int(x) for x in file.readlines()]

	array.append(0)
	array.sort()
	# print(array)
	answer = 0
	diff_one = 0
	diff_three = 1

	for index in range(1, len(array)):
		diff = array[index] - array[index - 1]
		if diff > 3:
			break
		elif diff == 3:
			diff_three += 1
		elif diff == 1:
			diff_one += 1

	answer = diff_one * diff_three

	print('Answer part 1: {}'.format(answer))


	answer = 1
	print(array)

	index = 0
	while index < len(array) - 1:
		begin_sub_index = index
		end_sub_index = 0

		# find sub section
		for j in range(index + 1, len(array)):
			if array[j] - array[j - 1] == 3 or j == len(array) - 1:
				end_sub_index = j
				break
			elif array[j] - array[j-1] == 2 and array[j-1] - array[j-2] == 2:
				end_sub_index = j - 1
				break
			elif j == len(array):
				end_sub_index = len(array)

		# calculate subsection
		answer *= check_perm(array[begin_sub_index:end_sub_index])

		# set index to after subsection
		print(end_sub_index, answer)
		index = end_sub_index

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
