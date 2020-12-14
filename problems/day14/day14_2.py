import time


def all_addresses(loc_in):
	mem_locations = []
	to_process = [loc_in]
	while len(to_process) > 0:
		loc = to_process.pop(0)
		x_loc = loc.find('X')
		if x_loc == -1:
			mem_locations.append(int(loc, 2))
		else:
			to_process.append(loc[:x_loc] + '1' + loc[x_loc + 1:])
			to_process.append(loc[:x_loc] + '0' + loc[x_loc + 1:])
	return mem_locations


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
			mem_string = format(mem[1], '0' + str(mask_length) + 'b')

			memory_location = list(mask_with_mem[0])
			mem_location_string = format(mem[0], '0' + str(mask_length) + 'b')
			for i in range(0, mask_length):
				if memory_location[i] == '0':
					memory_location[i] = mem_location_string[i]
			x_count = memory_location.count('X')

			value = mem[1]
			for x in all_addresses(''.join(memory_location)):
				memory_comp[x] = value

	answer = sum(memory_comp.values())

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
