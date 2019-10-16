import json

#some JSON:
x = '{"name": "John", "age": 30, "city": "New York"}'

# parse x:
y = json.loads(x)

#the result is a Python dictionary:
print(y["age"])

import json# a Python object (dict):
x = {
    "name": "john",
    "age": 30,
    "city":"New York"
}
#convert into JSON:
y = json.dumps(x)
#the result is JSON strings:
print(y)

import json
print(json.dumps({"name": "Rayn", "age": 24}))
print(json.dumps(["bluperry", "Cherry"]))
print(json.dumps(("bluperry", "Cherry")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(32.44))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

import json
z = {
    "name": "Reem",
    "age": 27,
    "Married": True,
    "divorced": False,
    "childern": ("Ann", "Billy"),
    "pets": None,
    "Cars": [
        {"model1": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}
#convert into JSON
j = json.dumps(z)
#the result is a JSON string
print(j)