
#https://rickandmortyapi.com/documentation#get-all-characters
from api_requests.fetch_posts import fetch_data

posts = fetch_data("https://rickandmortyapi.com/api/character")


print(posts)