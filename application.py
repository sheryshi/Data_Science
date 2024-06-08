import requests

url = "https://imdb-top-100-movies.p.rapidapi.com/"

headers = {
	"x-rapidapi-key": "919d42aad8msh141809834802b44p1ca286jsne4d8c87fcfa7",
	"x-rapidapi-host": "imdb-top-100-movies.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())