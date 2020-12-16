import time

if __name__ == '__main__':
	start = time.time()
	with open("input", "r") as file:
	# with open("testinput", "r") as file:
		blocks = file.read().split('\n\n')
		ranges = {}
		for line in blocks[0].split('\n'):
			range_1 = [int(x) for x in line.split(':')[1].split()[0].split('-')]
			range_2 = [int(x) for x in line.split(':')[1].split()[2].split('-')]
			ranges[line.split(':')[0]] = [range_1, range_2]

		nearby_ticket_lines = blocks[2][16:].split()
		nearby_tickets = [[int(y) for y in x.split(',')] for x in nearby_ticket_lines]

		my_tickets = []
		for line in blocks[1][13:].split():
			my_tickets = [int(x) for x in line.split(',')]

	valid_tickets = []
	for ticketList in nearby_tickets:
		is_valid = True
		for ticket in ticketList:

			valid = False
			for valid_ranges in ranges.values():
				for valid_range in valid_ranges:
					if valid_range[0] <= ticket and valid_range[1] >= ticket:
						valid = True
						break
				if valid:
					break
			if not valid:
				is_valid = False
				break
		if is_valid:
			valid_tickets.append(ticketList)

	positions = {}

	open_positions = list(range(0, len(ranges)))
	possible_options = [x for x in ranges]

	valid_tickets = list(zip(*valid_tickets))

	t = 0
	while True:
		pos = open_positions[t]
		valid_options = []
		for option in possible_options:
			valid = True
			for j in valid_tickets[pos]:
				range_valid = False
				for min_max in ranges[option]:
					if min_max[0] <= j <= min_max[1]:
						range_valid = True
						break
				if not range_valid:
					valid = False
					break
			if valid:
				valid_options.append(option)
		if len(valid_options) == 1:
			positions[pos] = valid_options[0]
			possible_options.remove(valid_options[0])
			open_positions.remove(pos)
			t = 0
		else:
			t += 1

		if len(open_positions) == 0:
			break

	answer = 1
	for x in positions:
		if positions[x].startswith('departure'):
			answer *= my_tickets[x]

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
