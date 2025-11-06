import turtle as turt
import random as rand

# --- Configuration ---
GRID_ROWS = 8
GRID_COLS = 8
CELL_SIZE = 50
SCREEN_WIDTH = GRID_COLS * CELL_SIZE + 40
SCREEN_HEIGHT = GRID_ROWS * CELL_SIZE + 140
TIMER_START = 30
GOAL_SCORE = 10

# --- State ---
screen = None
drawer = None
writer = None
active_cells = set()
marked_cells = {}
score = 0
timer = TIMER_START
timer_up = False
targets = set()  # cells that are currently "targeted"

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
    global score
    if (row, col) in active_cells:
        return
    active_cells.add((row, col))
    x0, y0 = grid_origin()
    x = x0 + col * CELL_SIZE
    y = y0 - row * CELL_SIZE
    drawer.penup()
    drawer.goto(x, y)
    drawer.fillcolor("green" if (row, col) not in targets else "lime")
    drawer.begin_fill()
    for _ in range(4):
        drawer.forward(CELL_SIZE)
        drawer.right(90)
    drawer.end_fill()
    
    # If it was a target, score
    if (row, col) in targets:
        score += 1
        update_score()
        targets.remove((row, col))
        spawn_target()  # spawn a new target

def toggle_mark(row, col):
    key = (row, col)
    x0, y0 = grid_origin()
    cx = x0 + col * CELL_SIZE + CELL_SIZE/2
    cy = y0 - row * CELL_SIZE - CELL_SIZE/2

    if key in marked_cells:
        marked_cells[key].clear()
        marked_cells[key].hideturtle()
        marked_cells.pop(key)
        return

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

# --- UI updates ---
score_writer = None
timer_writer = None

def update_score():
    score_writer.clear()
    score_writer.write(f"Score: {score}", font=("Arial", 20, "normal"))

def update_timer():
    timer_writer.clear()
    timer_writer.write(f"Time: {timer}", font=("Arial", 20, "normal"))

# --- Timer ---
def countdown():
    global timer, timer_up
    if timer > 0:
        update_timer()
        timer -= 1
        screen.ontimer(countdown, 1000)
    else:
        timer_up = True
        update_timer()
        game_over()

def game_over():
    msg = turt.Turtle(visible=False)
    msg.hideturtle()
    msg.penup()
    msg.goto(0, 0)
    if score >= GOAL_SCORE:
        msg.write(f"You Win! Score: {score}", align="center", font=("Arial", 24, "bold"))
    else:
        msg.write(f"Time's Up! Score: {score}", align="center", font=("Arial", 24, "bold"))

# --- Targets ---
def spawn_target():
    while True:
        r = rand.randint(0, GRID_ROWS - 1)
        c = rand.randint(0, GRID_COLS - 1)
        if (r, c) not in active_cells and (r, c) not in targets:
            targets.add((r, c))
            draw_target(r, c)
            break

def draw_target(row, col):
    x0, y0 = grid_origin()
    x = x0 + col * CELL_SIZE
    y = y0 - row * CELL_SIZE
    drawer.penup()
    drawer.goto(x, y)
    drawer.fillcolor("yellow")
    drawer.begin_fill()
    for _ in range(4):
        drawer.forward(CELL_SIZE)
        drawer.right(90)
    drawer.end_fill()

# --- Main ---
screen = turt.Screen()
screen.title("Grid Catch Game")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

drawer = turt.Turtle(visible=False)
drawer.speed(0)
cell_writer = turt.Turtle(visible=False)
cell_writer.hideturtle()

# UI turtles
score_writer = turt.Turtle(visible=False)
score_writer.penup()
score_writer.goto(-SCREEN_WIDTH//2 + 80, SCREEN_HEIGHT//2 - 40)

timer_writer = turt.Turtle(visible=False)
timer_writer.penup()
timer_writer.goto(SCREEN_WIDTH//2 - 120, SCREEN_HEIGHT//2 - 40)

draw_grid()
update_score()
update_timer()

# Bind clicks
screen.onscreenclick(lambda x, y: handle_click(x, y, 1), 1)
screen.onscreenclick(lambda x, y: handle_click(x, y, 3), 3)

# Spawn initial targets
for _ in range(3):
    spawn_target()

# Start timer
countdown()

turt.mainloop()
