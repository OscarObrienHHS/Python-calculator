# The variables in this list are used to verify that the user has inputted a shape that can be calculated and to identify which shape the user has inputted. 
# When the Line below runs it opens up a file where in future I plan to store the users inputs and the computers outputs.
validshapes = ["rectangle", "circle", "triangle", "parallelogram"]
f = open("storedcalculations", "x")

ans = True
while ans:
    print("""
    Hello, Please select what you would like to do
    1: Calculator
    2: View History
    3: Clear History
    """)
# Get the Shape the user wants to calculate and set it to lowercase.
shape = input('Please Select a following shape by typing it: Rectangle, Circle, Triangle, Parallelogram \n')
shape = shape.lower()

# Check If Shape is valid
while shape not in validshapes:
    shape = input('Sorry I dont recognise that shape, please select a following shape by typing it: Rectangle, Circle, Triangle, Parallelogram \n')

# If the Shape is a Rectangle this code will run and calculate the area and perimeter of the shape.
if shape == validshapes[0]:
    length = float(input('What is the length of your rectangle?\n'))
    width = float(input('What is the width of your rectangle?\n'))
    area = width * length
    perimeter = 2 * (length + width)
    print('The area of your {} is {} and your perimeter is {}'.format(shape, area, perimeter))
    
# If the Shape is a Rectangle this code will run and calculate the area and perimeter of the shape.
if shape == validshapes[1]:
    radius = float(input('What is the radius of your circle?\n'))
    pi = 3.14159265359
    area = pi * (radius * radius)
    perimeter = (pi * 2) * radius
    print('The area of your {} is {} and your perimeter is {}'.format(shape, area, perimeter))

# I havent created the code for calculating the dimensions of a triangle yet.
if shape == validshapes[2]: 
    print('The area of your {} is {} and your perimeter is {}'.format(shape, area, perimeter))

# If the shape is a Parallelogram this code will run and calculate the area and perimeter of the shape.
if shape == validshapes[3]:
    base = float(input('What is length of the base of your parallelogram? \n'))
    height = float(input('What is height of your parallelogram? \n'))
    side = float(input('What is the length of the side of your parallelogram?\n'))
    area = base * height
    perimeter = 2 * (side + base)
    output = print('The area of your {} is {} and your perimeter is {}'.format(shape, area, perimeter))

