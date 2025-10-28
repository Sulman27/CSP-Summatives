import turtle as turt

# start screen for minesweeper
def start_screen():
    turt.title("Minesweeper")
    turt.bgcolor("lightblue")
    turt.setup(width=600, height=600)
    
    # Draw title
    turt.penup()
    turt.goto(0, 200)
    turt.color("darkblue")
    turt.write("Minesweeper", align="center", font=("Arial", 36, "bold"))
    
    # Draw instructions
    turt.goto(0, 100)
    turt.color("black")
    turt.write("Click on a cell to reveal it.", align="center", font=("Arial", 16))
    
    turt.goto(0, 70)
    turt.write("Right-click to flag a cell.", align="center", font=("Arial", 16))
    
    turt.goto(0, 40)
    turt.write("Avoid the mines and clear the board!", align="center", font=("Arial", 16))
    
    # Draw start button
    turt.goto(0, -50)
    turt.color("green")
    turt.begin_fill()
    for _ in range(2):
        turt.forward(200)
        turt.right(90)
        turt.forward(50)
        turt.right(90)
    turt.end_fill()
    
    turt.penup()
    turt.goto(0, -35)
    turt.color("white")
    turt.write("Start Game", align="center", font=("Arial", 20, "bold"))
    
    # Hide turtle and wait for user action
    turt.hideturtle()
    turt.done()

# Call the start screen function to begin the game
if __name__ == "__main__":
    start_screen()