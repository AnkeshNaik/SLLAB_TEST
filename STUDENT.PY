class Student:
    def __init__(self):
        self.name=input("enter name")
        self.age=(input("enter age"))
        self.marks=[]
    def accept(self):
        for i in range(3):
            self.marks.append(input("enter marks of each subject"))
    def display(self):
        print("name; "+self.name)
        print("Age: "+self.age)
        print("Three subject marks are:")
        print(self.marks)

print("Student 1:")
s=Student()
s.accept()

print("Student 2:")
s1=Student()
s1.accept()

print("\nStudent 1")
s.display()
print("\nStudent 2")
s1.display()