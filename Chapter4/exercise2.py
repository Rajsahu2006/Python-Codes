# mylist = ()
# l1 = list(mylist)
# l1.insert(0,"Orange")
# l1.insert(1,"Apple")
# l1.insert(2,"Cherry")
# l1.insert(3,"Mango")
# l1.insert(4,"Banana")
# l1.insert(5,"Grapes")
# l1.insert(6,"Lemon")
# print(l1)

#problem2
marks =[]

M1 = input("Enter your physics Marks:")
marks.append(M1)
M2 = input("Enter your chemistry Marks:")
marks.append(M2)
M3 = input("Enter your Maths Marks:")
marks.append(M3)
M4 = input("Enter your Hindi Marks:")
marks.append(M4)
M5 = input("Enter your English Marks:")
marks.append(M5)

marks.sort()

print(marks)

#problem 3
l = [2,3,455,6,5,4]

print(sum(l))