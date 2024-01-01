import requests
import os
import json
from dotenv import load_dotenv

# Function to retrieve a dictionary of currency codes and names from an API
def get_currencies():
    # Load environment variables from a file named ".env"
    load_dotenv()

    # Get the API key from environment variables
    key = os.getenv("API_KEY")

    # Define the URL for retrieving currency data
    url = f"https://openexchangerates.org/api/currencies.json?prettyprint=false&show_alternative=true&show_inactive=false&app_id={key}"

    # Define headers for the HTTP request
    headers = {"accept": "application/json"}

    # Make an HTTP GET request to the API
    response = requests.get(url, headers=headers)

    # Initialize an empty dictionary to store currency data
    data = {}

    # Check if the API request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response into a Python dictionary
        data = json.loads(response.text)
    else:
        # Display an error message if the API request fails
        print(f"Error: {response.status_code}")

    # Return the dictionary containing currency data
    return data

# Entry point for the script
if __name__ == '__main__':
    # Call the get_currencies function when the script is executed
    get_currencies()
