import re
import time


def split_on_empty_lines(s):
	# greedily match 2 or more new-lines
	blank_line_regex = r"(?:\r?\n){2,}"

	return re.split(blank_line_regex, s.strip())


def check_birth_year(year):
	if not year.isdigit():
		return False
	return 1920 <= int(year) <= 2002


def check_issue_year(year):
	if not year.isdigit():
		return False
	return 2010 <= int(year) <= 2020


def check_expiration_year(year):
	if not year.isdigit():
		return False
	return 2020 <= int(year) <= 2030


def check_height(height):
	temp = re.compile("([0-9]+)([a-zA-Z]+)")
	temp2 = temp.match(height)
	if not temp2:
		return False
	split = temp2.groups()
	if len(split) != 2:
		return False
	if split[1] == 'cm':
		return 150 <= int(split[0]) <= 193
	elif split[1] == 'in':
		return 59 <= int(split[0]) <= 76
	else:
		return False


def check_hair_color(hcl):
	if len(hcl) != 7 or hcl[0] != '#':
		return False
	pattern = re.compile('#[0-9a-z]')
	return pattern.match(hcl)


def check_eye_color(ecl):
	allowed = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	return ecl in allowed


def check_passport_id(pid):
	if len(pid) != 9:
		return False
	pattern = re.compile('[0-9]')
	return pattern.match(pid)

def is_false():
	return False

def check_field_is_valid(pass_field):
	split = pass_field.split(':')
	if len(split) != 2:
		return False

	switcher = {
		'byr': check_birth_year,
		'iyr': check_issue_year,
		'eyr': check_expiration_year,
		'hgt': check_height,
		'hcl': check_hair_color,
		'ecl': check_eye_color,
		'pid': check_passport_id,
	}

	func = switcher.get(split[0], lambda: False)
	return func(split[1])

if __name__ == '__main__':
	start = time.time()
	with open("input", "r") as file:
		passports = split_on_empty_lines(file.read())

	answer = 0

	req_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # 'cid',

	for passport in passports:
		pass_fields = passport.split()

		has_all_fields = True
		for req_field in req_fields:
			found_req_field = False
			for pass_field in pass_fields:
				if pass_field.split(':')[0] == req_field:
					found_req_field = True
					break
			if not found_req_field:
				has_all_fields = False
				break
		if has_all_fields:
			answer += 1

	print('Answer part 1: {}'.format(answer))

	answer2 = 0
	for passport in passports:
		pass_fields = passport.split()

		has_all_fields = True
		for req_field in req_fields:
			found_req_field = False
			for pass_field in pass_fields:
				if pass_field.split(':')[0] == req_field and check_field_is_valid(pass_field):
					found_req_field = True
					break
			if not found_req_field:
				has_all_fields = False
				break
		if has_all_fields:
			answer2 += 1

	print('Answer part 2: {}'.format(answer2))

	end = time.time()
	print('Time: {:.3f}ms'.format(end - start))
