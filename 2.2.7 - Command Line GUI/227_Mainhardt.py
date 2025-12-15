
import tkinter as tk

# 1. Create the main application window
root = tk.Tk()

# 2. Set the window properties (title and size)
root.title("Command Line GUI")
root.geometry("900x900") # width x height

# 3. Add widgets (a Label widget in this case)
# The first argument specifies the parent window ('root')
label = tk.Label(root, text="Hello, Tkinter World!")

# 4. Arrange the widget using a geometry manager (pack)
label.pack(pady=50) # pady adds some vertical padding for better centering

# 5. Enter the main event loop
root.mainloop()
