# Create a Rectangle class that takes the length and width as arguments in the constructor. 
# Then, create two methods: area() - to calculate and return the area of the rectangle. 
# perimeter() - to calculate and return the perimeter of the rectangle. 
# Finally, create a print_details() method to print the length, width, area, and perimeter of the rectangle.

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2*(self.length * self.width)
    
    def print_details(self):
        print("length : ",self.length)
        print("width : ",self.width)
        print("Area : ",self.area())
        print("Perimeter  : ",self.perimeter())


re1=Rectangle(5,3)
re1.print_details()