import mymodule
import platform
import datetime
import json
import re
import camelcase

c = camelcase.CamelCase()

txt = "hello world"

print(c.hump(txt))

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x))


# use four indents to make it easier to read the result:
print(json.dumps(x, indent=4))
# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=(". ", " = ")))
# sort the result alphabetically by keys:
print(json.dumps(x, indent=4, sort_keys=True))



x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))

x = platform.system()
print(x)

x = dir(platform)
print(x)

mymodule.greeting("Viet")

a = mymodule.person1["age"]
print(a)