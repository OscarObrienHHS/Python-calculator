validshapes = ["rectangle", "circle", "triangle", "parallelogram"]

f = open("storedcalculations", "x")
shape = input('Hello, Please Select a following shape by typing it: Rectangle, Circle, Triangle, Parallelogram \n')
shape = shape.lower()

while shape not in validshapes:
    shape = input('Sorry I dont recognise that shape, please select a following shape by typing it: Rectangle, Circle, Triangle, Parallelogram \n')

if shape == validshapes[0]:
    length = float(input('What is the length of your rectangle?\n'))
    width = float(input('What is the width of your rectangle?\n'))
    area = width * length
    perimeter = 2 * (length + width)
    print('The area of your {} is {} and your perimeter is {}'.format(shape, area, perimeter))

if shape == validshapes[1]:
    radius = float(input('What is the radius of your circle?\n'))
    pi = 3.14159265359
    area = pi * (radius * radius)
    perimeter = (pi * 2) * radius
    print('The area of your {} is {} and your perimeter is {}'.format(shape, area, perimeter))
    
if shape == validshapes[2]:
    dimensions = int(input('What is the of your triangle? \n'))
    
    print('The area of your {} is {} and your perimeter is {}'.format(shape, area, perimeter))
    
if shape == validshapes[3]:
    base = float(input('What is length of the base of your parallelogram? \n'))
    height = float(input('What is height of your parallelogram? \n'))
    side = float(input('What is the length of the side of your parallelogram?\n'))
    area = base * height
    perimeter = 2 * (side + base)
    output = print('The area of your {} is {} and your perimeter is {}'.format(shape, area, perimeter))

