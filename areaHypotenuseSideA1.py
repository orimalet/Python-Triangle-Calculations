                 # Name: Orion Assefaw , Student Number: 201530497 , COMP517 Assignment 1                 # 

# mainMenu()- Gives User 4 options to choose from 
# Takes user input(string) by prompting user to type in their option
# Returns - a float of missing angle,hypotenuse length or triangle area; depending on user choice
def mainMenu(): 
    menu = input("Welcome!! Please select one of the following options :\n 1- To get a measure of a missing third angle of a triangle \n 2- To get the length of a hypotenuse of a right angled traingle calculated \n 3- To get the Area of a traingle calculated \n q- To exit the program")

# Option 1 Calculates the measure of the third internal angle and reports that to user
    if(menu=="1"): 
        angle1=float(input("Enter the degree measure of Angle 1 please : "))

        # Input error check
        if(angle1 >= 180 or angle1 <= 0): 
            print("You typed in an invalid interval angle, please retry by entering valid angle 1 measure")
            mainMenu()
        
        angle2=float(input("And now the degree measure of Angle 2 please : "))

        # Input error check
        if(angle2 >= 180 or angle2 <= 0):
            print("You typed in an invalid interval angle, please retry by entering valid angle 2 measure")
            mainMenu()

        missingangle= 180-(angle1+angle2)

        # Missing angle accuracy check
        if(missingangle >= 180 or missingangle <= 0):
            print("Oops Error, please retry by entering another valid combinations of angle measures")
            mainMenu()

        print("The degree measure of the 3 internal angles of the triangle is thus :",angle1,",",angle2,"and",missingangle)
        mainMenu() # Returns the User back to the Main Menu


# Option 2 Calculates the length of the hypotenuse of a right angled traingle and reports that to user
    elif(menu=="2"):
        side1=float(input("Enter the length (in cm) of the first side please : "))

        # Input error check
        if(side1 <= 0):
            print(" Input error!!!! Check side 1 length, a traingle can not have a side with length 0cm or less")
            mainMenu()

        side2=float(input("And now the length of the second side please : "))

        # Input error check
        if(side2 <= 0):
            print("Input error!!!! Check side 2 length, a traingle can not have a side with length 0cm or less")
            mainMenu()
        
        hypotenuse= (side1**2 +side2**2)**0.5
        print("The lengths of the 3 sides of the right angled traingle are thus :",side1,",",side2,"and",hypotenuse)
        mainMenu() # Returns the User back to the Main Menu


# Option 3 Calculates the Area of a traingle given the 3 sides entered by user and reports that to the user
    elif(menu=="3"):
        side1=float(input("Enter the length (in cm) of the first side please : "))

        # Input error check
        if(side1 <= 0):
            print("Input error!!!! Check side 1 length, a traingle can not have a side with length 0cm or less")
            mainMenu()

        side2=float(input("And now the length of the second side please : "))

        # Input error check
        if(side2 <= 0):
            print("Input error!!!! Check side 2 length, a traingle can not have a side with length 0cm or less")
            mainMenu()

        side3=float(input("And now the length of the third side please : "))

        # Input error check
        if(side3 <= 0):
            print("Input error!!!! Check side 3 length, a traingle can not have a side with length 0cm or less")
            mainMenu()

        # Triangle Inequality Theorem check
        if(((side1+side2) <= side3) | ((side1+side3) <= side2) | ((side2+side3) <= side1)):
            print("Oops ..the sides you inputed can not form a triangle (Sum of any 2 sides has to be greater than the 3rd side).")
            print("Please try again with another combination of sides")
            mainMenu()

        else:
            perimeter= (side1+side2+side3)/2
            area=((perimeter)*(perimeter-side1)*(perimeter-side2)*(perimeter-side3))**0.5
        print("The Area of the triangle is therefore :",area)
        mainMenu() # Returns the User back to the Main Menu


# This option lets the user exit the program
    elif(menu=="q"): 
        raise SystemExit


# If the user types in an invalid choice, they are notified and made to return back to the Main Menu
    else: 
        print("Invalid Option!! You have to select one of the 4 options given below")
        mainMenu() 

#Program Initiator
mainMenu()