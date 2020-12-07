import time


def process_line(line, bags):
	split_line = line.split()
	base_colour = ' '.join(split_line[:2])

	sub_colours_list = []
	i = 4
	while i < len(split_line):
		if split_line[i] == 'no':
			break
		sub_colours_list.append(' '.join(split_line[i + 1: i + 3]))
		i += 4

	bags[base_colour] = sub_colours_list

def check_bag_for(bag, target, bags):
	if len(bags[bag]) == 0:
		return False
	if target in bags[bag]:
		return True
	return any([check_bag_for(sub_bag, target, bags) for sub_bag in bags[bag]])

if __name__ == '__main__':
	start = time.time()

	bags = {}

	target = 'shiny gold'
	# with open("testinput", "r") as file:
	with open("input", "r") as file:
		[process_line(x, bags) for x in file.readlines()]

	answer = 0
	for bag in bags:
		if check_bag_for(bag, target, bags):
			answer += 1


	print('Answer part 1: {}'.format(answer))

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
