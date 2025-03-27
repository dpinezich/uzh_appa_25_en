import json

with open("04_json_write.json", "r") as read_file:
    data = json.load(read_file)

print(data)
print(data['president']['species'])