#List = are containers used to store multiple items in a single variable
#exa : ["apple", "banana", "cherry"]

mylist = ["Apple","hhhd",33,True,2.3]
            
print(mylist[3]) #True
print(mylist[0]) #Apple
print(mylist[-1]) #2.3
print(mylist[1:4]) #['hhhd', 33, True]
print(mylist[:3]) #['Apple', 'hhhd', 33]

mylist.append("Dude") # Add string in the end point
l1 = [1,2,3,45]
l1.reverse() #reverse the list
print(l1)

#Method 3:
l1.insert(2, "Dude") # Add string in the 2nd index
print(l1)
#method 4:
l1.pop(3) #pop the element at index 3
print(l1)
#method 5:

l1.remove("Dude")#Remove the element Dude from the list
print(l1)
# list is a mutabe data type but string are immutable data type
# mylist[0] = "Dude" # This will change the value of index