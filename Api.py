import http.client

conn = http.client.HTTPSConnection("api-nba-v1.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "919d42aad8msh141809834802b44p1ca286jsne4d8c87fcfa7",
    'x-rapidapi-host': "api-nba-v1.p.rapidapi.com"
}

conn.request("GET", "/players/statistics?game=8133", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))