import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    # URL of the website to fetch data from
    url = "https://tardis.wiki/wiki/The_Chimes_of_Midnight_(audio_story)"


    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Access the content of the response
        print("Data fetched successfully:")
        soup = BeautifulSoup(response.text, 'html.parser')

        for item in soup.select('div.pi-item'): # a for loop that runs through at elements in the table
            label = item.select_one('h3.pi-data-label')
            #Doctor Data retrival
            if label and 'Doctor:' in label.text:
                values = item.select('div.pi-data-value a')
                doctor = [d.text for d in values]

        return(doctor)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

print(fetch_data("https://tardis.wiki/wiki/The_Chimes_of_Midnight_(audio_story)"))
# The above code fetches data from the specified URL and prints it.