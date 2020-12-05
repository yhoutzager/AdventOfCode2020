import time


def determine_seat_id(seat):
	row_id = determine_bin_rep(seat[:7].replace('F', '0').replace('B', '1'))
	column_id = determine_bin_rep(seat[-7:].replace('L', '0').replace('R', '1'))
	return row_id * 8 + column_id


def determine_bin_rep(row):
	rep = 0
	for i in range(0, len(row)):
		if row[-1 - i] == '1':
			rep += 2 ** i
	return rep


if __name__ == '__main__':
	start = time.time()
	with open("input", "r") as file:
		array = file.read().split()

	answer = 0

	for seat in array:
		seat_id = determine_seat_id(seat)
		if seat_id > answer:
			answer = seat_id

	print('Answer part 1: {}'.format(answer))

	seats = [determine_seat_id(seat) for seat in array]
	seats.sort()
	for i in range(1, len(seats)):
		if seats[i] - seats[i - 1] != 1:
			answer = seats[i] - 1

	print('Answer part 2: {}'.format(answer))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
