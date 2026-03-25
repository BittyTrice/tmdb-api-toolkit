# Getting Started with TMDB API – A Beginner’s Guide

## 🎯 Objective
This project demonstrates how to make GET requests to the TMDB API, parse JSON responses, and build a simple movie search tool using Python. It’s designed as a beginner’s toolkit for learning API integration.

## 📖 Summary
The Movie Database (TMDB) is a free, community‑driven movie and TV database. Its API allows developers to search for movies, actors, ratings, and trending content. Learning TMDB helps beginners understand API integration, JSON parsing, and documentation — skills transferable to business APIs like payments or ERP systems.

## 🛠️ Requirements
- Python 3.x  
- PyCharm (or any IDE)  
- `requests` library (`pip install requests`)  
- TMDB API key (free from [themoviedb.org](https://www.themoviedb.org/))

## ⚙️ Setup Instructions
1. Install Python and PyCharm.  
2. Create a new project folder (`tmdb_project`).  
3. Install `requests` via terminal:
   ```bash
   pip install requests
   ```
4. Get a free API key from TMDB.
5. Create a file named tmdb.py in your project.
6. Paste the minimal example code (see below).
7. Replace "YOUR_API_KEY" with your actual TMDB key.
8. Run the script in PyCharm.

## 🐍 Minimal Working Example
```python
import requests

API_KEY = "YOUR_API_KEY"
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

```
## ✨ AI Prompts & Learning Reflections
- Prompt: *“Guide me on PyCharm part seriously”*  
  Reflection: Learned how to set up PyCharm step by step.  

- Prompt: *“But in this case how can I use this like in Postman to call”*  
  Reflection: Understood how Postman complements Python by showing raw JSON responses.  

- Prompt: *“Now give me the documentation”*  
  Reflection: AI provided a ready‑made Markdown template, making documentation easier.

## ⚠️ Common Errors & How to Resolve
- **Invalid API key** → Double‑check you copied it correctly.  
- **Empty results** → Movie name may be misspelled; try another query.  
- **Rate limits** → TMDB allows limited requests per second; slow down if needed.  
- **Environment errors** → Ensure `requests` is installed in the correct virtual environment.  
- **Git not recognized** → Install Git and add it to PATH before pushing to GitHub.  


## 📚 Reference Resources
- TMDB API Documentation (developer.themoviedb.org in Bing)  
- Python `requests` library documentation  
- Tutorials on GitHub basics and Markdown formatting

=======
4. Get a free API key from TMDB.
5. Create a file named tmdb_test.py in your project.
6. Run the script in PyCharm.
>>>>>>> 0fe6d8c5467d81ba10ff2468d10cd21ab4766323
