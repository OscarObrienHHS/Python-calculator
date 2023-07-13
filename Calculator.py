#setting up stuff for checking that the shape is valid
validshapes = ["rectangle", "circle", "triangle", "parallelogram"]
calculations = open("storedcalculations", "a+")
#Importing math for the square root (sqrt) in herons formula
import math

# Error Checker thingy majig
def getFloat(msg):
    try:
        f = float(input(msg))
        return f
    except ValueError:
        # This will run if the input is not a number
        print("You didnt enter a number >:(, Youre a horrible person")
        return getFloat(msg)

# Menu for the user to select what they want to do
ans = True
while ans:
    print("""
    Hello, Please select what you would like to do
    1: Calculator
    2: View History
    3: Clear History
    4: Exit program
    """)
    ans=input("What would you like to do? \n") 
    # if the user enters 1 the code below will run
    if ans=="1": 
        print("Calculator Opening") 
      # Get the Shape the user wants to calculate and set it to lowercase.
        shape = input('Please Select a following shape by typing it: Rectangle, Circle, Triangle, Parallelogram \n')
        shape = shape.lower()

        # Check If Shape is valid, if shape is not valid it will loop the code below.
        while shape not in validshapes:
            # Get the shape the user wants to calculate and set it to lowercase.
            shape = input('Sorry I dont recognise that shape, please select a following shape by typing it: Rectangle, Circle, Triangle, Parallelogram \n')
            shape = shape.lower()

        # If the Shape is a Rectangle this code will run.
        if shape == validshapes[0]:
            # Get the length and width of the rectangle.
            length = getFloat('What is the length of your rectangle?\n')
            width = getFloat('What is the width of your rectangle?\n')
            # Calculate the area and perimeter
            area = width * length
            perimeter = 2 * (length + width)
            # Print out answer to user
            print('The area of your {} is {} and your perimeter is {}'.format(shape, area, perimeter))
            # Write Information into the file
            calculations.write('shape: {}\n length: {}\n width: {}\n area: {}\n perimeter: {}\n\n'.format(shape, length, width, area, perimeter))
            calculations.flush()

        # If the Shape is a Circle this code will run.
        if shape == validshapes[1]:
            # Getting the radius of the Circle
            radius = getFloat('What is the radius of your circle?\n')
            # Setting pi variable
            pi = 3.14159265359
            # Calculating
            area = pi * (radius * radius)
            perimeter = (pi * 2) * radius
            # Printing out answer for user
            print('The area of your {} is {} and your perimeter is {}'.format(shape, area, perimeter))
            # Write Information into the file
            calculations.write('shape: {}\n radius: {}\n pi: {}\n area: {}\n perimeter: {}\n\n'.format(shape, radius, pi, area, perimeter))
            calculations.flush()
            
        # If the shape is a Triangle this code will run.
        if shape == validshapes[2]: 
            # A menu for the user to select their dimensions
            triangle_ans = True
            while triangle_ans:
                print("""
                Hello, Please select what dimesions you have?
                1: All sides (Herons formula)
                2: Base + Height
                """)
                triangle_ans=input("What would you like to do? \n") 
                # If they enter one this code will run.
                if triangle_ans=="1":
                    # Getting the three sides of the triangle
                    side1 = getFloat('What is the first side of your triangle?\n')
                    side2 = getFloat('What is the second side of your triangle?\n')
                    side3 = getFloat('What is the third side of your triangle?\n')
                    # Calculatiing the area and perimeter
                    perimeter = side1 + side2 + side3
                    s = perimeter / 2 
                    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
                    # Printing out the answer for the user
                    print('The area of your {} is {} and your perimeter is {}'.format(shape, area, perimeter))
                    # Writing Information into the calculations file
                    calculations.write('shape: {}\n side1: {}\n side2: {}\n side3: {}\n area: {}\n perimeter: {}\n\n'.format(shape, side1, side2, side3, area, perimeter))
                    calculations.flush()
                    # Ending the while loop
                    triangle_ans = False
                    # If they enter two this code will run.

                elif triangle_ans=="2":
                    # Getting the base and height
                    base = getFloat('What is the base of your triangle?\n')
                    height = getFloat('What is the height of your triangle?\n')
                    # Calculating the area
                    area = (height * base) / 2 
                    # Printing out the answer for the user
                    print('The area of your {} is {} and you cannot get a perimeter from only base and height'.format(shape, area))
                    # Writing information into the calculations file
                    calculations.write('shape: {}\n base: {}\n height: {}\n area: {}\n\n'.format(shape, base, height, area,))
                    calculations.flush()
                    # Ending while loop
                    triangle_ans = False

                # This code will run if the user doesnt enter either 1 or 2
                else:
                    print('\n Not valid choice try again')

        # If the shape is a Parallelogram this code will run and calculate the area and perimeter of the shape.
        if shape == validshapes[3]:
            # Getting the dimensions of a Parallelogram
            base = getFloat('What is length of the base of your parallelogram? \n')
            height = getFloat('What is height of your parallelogram? \n')
            side = getFloat('What is the length of the side of your parallelogram?\n')
            # Calculating the area and perimeter
            area = base * height
            perimeter = 2 * (side + base)
            # Printing the answer for the user
            print('The area of your {} is {} and your perimeter is {}'.format(shape, area, perimeter))
            # Writing information into the calculations file
            calculations.write('shape: {}\n base: {}\n side: {}\n area: {}\n perimeter: {}\n\n'.format(shape, base, side, height, perimeter))
            calculations.flush()

    # If the user enters 2 the code below will run.
    elif ans=="2":
        print("\nHistory Printing")
        # Set cursor to the top of the file and then read and print it out for the user
        calculations.seek(0)
        print(calculations.read())

    # If the user enters 3 the code below will run.
    elif ans=="3":
        print("\nHistory Cleared") 
        # This code will remove all of the text from the file.
        calculations.truncate(0)

    # If the user enters 4 the code below will run.
    elif ans=="4":
        # Printing out the history before the program closes
        print("\nHistory Printing")
        # Set cursor to the top of the file and then read and print it out for the user
        calculations.seek(0)
        print(calculations.read())
        # Printing a goodbye message and closing the calculations file
        print("\nGoodbye")
        calculations.close() 
    
    # This code will run if the user didnt enter a number between 1-4
    else:
        print("\nNot Valid Choice Try again") 


