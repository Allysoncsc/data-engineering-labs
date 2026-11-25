import requests


def fetch_data(api_url):
    """
    Fetches posts from the given API URL.

    Args:
        api_url (str): The URL of the API endpoint to fetch posts from.

    Returns:
        list: A list of posts retrieved from the API.
    """
    try:
        response = requests.get(api_url)
        #response.raise_for_status()  # Raise an error for bad responses
        if response.status_code == 200:
            return response.json()  # Assuming the API returns JSON data
        else:
            print(f"Failed to fetch posts. Status code: {response.status_code}")    
        return response.json()  # Assuming the API returns JSON data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching posts: {e}")
        return []