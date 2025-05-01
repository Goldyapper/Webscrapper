import requests
from bs4 import BeautifulSoup
import re

def fetch_data(url):
    # URL of the website to fetch data from
    url = "https://tardis.wiki/wiki/Rosa_(TV_story)"


    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Access the content of the response
        soup = BeautifulSoup(response.text, 'html.parser')

        for item in soup.select('div.pi-item'): # a for loop that runs through at elements in the table
            label = item.select_one('h3.pi-data-label')

            #Parts Data retrival
            if label and 'Number of parts:' in label.text:
                value = item.select_one('div.pi-data-value')
                if value:
                    parts = value.text.strip()
            
            #Doctor Data retrival
            if label and 'Doctor:' in label.text:
                values = item.select('div.pi-data-value a')
                doctor = [d.text for d in values]
            
            #companion retrival    
            if label and 'Companion(s):' in label.text:
                values = item.select('div.pi-data-value a')
                companions = [c.text for c in values]
            
            #Featuring retrival    
            if label and 'Featuring' in label.text:
                values = item.select('div.pi-data-value a')
                featuring = [f.text for f in values]

            #Enemy retrival
            if label and 'Main enemy' in label.text:
                values = item.select('div.pi-data-value a')
                enemy = [e.text for e in values]

            #Writer Retrival
            if label and 'Writers' in label.text:
                values = item.select('div.pi-data-value a')
                writer = [w.text for w in values]

            #Director Retrival
            if label and 'Director' in label.text:
                values = item.select('div.pi-data-value a')
                director = [d.text for d in values]
        
        return(parts,doctor,companions,featuring,enemy,writer,director)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

print(fetch_data("https://tardis.wiki/wiki/The_Chimes_of_Midnight_(audio_story)"))
# The above code fetches data from the specified URL and prints it.