import turtle as turt
import math # for distance calculations
import random as rand # for randomizing mine placement
import os
import tkinter as tk
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
# Flags state: mapping (row,col) -> canvas image id
flags = {}
# Cached PhotoImage objects by path to avoid GC
_flag_images = {}
# default flag image path (change this to switch image)
FLAG_IMAGE = os.path.join(os.path.dirname(__file__), "minesweeperflag.png")


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
    screen.clearscreen()
    screen.title("Minesweeper - Game")
    screen.bgcolor("lightgray")
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)

    # recreate turtles
    global drawer, writer, revealed
    drawer = turt.Turtle(visible=False)
    writer = turt.Turtle(visible=False)
    drawer.speed(0)
    writer.speed(0)
    revealed = set()

    draw_grid(GRID_ROWS, GRID_COLS, CELL_SIZE)

    # bind grid click handlers: left = reveal, right = flag toggle
    # Use onscreenclick with btn to distinguish buttons
    screen.onscreenclick(handle_left_click, 1)
    screen.onscreenclick(handle_right_click, 3)


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


def handle_grid_click(x, y):
    # Convert click to grid row/col
    x0, y0 = grid_origin(GRID_ROWS, GRID_COLS, CELL_SIZE)
    col = int((x - x0) // CELL_SIZE)
    row = int((y0 - y) // CELL_SIZE)
    if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS:
        reveal_cell(row, col)


def handle_left_click(x, y):
    # left click = reveal
    x0, y0 = grid_origin(GRID_ROWS, GRID_COLS, CELL_SIZE)
    col = int((x - x0) // CELL_SIZE)
    row = int((y0 - y) // CELL_SIZE)
    if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS:
        reveal_cell(row, col)


def handle_right_click(x, y):
    # right click = toggle flag image on the cell
    x0, y0 = grid_origin(GRID_ROWS, GRID_COLS, CELL_SIZE)
    col = int((x - x0) // CELL_SIZE)
    row = int((y0 - y) // CELL_SIZE)
    if 0 <= row < GRID_ROWS and 0 <= col < GRID_COLS:
        toggle_flag(row, col)


def _get_canvas_and_photo(path):
    """Return (canvas, PhotoImage) for given path, caching PhotoImage to avoid GC."""
    if not os.path.isfile(path):
        # file not found: return None to signal missing image
        return None, None
    canvas = screen.getcanvas()
    if path not in _flag_images:
        # create PhotoImage and cache it
        try:
            _flag_images[path] = tk.PhotoImage(file=path)
        except Exception:
            # couldn't load image
            _flag_images[path] = None
    return canvas, _flag_images[path]


def toggle_flag(row, col):
    """Toggle flag image at (row, col). Uses tkinter canvas to place image centered in cell.
    If FLAG_IMAGE is missing or cannot be loaded, this function will draw a simple red 'F' instead.
    """
    key = (row, col)
    x0, y0 = grid_origin(GRID_ROWS, GRID_COLS, CELL_SIZE)
    # center of cell in turtle coords
    cx = x0 + col * CELL_SIZE + CELL_SIZE / 2
    cy = y0 - row * CELL_SIZE - CELL_SIZE / 2

    # If flag already present, remove it
    if key in flags:
        # flags[key] stores the canvas image id (int) or a placeholder writer mark
        item = flags.pop(key)
        canvas = screen.getcanvas()
        try:
            canvas.delete(item)
        except Exception:
            # if deletion fails, try clearing writer mark
            drawer.clear()
            draw_grid(GRID_ROWS, GRID_COLS, CELL_SIZE)
        return

    # Try to place image
    canvas, photo = _get_canvas_and_photo(FLAG_IMAGE)
    if canvas and photo:
        # convert turtle coords (cx,cy) to canvas pixel coords
        canvas_x = cx + screen.window_width() / 2
        canvas_y = screen.window_height() / 2 - cy
        img_id = canvas.create_image(canvas_x, canvas_y, image=photo)
        flags[key] = img_id
    else:
        # fallback: draw a red 'F' using a dedicated turtle writer and store placeholder
        temp = turt.Turtle(visible=False)
        temp.hideturtle()
        temp.penup()
        temp.goto(cx, cy - 8)
        temp.color("red")
        temp.write("F", align="center", font=("Arial", 16, "bold"))
        # For fallback we cannot delete easily via canvas, so store the turtle object id
        # We'll delete it by clearing and redrawing the grid when needed
        flags[key] = temp.get_shapepoly() if hasattr(temp, 'get_shapepoly') else None


def set_flag_image(path):
    """Change the flag image used for flags. Path can be absolute or relative.
    Call this before starting a game or while running to change subsequent flags.
    """
    global FLAG_IMAGE
    FLAG_IMAGE = path
    # preload if possible
    _get_canvas_and_photo(path)
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

