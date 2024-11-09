# Question : Create a class and find average and print the average using methods in python
class Student:
    def __init__(self,name,s1,s2,s3):
        self.name = name
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def average(self):
        return(self.s1 + self.s2 + self.s3)/3
    
    def display(self):
        print("Student Name :", self.name, " and ", "Average :",  self.average())

stud1=Student("Darpan",87,90,93)
stud1.display()
stud2=Student("Brijesh",85,79,91)
stud2.display()
