#python json2
import json
x = {
    "name": "json",
    "age": 30,
    "married": True,
    "divorced": False,
    "childern":("Anne", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model1": "ford edge", "mpg": 24.2}
    ]
}
#use four indents to make it easer to read the result:
print(json.dumps(x, indent=4))
#use . and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
#sort the result alphabletically by keys:
print(json.dumps(x, indent=4, sort_keys=True))