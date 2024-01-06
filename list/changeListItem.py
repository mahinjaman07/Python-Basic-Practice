myList = ["a", "b", "c", 1, 2, 3];

# use indexing
print(myList)
myList[2] = "x";
print(myList);

# use range

myList[0: 3] = "x", "y", "z";
print(myList);

# use insert()

myList.insert(1, 100);
print(myList)