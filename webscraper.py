import requests

def fetch_data(url):
    # URL of the website to fetch data from
    url = "https://tardis.wiki/wiki/The_Chimes_of_Midnight_(audio_story)"

    try:
        # Send a GET request to the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes

        # Access the content of the response
        data = response.text
        print("Data fetched successfully:")
        return(data)

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

print(fetch_data("https://tardis.wiki/wiki/The_Chimes_of_Midnight_(audio_story)"))
# The above code fetches data from the specified URL and prints it.