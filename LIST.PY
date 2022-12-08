li=[]
n=int(input("Enter number of elements"))
for i in range(n):
    li.append(int(input()))
print(li)
while (1):
    choice=int(input("Enter\n1.maxmin\n2.insert\n3.delete\n4.search\n5.exit\n "))
    if (choice==1):
        print("Max element is "+str(max(li)))
        print("Min element is "+str(min(li)))

    if(choice==2):
        li.insert(int(input("enter positon : ")),int(input("enter element : ")))
        print(li)

    if(choice==3):
        li.remove(int(input("enter the elemnet to be deleted : ")))
        print(li)
        
    if(choice==4):
        try:
            pos=li.index(int(input("enter element to be searched : ")))
            print("positon of element is : "+str(pos+1))
        
        except:
            print("element not found")
    if(choice==5):
        break
        

