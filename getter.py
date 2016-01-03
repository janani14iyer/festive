import requests


response = requests.get("http://pokeapi.co/api/v1/pokemon/1/")
print(response)
