import requests

API_KEY = "15eea0ea075bbe4af32ba6be8fff0acb"
BASE_URL = "https://api.themoviedb.org/3"

movie_name = input("Enter a movie name: ")

url = f"{BASE_URL}/search/movie?api_key={API_KEY}&query={movie_name}"
response = requests.get(url)
data = response.json()

if data["results"]:
    movie = data["results"][0]
    print("🎬 Title:", movie["title"])
    print("📅 Release Date:", movie["release_date"])
    print("⭐ Rating:", movie["vote_average"])
    print("📝 Overview:", movie["overview"])
else:
    print("No results found.")
