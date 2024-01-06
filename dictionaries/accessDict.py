person = {
    "name": "Mahin Jaman",
    "address": "Dhaka, Bangladesh",
    "age": 19
};


# access dict item use key name
name = person["name"];
print(name);

# access key in dict

keys = person.keys();
print(keys);

# access value in dict
value = person.values();
print(value);

ever = person.items();
print(ever);

# use get() method

age = person.get("age");
print(age);