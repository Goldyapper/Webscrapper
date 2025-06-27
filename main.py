from webscraper import fetch_data


def txt_reader(input_file):
	with open(input_file) as file:
		return [line.strip() for line in file]


lines = txt_reader("input.txt")

for item in lines:
    print(fetch_data(item))

# The above code fetches data from the specified name and prints it.