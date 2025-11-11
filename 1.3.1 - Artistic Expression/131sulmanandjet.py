import turtle as turt

wn = turt.Screen()

letter_closed = "closed_letter.gif"
wn.addshape(letter_closed)
letter_open = "openletter.gif"
wn.addshape(letter_open)
letter_turtle = turt.Turtle(shape=letter_closed)  
letter_turtle.penup()
letter_turtle.goto(0, 0)




def change_letter(x, y):
    letter_turtle.clear()
    letter_turtle.shape(letter_open)

letter_turtle.onclick(change_letter)
# List of letters for war veterans by conflict
veteran_letters = [
    {
        "war": "World War I",
        "letter": """Dear World War I Veteran,
Thank you for your bravery in enduring one of the most devastating conflicts in history. 
Your courage in the trenches and sacrifice for freedom continue to inspire generations. 
Your legacy reminds us of the cost of peace and the strength of unity in adversity.
With gratitude,
A Grateful Nation"""
    },
    {
        "war": "World War II",
        "letter": """Dear World War II Veteran,
Your service helped protect the world from tyranny and preserved democracy during its darkest hour.
From Normandy to the Pacific, your valor shaped the modern world. 
We remember your resilience and honor your commitment to justice and liberty.
With deepest respect,
A Thankful Citizen"""
    },
    {
        "war": "Korean War",
        "letter": """Dear Korean War Veteran,
Your courage in the 'Forgotten War' will never be forgotten by us. 
You fought under harsh conditions to defend freedom and uphold peace on the Korean Peninsula. 
Thank you for your quiet heroism and steadfast service.
Sincerely,
An Appreciative American"""
    },
    {
        "war": "Vietnam War",
        "letter": """Dear Vietnam War Veteran,
Thank you for your service in a time of great division and uncertainty. 
Your strength, endurance, and loyalty through difficult times reflect true heroism. 
We honor you for your courage, both abroad and at home.
Respectfully,
A Nation That Remembers"""
    },
    {
        "war": "Gulf War",
        "letter": """Dear Gulf War Veteran,
Thank you for standing ready to defend freedom and stability in a time of global tension. 
Your swift and professional service restored peace and protected countless lives. 
We honor your dedication and sacrifice.
With gratitude,
A Fellow American"""
    },
    {
        "war": "Iraq War",
        "letter": """Dear Iraq War Veteran,
Your service and sacrifice in the face of uncertainty demonstrated the highest values of honor and courage. 
You protected others and helped rebuild hope in difficult times. 
Thank you for your bravery and dedication.
Sincerely,
A Grateful Citizen"""
    },
    {
        "war": "War in Afghanistan",
        "letter": """Dear Afghanistan War Veteran,
For two decades, you served with courage and resilience in one of the longest conflicts in our nation’s history. 
Your efforts to protect freedom and aid those in need will never be forgotten. 
Thank you for your strength and sacrifice.
With respect and gratitude,
A Nation in Your Debt"""
    }
]
wn.mainloop()