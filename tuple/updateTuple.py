myTuple = ("apple", "banana", "cherry", 1, 2, 3);

convertList = list(myTuple);

convertList[0] = "lemon";

myTuple = tuple(convertList);
print(myTuple);

# add tuple item

convertList.append("pynapple");

myTuple = tuple(convertList);

print(myTuple);

# remove

convertList.remove("banana");
myTuple = tuple(convertList);
print(myTuple);

# del tuple list / del korar por amra ar amader tuple list ke run korte parbo na karon del korle amader pra tuple list e remove hoye jay

# del myTuple;
# print(myTuple)