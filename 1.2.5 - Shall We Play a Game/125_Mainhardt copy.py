import turtle as turt

# --- Configuration ---
GRID_ROWS = 8
GRID_COLS = 8
CELL_SIZE = 50
SCREEN_WIDTH = GRID_COLS * CELL_SIZE + 40
SCREEN_HEIGHT = GRID_ROWS * CELL_SIZE + 140

# --- State ---
screen = None
drawer = None
cell_writer = None
active_cells = set()  # clicked/activated cells
marked_cells = {}     # right-click marked cells: (row,col) -> turtle

# --- Helper functions ---
def grid_origin():
    x0 = -GRID_COLS * CELL_SIZE / 2
    y0 = GRID_ROWS * CELL_SIZE / 2
    return x0, y0

def draw_grid():
    drawer.color("black")
    x0, y0 = grid_origin()
    for r in range(GRID_ROWS):
        for c in range(GRID_COLS):
            x = x0 + c * CELL_SIZE
            y = y0 - r * CELL_SIZE
            drawer.penup()
            drawer.goto(x, y)
            drawer.pendown()
            drawer.fillcolor("darkgray")
            drawer.begin_fill()
            for _ in range(4):
                drawer.forward(CELL_SIZE)
                drawer.right(90)
            drawer.end_fill()

def cell_coords(x, y):
    x0, y0 = grid_origin()
    col = int((x - x0) // CELL_SIZE)
    row = int((y0 - y) // CELL_SIZE)
    if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS:
        return row, col
    return None, None

# --- Game logic ---
def activate_cell(row, col):
    if (row, col) in active_cells:
        return
    active_cells.add((row, col))
    x0, y0 = grid_origin()
    x = x0 + col * CELL_SIZE
    y = y0 - row * CELL_SIZE
    drawer.penup()
    drawer.goto(x, y)
    drawer.fillcolor("green")
    drawer.begin_fill()
    for _ in range(4):
        drawer.forward(CELL_SIZE)
        drawer.right(90)
    drawer.end_fill()

def toggle_mark(row, col):
    key = (row, col)
    x0, y0 = grid_origin()
    cx = x0 + col * CELL_SIZE + CELL_SIZE / 2
    cy = y0 - row * CELL_SIZE - CELL_SIZE / 2

    # Remove mark if exists
    if key in marked_cells:
        marked_cells[key].clear()
        marked_cells[key].hideturtle()
        marked_cells.pop(key)
        return

    # Add a new mark
    mark = turt.Turtle(visible=False)
    mark.penup()
    mark.goto(cx, cy - 10)
    mark.color("red")
    mark.write("X", align="center", font=("Arial", 16, "bold"))
    marked_cells[key] = mark

def handle_click(x, y, button):
    row, col = cell_coords(x, y)
    if row is None:
        return
    if button == 1:
        activate_cell(row, col)
    elif button == 3:
        toggle_mark(row, col)

# --- Main ---
screen = turt.Screen()
screen.title("Grid Game")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
drawer = turt.Turtle(visible=False)
drawer.speed(0)
cell_writer = turt.Turtle(visible=False)
cell_writer.hideturtle()
draw_grid()

# Bind clicks
screen.onscreenclick(lambda x, y: handle_click(x, y, 1), 1)  # left click
screen.onscreenclick(lambda x, y: handle_click(x, y, 3), 3)  # right click

turt.mainloop()
