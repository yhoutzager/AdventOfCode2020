import time

if __name__ == '__main__':
	start = time.time()
	masks_with_mem = []
	with open("input", "r") as file:
		# with open("testinput", "r") as file:
		array = file.read().split('\n')
		i = 0
		while i < len(array):
			split = array[i].split()
			mask_with_mem = split[2]
			mem_alloc = []
			i += 1
			while i < len(array):
				split = array[i].split()
				if split[0] == 'mask':
					break
				mem_alloc.append([int(split[0][4:-1]), int(split[2])])
				i += 1
			masks_with_mem.append([mask_with_mem, mem_alloc])

	answer = 0

	mask_length = len(masks_with_mem[0][0])
	memory_comp = {}
	for mask_with_mem in masks_with_mem:
		for mem in mask_with_mem[1]:
			memory_value = list(mask_with_mem[0])
			mem_string = format(mem[1], '0' + str(mask_length) + 'b')

			for i in range(0, mask_length):

				if memory_value[i] == 'X':
					memory_value[i] = mem_string[i]
			memory_comp[mem[0]] = int(''.join(memory_value), 2)

	answer = sum(memory_comp.values())

	print('Answer part 1: {}'.format(answer))

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
