import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}


with open("04_json_write.json", "w") as write_file:
    json.dump(data, write_file)