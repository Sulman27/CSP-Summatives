import turtle as turt

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


# -------------------- Restart function --------------------
def restart_program(x=None, y=None):
    answer = turt.textinput("Restart", "Do you want to restart the program? (y/n)")
    if answer and answer.lower() == "y":
        wn.clearscreen()
        main()
    else: 
        quit()


# -------------------- Afghanistan Letter Screen --------------------
def afghanistan_letter(x, y):
    wn.clearscreen()
    noteturtle = turt.Turtle()
    noteturtle.hideturtle()
    noteturtle.speed(10)
    noteturtle.penup()
    noteturtle.goto(-400, -150)
    noteturtle.pendown()
    noteturtle.goto(400, -150)
    noteturtle.goto(400, 200)
    noteturtle.goto(-400, 200)
    noteturtle.goto(-400, -150)

    Afgnahistanwrite = turt.Turtle()
    Afgnahistanwrite.hideturtle()
    Afgnahistanwrite.write(veteran_letters[2]["letter"], align='center', font=('Arial', 16, 'normal'))

    restart = turt.Turtle()
    restart.shape("square")
    restart.color("blue")
    restart.shapesize(2)
    restart.penup()
    restart.goto(-300, -250)
    restart.write("Restart", align='center', font=('Arial', 10, 'bold'))
    restart.onclick(restart_program)


# -------------------- Iraq Letter Screen --------------------
def iraqButton(x, y):
    wn.clearscreen()
    noteturtle = turt.Turtle()
    noteturtle.hideturtle()
    noteturtle.speed(10)
    noteturtle.penup()
    noteturtle.goto(-400, -150)
    noteturtle.pendown()
    noteturtle.goto(400, -150)
    noteturtle.goto(400, 200)
    noteturtle.goto(-400, 200)
    noteturtle.goto(-400, -150)

    Iraqwrite = turt.Turtle()
    Iraqwrite.hideturtle()
    Iraqwrite.write(veteran_letters[1]["letter"], align='center', font=('Arial', 16, 'normal'))

    restart = turt.Turtle()
    restart.shape("square")
    restart.color("blue")
    restart.shapesize(2)
    restart.penup()
    restart.goto(-300, -250)
    restart.write("Restart", align='center', font=('Arial', 10, 'bold'))
    restart.onclick(restart_program)


# -------------------- Vietnam Letter Screen --------------------
def vietnamButton(x, y):
    wn.clearscreen()
    noteturtle = turt.Turtle()
    noteturtle.hideturtle()
    noteturtle.speed(10)
    noteturtle.penup()
    noteturtle.goto(-400, -150)
    noteturtle.pendown()
    noteturtle.goto(400, -150)
    noteturtle.goto(400, 200)
    noteturtle.goto(-400, 200)
    noteturtle.goto(-400, -150)

    Vietnamwrite = turt.Turtle()
    Vietnamwrite.hideturtle()
    Vietnamwrite.write(veteran_letters[0]["letter"], align='center', font=('Arial', 16, 'normal'))

    restart = turt.Turtle()
    restart.shape("square")
    restart.color("blue")
    restart.shapesize(2)
    restart.penup()
    restart.goto(-300, -250)
    restart.write("Restart", align='center', font=('Arial', 10, 'bold'))
    restart.onclick(restart_program)


# -------------------- Change Letter (Main Menu) --------------------
def change_letter(x, y):
    letter_turtle.clear()
    letter_turtle.shape("openletter.gif")

    # Afghanistan button
    afghanistanWarLetter.penup()
    afghanistanWarLetter.goto(-150, 200)
    afghanistanWarLetter.color("black")
    afghanistanWarLetter.write("Afghanistan War 2001-2014", align='center', font=('Arial', 20, 'normal'))
    afghanistanCircle = turt.Turtle()
    afghanistanCircle.shape("circle")
    afghanistanCircle.color("grey")
    afghanistanCircle.penup()
    afghanistanCircle.goto(-295, 212)
    afghanistanCircle.onclick(afghanistan_letter)

    

    # Vietnam button
    VietnamWarLetter.penup()
    VietnamWarLetter.goto(-150, 175)
    VietnamWarLetter.color("black")
    VietnamWarLetter.write("Vietnam War 1955-1975", align='center', font=('Arial', 20, 'normal'))
    vietnamCircle = turt.Turtle()
    vietnamCircle.shape("circle")
    vietnamCircle.color("pink")
    vietnamCircle.penup()
    vietnamCircle.goto(-295, 187)
    vietnamCircle.onclick(vietnamButton)

    # Iraq button
    IraqWarLetter.penup()
    IraqWarLetter.goto(-150, 145)
    IraqWarLetter.color("black")
    IraqWarLetter.write("Iraq War Letter 2003-2011", align='center', font=('Arial', 20, 'normal'))
    iraqCircle = turt.Turtle()
    iraqCircle.shape("circle")
    iraqCircle.color("green")
    iraqCircle.penup()
    iraqCircle.goto(-295, 157)
    iraqCircle.onclick(iraqButton)


# -------------------- Main Setup --------------------
def main():
    global wn, letter_turtle, IraqWarLetter, afghanistanWarLetter, VietnamWarLetter

    wn = turt.Screen()
    wn.title("War Letters")


    wn.addshape("closed_letter.gif")
    wn.addshape("openletter.gif")

    # show a trigger warning
    all_wars = ""
    for letter in veteran_letters:
        years = next(iter(letter))
        all_wars += f"{letter[years]} ({years})\n"
    turt.textinput("Available Letters", f"wars mentioned: :\n{all_wars}" + " please press OK")


    letter_turtle = turt.Turtle(shape="closed_letter.gif")
    letter_turtle.penup()
    letter_turtle.goto(0, 0)

    IraqWarLetter = turt.Turtle()
    IraqWarLetter.hideturtle()

    afghanistanWarLetter = turt.Turtle()
    afghanistanWarLetter.hideturtle()

    VietnamWarLetter = turt.Turtle()
    VietnamWarLetter.hideturtle()

    letter_turtle.onclick(change_letter)


# -------------------- Run Program --------------------
main()
turt.mainloop()
