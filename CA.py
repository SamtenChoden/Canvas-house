
import tkinter as tk

root = tk.Tk()
root.title("Canvas Animation")

canvas = tk.Canvas(
    root,
    width=600,
    height=350,
    bg="white"
)
canvas.pack()

# Ground: simple black line
GROUND = 300
canvas.create_line(
    0, GROUND, 600, GROUND,
    fill="black",
    width=2
)

# Ball
ball = canvas.create_oval(
    20, 120, 70, 170,
    fill="orange",
    outline=""
)

# Starting speed
dx = 3
dy = 0
gravity = 0.45
bounce = 0.75
radius = 25
stopped = False

def animate():
    global dx, dy, stopped

    if stopped:
        return

    x1, y1, x2, y2 = canvas.coords(ball)

    # Apply gravity
    dy += gravity

    # Move horizontally
    canvas.move(ball, dx, dy)

    x1, y1, x2, y2 = canvas.coords(ball)

    # Bounce off the left and right edges
    if x1 <= 0:
        dx = abs(dx)
    elif x2 >= 600:
        dx = -abs(dx)

    # Bounce off the ground
    if y2 >= GROUND:
        canvas.move(ball, 0, GROUND - y2)
        dy = -abs(dy) * bounce

        # Stop when the bounce becomes very small
        if abs(dy) < 2:
            dy = 0
            dx = 0
            stopped = True

    if not stopped:
        root.after(16, animate)

animate()
root.mainloop()