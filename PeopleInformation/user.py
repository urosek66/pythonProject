# import jason library
import json

# read file users.json and save  data of people in a variable content
with open("users.json", "r") as user_file:
    content = json.loads(user_file.read())

# for each person print out the following things(in this order): last name, first name, latitude and the catchphrase
    for line in content:
        name_split = line["name"].split()
        address = line["address"]["geo"]["lat"]
        catch_phrase = line["company"]["catchPhrase"]

        if line["id"] == 6:
            print(f"Last name: {name_split[2]}, First name: {name_split[1]}, Latitude: {address}, "
                  f"Company catch phrase: {catch_phrase}")
        else:
            print(f"Last name: {name_split[1]}, First name: {name_split[0]}, Latitude: {address}, "
                    f"Company catch phrase: {catch_phrase}")
