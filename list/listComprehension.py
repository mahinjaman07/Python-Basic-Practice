# newlist = [expression for item in iterable if condition == True]
list1 = ["apple", "banana", "cherry", 1, 2, 3];
list2 = [x for x in list1 if "lemon" not in list1];
print(list2)