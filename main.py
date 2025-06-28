from webscraper import fetch_data
from database_adder import database_adder
from text_reader import txt_reader


lines = txt_reader("input.txt")

#print(fetch_data("rose"))
#database_adder(fetch_data("rose"))
for item in lines:
    database_adder(fetch_data(item))
    print("Inserting data...")

print("DB insertation done")

#########################
# test on whole season
# add in a seasons? maybe do it manually
# add more stories to txt
# run for all stories
#########################