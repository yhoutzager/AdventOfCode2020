import time


def process_line(line, bags):
	split_line = line.split()
	base_colour = ' '.join(split_line[:2])

	sub_colours_list = []
	i = 4
	while i < len(split_line):
		if split_line[i] == 'no':
			break
		sub_colours_list.append([split_line[i], ' '.join(split_line[i + 1: i + 3])])
		i += 4

	bags[base_colour] = sub_colours_list

def check_bag_for(bag, target, bags):
	if len(bags[bag]) == 0:
		return False
	if target in bags[bag]:
		return True
	return any([check_bag_for(sub_bag, target, bags) for sub_bag in bags[bag]])


def determine_number_of_sub_bags(target, bags):
	sum = 1

	for sub_bag in bags[target]:
		sum += int(sub_bag[0]) * determine_number_of_sub_bags(sub_bag[1], bags)

	return sum

if __name__ == '__main__':
	start = time.time()

	bags = {}

	target = 'shiny gold'
	# with open("testinput", "r") as file:
	# with open("testinput2", "r") as file:
	with open("input", "r") as file:
		[process_line(x, bags) for x in file.readlines()]

	# print(bags)

	answer = determine_number_of_sub_bags(target, bags) - 1

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
