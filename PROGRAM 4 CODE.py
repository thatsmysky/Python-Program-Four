##ok so i'm gonna make 5 functions to draw things;
##circle, rectangle, python logo, and star, and then i make one up
##[probably my name].
##then all i need is a loop
##    to make the program ask if they have a picture they wanna draw,
##a loop inside that asking what picture,
##a try/except block to try to open the file
##    and run a warning if it doesnt open right.
##then the program should open the file,
##draw the picture,
##clear the screen,
##and ask if you want to draw something else

import turtle
not_integers = ('not_int')
def try_open(file):
    try:
        opening_file = open(file, 'r')
        return True
    except IOError:
        print("I'm sorry, that file cannot be opened, please try again.")
    except:
        print("Please try again")

def set_color():
    Line = line.split()
    end = len(Line)
    color = str(Line[1])
    turtle.color (color)

def draw_rectangle():
    Fline = line.split()
    if Fline[1] == 'not_int':
        print(Fline)
        print("I'm sorry, I cannot understand that integer")
        return
    if len(Fline) < 4:
        print(Fline)
        print("I'm sorry, I do not understand that value")
        return
    x = int(Fline[1])
    y = int(Fline[2])
    width = int(Fline[3])
    height = int(Fline[4])
    turtle.penup()
    turtle.setpos(x, y)
    turtle.setheading(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(width)
    turtle.setheading(-90)
    turtle.forward(height)
    turtle.setheading(180)
    turtle.forward(width)
    turtle.setheading(90)
    turtle.forward(height)
    turtle.end_fill()
            
def draw_circle(x, y, radius):
    Line = line.split()
    if Line[0] == 'color':
        return
    x = int(Line[1])
    y = int(Line[2])
    radius = int(Line[3])
    turtle.penup()
    turtle.setpos((x+radius),(y))
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    
    
def draw_line():
    Bits_of_Fline = line.split()
    x = int(Bits_of_Fline[1])
    y = int(Bits_of_Fline[2])
    angle = int(Bits_of_Fline[3])
    length = int(Bits_of_Fline[4])
    turtle.penup()
    turtle.setpos(x, y)
    turtle.pendown()
    turtle.setheading(angle)
    turtle.forward(length)



draw_a_file = "YES"
Open = True
while draw_a_file in ('YES', 'Y'):
    open_file = input("What file would you like to open? ")
    if open_file in ('quit', 'QUIT'):
        break
    try_open(open_file)
    F = open(open_file, 'r')
    for line in F:
        line = line.lower()
        if 'color' in line:
            set_color()        
        if 'rect' in line:
            draw_rectangle()
        if 'circle' in line:
            draw_circle(0,0,0)
        if 'line' in line:
            draw_line()
        if 'bigstar' in line:
            print("I'm sorry, that's not an understandable command.")
    turtle.done()
    draw_again = input("Do you have something else you would like to draw? ")
    draw_again = draw_again.upper()
    if draw_again in ('Y', 'YES'):
        turtle.reset()
        print('Excellent! Lets do this again!')
    else:
        print("Thank you for playing")
        break
