import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
a =  '{ "name":"Devin", "age":32, "city":"California"}'
# parse x:
y = json.loads(x)
b = json.loads(a)

# the result is a Python dictionary:
print(y["age"])
print(y["name"])
print(y["city"])


# the result is a Python dictionary:
print(b["age"])
print(b["name"])
print(b["city"])
