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

def afganistan_letter(x,y):
    

def change_letter(x, y):
    letter_turtle.clear()
    letter_turtle.shape(letter_open)

    afghanistanWarLetter = turt.Turtle()
    afghanistanWarLetter.hideturtle()
    afghanistanWarLetter.penup()
    afghanistanWarLetter.goto(-150,200)
    afghanistanWarLetter.color("black")
    afghanistanWarLetter.write("Afghanistan War 2001-2014", align='center', font=('Arial', 20, 'normal'))

    afghanistanCircle = turt.Turtle()   
    afghanistanCircle.shape("circle")
    afghanistanCircle.color("grey")
    afghanistanCircle.penup()
    afghanistanCircle.goto(-295, 212)
    afghanistanCircle.onclick(afganistan_letter)

    VietnamWarLetter = turt.Turtle()
    VietnamWarLetter.hideturtle()
    VietnamWarLetter.penup()
    VietnamWarLetter.goto(-150,175)
    VietnamWarLetter.color("black")
    VietnamWarLetter.write("Vietnam War 1955-1975", align='center', font=('Arial', 20, 'normal'))

    vietnamCircle = turt.Turtle()   
    vietnamCircle.shape("circle")
    vietnamCircle.color("pink")
    vietnamCircle.penup()
    vietnamCircle.goto(-295, 187)


    IraqWarLetter = turt.Turtle()
    IraqWarLetter.hideturtle()
    IraqWarLetter.penup()
    IraqWarLetter.goto(-150, 145)
    IraqWarLetter.color("black")
    IraqWarLetter.write("Iraq War Letter 2003-2011", align='center', font=('Arial', 20, 'normal'))

    iraqCircle = turt.Turtle()   
    iraqCircle.shape("circle")
    iraqCircle.color("green")
    iraqCircle.penup()
    iraqCircle.goto(-295, 157)


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


#afghanistanWarLetter.onclick(upscore)

# user clicks on opened envelope to read letter

wn.mainloop()


