my_list = []  

# Append the elements
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)


#insert 15 in second position
my_list.insert(1, 15)

# Extend my_list with [50, 60, 70]
my_list.extend([50, 60, 70])


# Remove the last element
my_list.pop()

# Sort my_list in ascending order
my_list.sort()

# Find the index of the value 30
index_of_30 = my_list.index(30)
print(index_of_30)


# Now my_list contains the elements
print(my_list)
