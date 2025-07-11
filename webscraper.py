import requests
from bs4 import BeautifulSoup
import re

def clean_text(value):
    if isinstance(value, str):
        cleaned = re.sub(r'\[nb \d+\]', '', value)
        return [cleaned.strip()] if cleaned.strip() else []
    elif isinstance(value, list):
        return [re.sub(r'\[nb \d+\]', '', v).strip() for v in value if v.strip()]
    return []



def smart_capitalize(text):
    exceptions = {'the', 'of', 'for', 'and', 'a', 'an', 'in', 'on', 'at', 'to', 'with'}
    words = text.lower().split()
    result = []

    for i, word in enumerate(words):
        if i == 0 or word not in exceptions:
            result.append(word.capitalize())
        else:
            result.append(word)
    
    return ' '.join(result)

def doctorconverter(data):
	doctor_number_map = {
		'Fugitive Doctor': 'Fugitive Dr',
		'First Doctor': '1st Dr',
		'Second Doctor': '2nd Dr',
		'Third Doctor': '3rd Dr',
		'Fourth Doctor': '4th Dr',
		'Fifth Doctor': '5th Dr',
		'Sixth Doctor': '6th Dr',
		'Seventh Doctor': '7th Dr',
		'Eighth Doctor': '8th Dr',
		'War Doctor': 'War Dr',
		'Ninth Doctor': '9th Dr',
		'Tenth Doctor': '10th Dr',
		'Eleventh Doctor': '11th Dr',
		'Twelfth Doctor': '12th Dr',
		'Thirteenth Doctor': '13th Dr',
		'Fourteenth Doctor': '14th Dr',
		'Fifteenth Doctor': '15th Dr'
	}
	formatted_data = [doctor_number_map.get(d, d) for d in data]
	return formatted_data



def fetch_data(name):
	#######
	#add in media_type as an input for the function
	#######
	# if media_type == "audio":
	# 	media = "_(audio_story)"
	# elif media_type == "tv":
	# 	media = "_(TV_story)"
	# elif media_type == "novel":
	# 	media = "_(novel)"
	# else:
	# 	media = ""

	episode_name = smart_capitalize(name)
	episode_formatted = episode_name.replace(" ","_")

    #url = "https://tardis.wiki/wiki/" + episode_formatted + media

	url = "https://tardis.wiki/wiki/" + episode_formatted + "_(TV_story)"

	try:
		
		# Send a GET request to the website
		response = requests.get(url)
		response.raise_for_status()  # Raise an error for bad status codes

		# Access the content of the response
		soup = BeautifulSoup(response.text, 'html.parser')
		season = doctor = companions = featuring = enemy = writer = director = air_date =  setting = ''
		
		for item in soup.select('div.pi-item'): # a for loop that runs through at elements in the table
			label = item.select_one('h3.pi-data-label')

			value_element = item.select_one('div.pi-data-value')
			
			if not label or not value_element:
				continue

			label_text = label.text.strip()

			# Extract values
			values = [a.text.strip() for a in value_element.select('a')] or [value_element.text.strip()]

			if 'Doctor:' in label_text:
				doctor = clean_text(values)

			elif 'Companion' in label_text:
				companions = clean_text(values)

			elif 'Featuring' in label_text:
				featuring = clean_text(values)

			elif 'Main enemy' in label_text:
				enemy = clean_text(values)

			elif 'Main setting' in label_text:
				setting = clean_text(values)

			elif 'Writers' in label_text or 'Writer' in label_text:
				writer = clean_text(values)

			elif 'Director' in label_text:
				director = clean_text(values)

			elif 'Part of' in label_text:
				season = clean_text(values)

			elif 'Premiere broadcast' in label_text:
				air_date = clean_text(values)
		
		# Apply doctor converter
		#doctor = doctorconverter(doctor)
		#featuring = doctorconverter(featuring)


		if not any([season, doctor, companions, featuring, enemy,setting, writer, director,air_date]):
			raise KeyError("No valid data found on the page.")
		else:
			return [episode_name],season,doctor,companions,featuring,enemy,setting, writer,director,air_date

	except requests.exceptions.RequestException as e:
		#print(f"An error occurred: {e}")
		return ('N/A',)*10  # Return a default tuple
	
	except KeyError as e:
		print(f"Data missing: {e}")
		return ('N/A',)*10 
	