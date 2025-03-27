import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
todos = json.loads(response.text)


with open("json_example.json", "w") as write_file:
    json.dump(todos[:20], write_file)