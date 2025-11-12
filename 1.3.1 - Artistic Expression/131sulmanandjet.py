import turtle as turt

wn = turt.Screen()
score = 0


letter_closed = "closed_letter.gif"
wn.addshape(letter_closed)
letter_open = "openletter.gif"
wn.addshape(letter_open)
letter_turtle = turt.Turtle(shape=letter_closed)  
letter_turtle.penup()
letter_turtle.goto(0, 0)


IraqWarLetter = turt.Turtle()
IraqWarLetter.hideturtle()


afghanistanWarLetter = turt.Turtle()
afghanistanWarLetter.hideturtle()


VietnamWarLetter = turt.Turtle()
VietnamWarLetter.hideturtle()


def change_letter(x, y):
        
        letter_turtle.clear()
        letter_turtle.shape(letter_open)

   

    
        afghanistanWarLetter.penup()
        afghanistanWarLetter.goto(-150,200)
        afghanistanWarLetter.color("black")
        afghanistanWarLetter.write("Afghanistan War 2001-2014", align='center', font=('Arial', 20, 'normal'))


    #button for afghanistan war letter
        afghanistanCircle = turt.Turtle()   
        afghanistanCircle.shape("circle")
        afghanistanCircle.color("grey")
        afghanistanCircle.penup()
        afghanistanCircle.goto(-295, 212)
        afghanistanCircle.onclick(afganistan_letter)

        VietnamWarLetter.penup()
        VietnamWarLetter.goto(-150,175)
        VietnamWarLetter.color("black")
        VietnamWarLetter.write("Vietnam War 1955-1975", align='center', font=('Arial', 20, 'normal'))

    #button for vietnam war letter
        vietnamCircle = turt.Turtle()   
        vietnamCircle.shape("circle")
        vietnamCircle.color("pink")
        vietnamCircle.penup()
        vietnamCircle.goto(-295, 187)
        vietnamCircle.onclick(vietnamButton)

    
        IraqWarLetter.penup()
        IraqWarLetter.goto(-150, 145)
        IraqWarLetter.color("black")
        IraqWarLetter.write("Iraq War Letter 2003-2011", align='center', font=('Arial', 20, 'normal'))

    #button for iraq war letter
        iraqCircle = turt.Turtle()   
        iraqCircle.shape("circle")
        iraqCircle.color("green")
        iraqCircle.penup()
        iraqCircle.goto(-295, 157)
        iraqCircle.onclick(iraqButton)

    #onclick function for afghanistan
def afganistan_letter(x,y):
        wn.clearscreen()
        noteturtle = turt.Turtle()
        noteturtle.hideturtle()
        noteturtle.speed(10)
        noteturtle.penup()
        noteturtle.goto(-400,-150)
        noteturtle.pendown()
        noteturtle.goto(400,-150)
        noteturtle.goto(400,200)
        noteturtle.goto(-400,200)
        noteturtle.goto(-400,-150)

        Afgnahistanwrite = turt.Turtle()
        Afgnahistanwrite.hideturtle()
        Afgnahistanwrite.write(veteran_letters[2]["letter"], align='center', font=('Arial', 16, 'normal'))
        restart = turt.Turtle()
        restart.hideturtle()
        restart.shapesize(6)
        restart.penup()
        restart.shape("square")
        restart.goto(-300,-300)
        restart.showturtle()
        restart.onclick(restart_game)
    #onclick function for iraq
def iraqButton(x,y):
        wn.clearscreen()
        noteturtle = turt.Turtle()
        noteturtle.hideturtle()
        noteturtle.speed(10)
        noteturtle.penup()
        noteturtle.goto(-400,-150)
        noteturtle.pendown()
        noteturtle.goto(400,-150)
        noteturtle.goto(400,200)
        noteturtle.goto(-400,200)
        noteturtle.goto(-400,-150)


        Iraqwrite = turt.Turtle()
        Iraqwrite.hideturtle()
        Iraqwrite.write(veteran_letters[1]["letter"], align='center', font=('Arial', 16, 'normal'))

        restart = turt.Turtle()
        restart.hideturtle()
        restart.shapesize(6)
        restart.penup()
        restart.shape("square")
        restart.goto(-300,-300)
        restart.showturtle()

    #onclick function for vietnam
def vietnamButton(x,y):
        wn.clearscreen()

        noteturtle = turt.Turtle()
        noteturtle.hideturtle()
        noteturtle.speed(10)
        noteturtle.penup()
        noteturtle.goto(-400,-150)
        noteturtle.pendown()
        noteturtle.goto(400,-150)
        noteturtle.goto(400,200)
        noteturtle.goto(-400,200)
        noteturtle.goto(-400,-150)


        Vietnamwrite = turt.Turtle()
        Vietnamwrite.hideturtle()
        Vietnamwrite.write(veteran_letters[0]["letter"], align='center', font=('Arial', 16, 'normal'))

        restart = turt.Turtle()
        restart.hideturtle()
        restart.shapesize(6)
        restart.penup()
        restart.shape("square")
        restart.goto(-300,-300)
        restart.showturtle()

letter_turtle.onclick(change_letter)




    # List of letters for war veterans by conflict
veteran_letters = [

    
        {
            "1955 - 1975": "Vietnam War",
            "letter": """Dear Vietnam War Veteran,
    Thank you for your service in a time of great division and uncertainty. 
    Your strength, endurance, and loyalty through difficult times reflect true heroism. 
    We honor you for your courage, both abroad and at home.
    Respectfully,
    A Nation That Remembers"""
        },
    
        {
            "2003 - 2011": "Iraq War",
            "letter": """Dear Iraq War Veteran,
    Your service and sacrifice in the face of uncertainty demonstrated the highest values of honor and courage. 
    You protected others and helped rebuild hope in difficult times. 
    Thank you for your bravery and dedication.
    Sincerely,
    A Grateful Citizen"""
        },
        {
            "2001 - 2014": "War in Afghanistan",
            "letter": """Dear Afghanistan War Veteran,
    For two decades, you served with courage and resilience in one of the longest conflicts in our nation’s history. 
    Your efforts to protect freedom and aid those in need will never be forgotten. 
    Thank you for your strength and sacrifice.
    With respect and gratitude,
    A Nation in Your Debt"""
        }
    ]

#if iraqCircle.onlclick:

#afghanistanWarLetter.onclick(upscore)

# user clicks on opened envelope to read letter


def restart_game(x,y):
        
        answer = turt.textinput("Restart","Would you like to restart? (y/n)")
        if answer == "y":
                wn.clearscreen()
                score = 0


       

        else:
               quit()
        
        
wn.mainloop()

