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
    
    # Draw start button (centered)
    turt.color("green")
    turt.penup()
    # center the rectangle at x=0, y=-50 with width 200 and height 50
    width, btn_height = 200, 50
    # center the rectangle at x=0, y=-50 -> top-left corner should be at (-width/2, -50 + btn_height/2)
    start_x = -width / 2
    start_y = -50 + btn_height / 2
    turt.penup()
    turt.goto(start_x, start_y)
    turt.setheading(0)
    turt.pendown()
    turt.begin_fill()
    for _ in range(2):
        turt.forward(width)
        turt.right(90)
        turt.forward(btn_height)
        turt.right(90)
    turt.end_fill()
    turt.penup()
    turt.goto(0, -50)
    turt.color("white")
    turt.write("Start Game", align="center", font=("Arial", 20, "bold"))
    
    # Hide turtle and wait for user action
    turt.hideturtle()
    turt.done()

# Call the start screen function to begin the game
if __name__ == "__main__":
    start_screen()

# make minesweeper grid
def draw_grid(rows, cols, cell_size):
    turt.speed(0)
    turt.penup()
    start_x = -cols * cell_size / 2
    start_y = rows * cell_size / 2
    turt.goto(start_x, start_y)
    
    for row in range(rows):
        for col in range(cols):
            turt.pendown()
            for _ in range(4):
                turt.forward(cell_size)
                turt.right(90)
            turt.penup()
            turt.forward(cell_size)
        turt.goto(start_x, start_y - (row + 1) * cell_size)