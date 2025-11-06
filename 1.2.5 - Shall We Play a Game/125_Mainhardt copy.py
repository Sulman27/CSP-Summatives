import turtle as turt
import math  # for distance calculations
import random as rand  # for randomizing mine placement
import os

# Configuration
GRID_ROWS = 8
GRID_COLS = 8
CELL_SIZE = 50
SCREEN_WIDTH = max(600, GRID_COLS * CELL_SIZE + 40)
SCREEN_HEIGHT = max(600, GRID_ROWS * CELL_SIZE + 140)

# State
screen = None
drawer = None  # turtle used to draw cells
writer = None  # turtle used to write text
revealed = set()
# State for flags: map (row,col) -> dict with {'turtle': Turtle, 'stamp_id': int}
flags = {}
# Put your image filename here (prefer GIF if PNG doesn't show)
FLAG_IMAGE = "minesweeperflag.png"


def _flag_image_path():
    """Return path to flag image: try same dir as script, but allow running interactively."""
    try:
        base = os.path.dirname(__file__)
    except NameError:
        base = os.getcwd()
    return os.path.join(base, FLAG_IMAGE)


def make_screen():
    global screen
    screen = turt.Screen()
    screen.title("Minesweeper")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.bgcolor("lightblue")
    return screen


def start_screen():
    global drawer, writer
    make_screen()

    # create drawer/writer turtles
    drawer = turt.Turtle(visible=False)
    writer = turt.Turtle(visible=False)
    drawer.speed(0)
    writer.speed(0)

    # Draw title and instructions
    drawer.penup()
    drawer.goto(0, SCREEN_HEIGHT // 2 - 80)
    drawer.color("darkblue")
    drawer.write("Minesweeper", align="center", font=("Arial", 36, "bold"))

    drawer.goto(0, SCREEN_HEIGHT // 2 - 120)
    drawer.color("black")
    drawer.write("Click the Start button to begin", align="center", font=("Arial", 16))

    # Draw start button centered
    btn_w, btn_h = 220, 60
    btn_x = -btn_w / 2
    btn_y = -40

    drawer.goto(btn_x, btn_y + btn_h / 2)
    drawer.setheading(0)
    drawer.color("green")
    drawer.begin_fill()
    drawer.pendown()
    for _ in range(2):
        drawer.forward(btn_w)
        drawer.right(90)
        drawer.forward(btn_h)
        drawer.right(90)
    drawer.end_fill()
    drawer.penup()

    drawer.goto(0, btn_y + btn_h / 2 - 12)
    drawer.color("white")
    drawer.write("Start Game", align="center", font=("Arial", 20, "bold"))

    # Record button bounds on the screen object for click handler
    screen.start_button = {
        "left": btn_x,
        "right": btn_x + btn_w,
        "top": btn_y + btn_h / 2,
        "bottom": btn_y - btn_h / 2,
    }

    # bind click handler
    screen.onclick(handle_start_click)


def handle_start_click(x, y):
    # Called when screen is clicked on start screen; check if inside button
    b = screen.start_button
    if b["left"] <= x <= b["right"] and b["bottom"] <= y <= b["top"]:
        screen.onclick(None)  # remove handler
        start_game()


def start_game():
    # Clear and set up game screen
    # Note: clearscreen resets many things. We'll re-create the screen's turtles & preload shape.
    screen.clearscreen()
    screen.title("Minesweeper - Game")
    screen.bgcolor("lightgray")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

    # recreate turtles
    global drawer, writer, revealed, flags
    drawer = turt.Turtle(visible=False)
    writer = turt.Turtle(visible=False)
    drawer.speed(0)
    writer.speed(0)
    revealed = set()
    flags = {}

    # Try to register the flag image as a turtle shape now (preload)
    path = _flag_image_path()
    print("Attempting to load flag image from:", path)
    try:
        # Use a fixed shape name to check later
        shape_name = "flagshape_image"
        # register only if not already present
        if shape_name not in screen.getshapes():
            # register the file path directly; turtle often prefers GIF files.
            screen.register_shape(shape_name, path)
        # store chosen shape name on screen for later use
        screen._flag_shape_name = shape_name
        screen._flag_image_loaded = True
    except Exception as e:
        # If registration fails (common for non-GIF on some setups), mark as not loaded
        print("Flag image registration failed:", e)
        screen._flag_image_loaded = False

    draw_grid(GRID_ROWS, GRID_COLS, CELL_SIZE)

    # bind unified grid click handler for both left and right buttons
    screen.onscreenclick(lambda x, y: handle_click(x, y, 1), 1)  # left click
    screen.onscreenclick(lambda x, y: handle_click(x, y, 3), 3)  # right click


def grid_origin(rows, cols, cell_size):
    # Top-left corner of the grid
    x0 = -cols * cell_size / 2
    y0 = rows * cell_size / 2
    return x0, y0


def draw_grid(rows, cols, cell_size):
    drawer.color("black")
    start_x, start_y = grid_origin(rows, cols, cell_size)
    for r in range(rows):
        for c in range(cols):
            x = start_x + c * cell_size
            y = start_y - r * cell_size
            draw_closed_cell(x, y, cell_size)


def draw_closed_cell(x, y, size):
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.fillcolor("darkgray")
    drawer.begin_fill()
    for _ in range(4):
        drawer.forward(size)
        drawer.right(90)
    drawer.end_fill()
    drawer.penup()


def reveal_cell(row, col):
    # If already revealed, do nothing
    if (row, col) in revealed:
        return
    revealed.add((row, col))

    x0, y0 = grid_origin(GRID_ROWS, GRID_COLS, CELL_SIZE)
    x = x0 + col * CELL_SIZE
    y = y0 - row * CELL_SIZE

    # draw opened cell background
    drawer.penup()
    drawer.goto(x, y)
    drawer.pendown()
    drawer.fillcolor("lightgray")
    drawer.begin_fill()
    for _ in range(4):
        drawer.forward(CELL_SIZE)
        drawer.right(90)
    drawer.end_fill()
    drawer.penup()

    # placeholder mark
    writer.penup()
    writer.goto(x + CELL_SIZE / 2, y - CELL_SIZE / 2 - 8)
    writer.color("black")
    writer.write("X", align="center", font=("Arial", 14, "bold"))


def handle_click(x, y, btn=1):
    """Unified handler for both left and right clicks."""
    x0, y0 = grid_origin(GRID_ROWS, GRID_COLS, CELL_SIZE)
    col = int((x - x0) // CELL_SIZE)
    row = int((y0 - y) // CELL_SIZE)
    if not (0 <= row < GRID_ROWS and 0 <= col < GRID_COLS):
        return
    if btn == 1:
        reveal_cell(row, col)
    elif btn == 3:
        toggle_flag(row, col)


def toggle_flag(row, col):
    """Toggle a flag image at (row, col) using only turtle, no tkinter.
    Stores per-cell {'turtle': Turtle, 'stamp_id': int} in flags to remove later.
    """
    key = (row, col)

    # Don't allow flagging revealed cells
    if (row, col) in revealed:
        return

    # Calculate center of the cell
    x0, y0 = grid_origin(GRID_ROWS, GRID_COLS, CELL_SIZE)
    cx = x0 + col * CELL_SIZE + CELL_SIZE / 2
    cy = y0 - row * CELL_SIZE - CELL_SIZE / 2

    # If already flagged, remove it by clearing the specific stamp
    if key in flags:
        info = flags.pop(key)
        t = info.get("turtle")
        sid = info.get("stamp_id")
        try:
            if t is not None and sid is not None:
                t.clearstamp(sid)  # remove that stamp only
            if t is not None:
                t.hideturtle()
                t.clear()
                t.reset()  # safe cleanup
                # Avoid destroying the turtle object; we let GC handle it
        except Exception:
            # fallback: try redrawing grid to remove stray marks
            drawer.clear()
            draw_grid(GRID_ROWS, GRID_COLS, CELL_SIZE)
        return

    # Create a small turtle to stamp the flag image
    flag_t = turt.Turtle(visible=False)
    flag_t.penup()
    flag_t.speed(0)
    flag_t.goto(cx, cy)

    # If image was registered successfully earlier, use it
    if getattr(screen, "_flag_image_loaded", False) and hasattr(screen, "_flag_shape_name"):
        shape_name = screen._flag_shape_name
        try:
            flag_t.shape(shape_name)
            flag_t.showturtle()
            stamp_id = flag_t.stamp()  # returns the stamp id
            # store the stamp id and turtle for later removal
            flags[key] = {"turtle": flag_t, "stamp_id": stamp_id}
            return
        except Exception as e:
            print("Stamping shape failed:", e)
            # fallthrough to drawing 'F'

    # fallback: draw a visible 'F' using the writer turtle (if image unavailable)
    writer.penup()
    writer.goto(cx, cy - 8)
    writer.color("red")
    writer.write("F", align="center", font=("Arial", 16, "bold"))
    # store a placeholder so toggle_flag can remove (we'll just clear/redraw grid when unflagging)
    flags[key] = {"turtle": None, "stamp_id": None}


# randomizing mine placement under each button that corresponds to a grid cell
def place_mines(num_mines):
    mines = set()
    while len(mines) < num_mines:
        r = rand.randint(0, GRID_ROWS - 1)
        c = rand.randint(0, GRID_COLS - 1)
        mines.add((r, c))
    return mines


def main():
    make_screen()
    start_screen()
    turt.mainloop()


if __name__ == "__main__":
    main()
