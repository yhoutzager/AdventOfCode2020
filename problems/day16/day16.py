import time


if __name__ == '__main__':
	start = time.time()
	with open("input", "r") as file:
	# with open("testinput", "r") as file:
		blocks = file.read().split('\n\n')
		ranges = []
		for line in blocks[0].split('\n'):
			ranges.append([int(x) for x in line.split(':')[1].split()[0].split('-')])
			ranges.append([int(x) for x in line.split(':')[1].split()[2].split('-')])

		nearby_tickets = []
		for line in blocks[2][16:].split():
			[nearby_tickets.append(int(x)) for x in line.split(',')]

	invalids = []
	for ticket in nearby_tickets:

		valid = False
		for valid_range in ranges:

			if valid_range[0] <= ticket and valid_range[1] >= ticket:
				valid = True
				break
		if not valid:
			invalids.append(ticket)

	answer = sum(invalids)

	print('Answer part 1: {}'.format(answer))

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))