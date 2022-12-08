from functools import reduce
li=[]
n=int(input("enter no of elements"))
for i in range(n):
    li.append(int(input("enter element")))
print(li)
li1=[i*3 for i in li]
print("new list")
print(li1)
print("sum of original list")
li2=reduce(lambda a,b:a+b,li)
print(li2)
print("sum of new list")
li3=reduce(lambda a,b:a+b,li1)
print(li3)