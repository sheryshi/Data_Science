import requests

url = "https://fresh-linkedin-profile-data.p.rapidapi.com/search-decision-makers"

payload = {
	"company_ids": ["163640", "19080118"],
	"title_keywords": ["CEO", "Founder", "Owner"],
	"geo_codes": [103644278, 102299470],
	"limit": "25"
}
headers = {
	"x-rapidapi-key": "919d42aad8msh141809834802b44p1ca286jsne4d8c87fcfa7",
	"x-rapidapi-host": "fresh-linkedin-profile-data.p.rapidapi.com",
	"Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.json())