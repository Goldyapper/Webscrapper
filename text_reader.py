def txt_reader(input_file):
	with open(input_file) as file:
		return [line.strip() for line in file]

