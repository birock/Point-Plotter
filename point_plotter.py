import turtle

turtle.setup(500,500)
turtle.pensize(3)
turtle.speed(20)

turtle.up()
turtle.goto(0,250)
turtle.down()
turtle.goto(0,-250)
turtle.up()
turtle.goto(-250,0)
turtle.down()
turtle.goto(250,0)
turtle.up()

turtle.pensize(1)

turtle.goto(-250,250)

position = -250
while position <= 250:
    turtle.down()
    turtle.goto(position,-250)
    turtle.up()
    position += 10
    turtle.goto(position,250)

turtle.goto(-250,250)
position = 250
while position >= -250:
    turtle.down()
    turtle.goto(250,position)
    turtle.up()
    position -= 10
    turtle.goto(-250,position)

turtle.speed(5)

print("Welcome to the point plotter!")
print()

number = 1
while True:
    
    if number == 1:
        color = input("What color would you like your " + str(number) + "st point to be? ")
    elif number == 2:
        color = input("What color would you like your " + str(number) + "nd point to be? ")
    elif number == 3:
        color = input("What color would you like your " + str(number) + "rd point to be? ")
    else:
        color = input("What color would you like your " + str(number) + "th point to be? ")

    try:
        turtle.color(color)
    except:
        print("Invalid color. Please try again.")
        print()
        continue

    turtle.color("black")
    
    number += 1

    print()

    x = float(input("Enter the x-coordinate of your point: "))
    y = float(input("Enter the y-coordinate of your point: "))

    print()

    print("Your point is now being plotted.")

    print()

    turtle.showturtle()
    turtle.up()
    turtle.goto(10*x,10*y)
    turtle.down()
    turtle.dot(None,color)
    turtle.up()
    turtle.hideturtle()

    repeat = input("Continue? (y or n): ")

    print()

    if repeat.lower() == "n" or repeat.lower() == "no":
        break
    else:
        continue

print("Program finished.")






    
