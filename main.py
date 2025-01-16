#API Calling ( use " pip install requests " to install requests and be able to import, else it would give a NOTFOUND Error

import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
#       print("Data retrieved !")
        pokemon_data = response.json()
        return pokemon_data

    else:
        print(f"Error N°{response.status_code}, Couldn't retrieve data")


pokemon_name = "pikachu"
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"name: {pokemon_info["name"].capitalize()}")
    print(f"id: {pokemon_info["id"]}")
    print(f"height: {pokemon_info["height"]} cm")
    print(f"weight: {pokemon_info["weight"]} kg")
