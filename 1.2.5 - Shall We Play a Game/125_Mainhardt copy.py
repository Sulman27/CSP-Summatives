import turtle as turt
import math

# Global variables for the game
GRID_SIZE = 8  # 8x8 grid
CELL_SIZE = 40  # pixels per cell
screen = None  # Will store the screen object for click handling
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
    
    # Hide turtle and set up click handling
    turt.hideturtle()
    
    # Set up screen for click handling
    global screen
    screen = turt.Screen()
    
    # Calculate start button boundaries for click detection
    button_width = 200
    button_height = 50
    button_left = -button_width/2
    button_right = button_width/2
    button_top = -25  # -50 + button_height/2
    button_bottom = -75  # -50 - button_height/2
    
    # Click handler function
    def handle_click(x, y):
        # Check if click is within start button boundaries
        if (button_left <= x <= button_right and 
            button_bottom <= y <= button_top):
            screen.onclick(None)  # Remove click handler
            
    
    # Bind click handler
    screen.onclick(handle_click)
    screen.listen()
    
    turt.done()



# Call the start screen function to begin the game
if __name__ == "__main__":
    start_screen()
