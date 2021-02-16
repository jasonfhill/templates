import json


with open('./configs/config.json') as json_file:
    data = json.load(json_file)
    print(f"The full JSON data is: {data}")

    print("Here are all the people though:")
    for person in data["people"]:
        print(person["name"])
