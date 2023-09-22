# # 7. Write a python program to create the json from dictionary 

import json

# Data to be written
dictionary = {
	"name": "sathiyajith",
	"rollno": 56,
	"cgpa": 8.6,
	"phonenumber": "9976770500"
}

# Serializing json
json_object = json.dumps(dictionary, indent=4)

# Writing to sample.json
with open("sample.json", "w") as outfile:
	outfile.write(json_object)


# Opening JSON file
with open('sample.json', 'r') as openfile:

	# Reading from json file
	json_object = json.load(openfile)

print(json_object)
print(type(json_object))