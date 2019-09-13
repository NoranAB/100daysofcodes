#task1
set = {1,3,5,7,8}
set.update ([4,8,12])
print(set)
set.remove(8)
print(set)
set.clear()
print(set)
#task2
dict = {
    "name": "pigeon",
    "type": "bird",
    "skin cover": "feathers"
}
i = dict.get("type")
print(i)
dict["skin cover"] = "none feathers"
print(dict)