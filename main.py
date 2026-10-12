# import tkinter as tk

# root= tk.Tk()
# root.title("My First Canvas")

# canvas = tk.Canvas(root,width=550, height=360, bg='white')
# canvas.pack()
# canvas.create_rectangle(40, 40, 220, 150, fill="coral")
# canvas.create_oval(280, 50, 440, 190, fill="lightblue")
# canvas.create_line(50, 250, 500, 250, width="4")
# canvas.create_text(275, 310, text="Hello Canvas", font=("Arial", 20))

# root.mainloop()

import tkinter as tk
import math

root = tk.Tk()
root.title("My Animated Neighborhood")
root.geometry("900x600")
root.resizable(False, False)

canvas = tk.Canvas(root, width=900, height=600, bg="#87CEEB")
canvas.pack()

# =====================================================
# GROUND
# =====================================================

canvas.create_rectangle(0, 400, 900, 600, fill="#79C267", outline="")

# Road
canvas.create_rectangle(0, 475, 900, 550, fill="#555555", outline="")

# Road lines
road_lines = []
for x in range(0, 900, 100):
    line = canvas.create_rectangle(
        x, 510, x + 55, 516,
        fill="white",
        outline=""
    )
    road_lines.append(line)

# =====================================================
# SUN
# =====================================================

sun = canvas.create_oval(
    735, 55, 815, 135,
    fill="#FFD93D",
    outline="#F4B400",
    width=3
)

sun_rays = []

for x1, y1, x2, y2 in [
    (775, 40, 775, 20),
    (775, 150, 775, 170),
    (720, 95, 700, 95),
    (830, 95, 850, 95),
    (730, 50, 715, 35),
    (820, 50, 835, 35),
    (730, 140, 715, 155),
    (820, 140, 835, 155)
]:
    sun_rays.append(
        canvas.create_line(
            x1, y1, x2, y2,
            fill="#FFD93D",
            width=4
        )
    )

# =====================================================
# CLOUDS
# =====================================================

def create_cloud(x, y):
    parts = []

    parts.append(canvas.create_oval(
        x, y + 15, x + 50, y + 45,
        fill="white", outline=""
    ))

    parts.append(canvas.create_oval(
        x + 25, y, x + 75, y + 45,
        fill="white", outline=""
    ))

    parts.append(canvas.create_oval(
        x + 55, y + 12, x + 105, y + 45,
        fill="white", outline=""
    ))

    parts.append(canvas.create_rectangle(
        x + 20, y + 25, x + 80, y + 45,
        fill="white", outline=""
    ))

    return parts


cloud1 = create_cloud(100, 70)
cloud2 = create_cloud(420, 45)


# =====================================================
# MAIN HOUSE
# =====================================================

# Shadow
canvas.create_oval(
    180, 390, 500, 425,
    fill="#5B9E4A",
    outline=""
)

# Main wall
canvas.create_rectangle(
    180, 210, 470, 400,
    fill="#FFF1B8",
    outline="#8B5E3C",
    width=4
)

# 3D side
canvas.create_polygon(
    470, 210,
    510, 230,
    510, 400,
    470, 400,
    fill="#E8C982",
    outline="#8B5E3C",
    width=3
)

# Main roof
canvas.create_polygon(
    145, 210,
    325, 75,
    505, 210,
    fill="#C94C4C",
    outline="#743737",
    width=4
)

# Roof highlight
canvas.create_line(
    170, 200,
    325, 90,
    480, 200,
    fill="#E76F51",
    width=8
)

# Chimney
canvas.create_rectangle(
    390, 115, 430, 175,
    fill="#B85C4A",
    outline="#743737",
    width=3
)

canvas.create_rectangle(
    385, 108, 435, 120,
    fill="#8E4638",
    outline=""
)

# =====================================================
# MAIN HOUSE WINDOWS
# =====================================================

def create_window(x, y):

    canvas.create_rectangle(
        x, y, x + 65, y + 65,
        fill="#6B432C",
        outline="#4B3021",
        width=3
    )

    glass = canvas.create_rectangle(
        x + 7, y + 7,
        x + 58, y + 58,
        fill="#8ED6F5",
        outline=""
    )

    canvas.create_line(
        x + 32, y + 7,
        x + 32, y + 58,
        fill="white",
        width=3
    )

    canvas.create_line(
        x + 7, y + 32,
        x + 58, y + 32,
        fill="white",
        width=3
    )

    return glass


window1 = create_window(200, 245)
window2 = create_window(390, 245)

# =====================================================
# DOOR
# =====================================================

canvas.create_rectangle(
    275, 290, 365, 400,
    fill="#754C32",
    outline="#4E3324",
    width=4
)

canvas.create_rectangle(
    285, 300, 355, 400,
    fill="#A66A3F",
    outline="#593B27",
    width=3
)

canvas.create_oval(
    335, 350, 345, 360,
    fill="#FFD700",
    outline=""
)

# =====================================================
# LEFT NEIGHBOR HOUSE
# =====================================================

# Wall
canvas.create_rectangle(
    20, 270, 145, 400,
    fill="#FFD1DC",
    outline="#79444F",
    width=3
)

# Roof
canvas.create_polygon(
    5, 270,
    82, 205,
    160, 270,
    fill="#6C63A8",
    outline="#443E70",
    width=3
)

# Door
canvas.create_rectangle(
    65, 325, 100, 400,
    fill="#7B4F35",
    outline="#4E3324"
)

# Window
canvas.create_rectangle(
    30, 300, 60, 335,
    fill="#9DE4FF",
    outline="#4B3021",
    width=2
)

canvas.create_line(
    45, 300, 45, 335,
    fill="white",
    width=2
)

canvas.create_line(
    30, 317, 60, 317,
    fill="white",
    width=2
)

# =====================================================
# RIGHT NEIGHBOR HOUSE
# =====================================================

# Wall
canvas.create_rectangle(
    555, 280, 680, 400,
    fill="#D6F5D6",
    outline="#426B42",
    width=3
)

# Roof
canvas.create_polygon(
    540, 280,
    617, 215,
    695, 280,
    fill="#D27D35",
    outline="#80491E",
    width=3
)

# Door
canvas.create_rectangle(
    600, 325, 635, 400,
    fill="#70452E",
    outline="#4E3324"
)

# Windows
canvas.create_rectangle(
    570, 305, 600, 340,
    fill="#8ED6F5",
    outline="#4B3021",
    width=2
)

canvas.create_rectangle(
    645, 305, 675, 340,
    fill="#8ED6F5",
    outline="#4B3021",
    width=2
)

# =====================================================
# TREES
# =====================================================

def create_tree(x, y):

    canvas.create_rectangle(
        x + 18, y + 55,
        x + 35, y + 125,
        fill="#795548",
        outline=""
    )

    canvas.create_oval(
        x, y + 20,
        x + 55, y + 80,
        fill="#4E9F3D",
        outline="#397A30",
        width=2
    )

    canvas.create_oval(
        x + 25, y,
        x + 80, y + 75,
        fill="#5EAA48",
        outline="#397A30",
        width=2
    )

    canvas.create_oval(
        x + 50, y + 20,
        x + 100, y + 80,
        fill="#4E9F3D",
        outline="#397A30",
        width=2
    )


create_tree(5, 350)
create_tree(700, 345)
create_tree(810, 350)

# =====================================================
# DOG HOUSE
# =====================================================

canvas.create_rectangle(
    45, 415, 145, 475,
    fill="#D99152",
    outline="#704020",
    width=3
)

canvas.create_polygon(
    35, 415,
    95, 370,
    155, 415,
    fill="#9E4F3D",
    outline="#65352A",
    width=3
)

canvas.create_oval(
    72, 430, 118, 475,
    fill="#4A3025",
    outline=""
)

canvas.create_rectangle(
    65, 395, 125, 415,
    fill="#F6D58A",
    outline="#704020"
)

canvas.create_text(
    95, 405,
    text="DOG",
    font=("Arial", 8, "bold"),
    fill="#704020"
)

# =====================================================
# DOG
# =====================================================

# Body
canvas.create_oval(
    110, 440, 180, 485,
    fill="#C9824B",
    outline="#633D27",
    width=3
)

# Head
canvas.create_oval(
    80, 410, 135, 460,
    fill="#C9824B",
    outline="#633D27",
    width=3
)

# Ears
canvas.create_oval(
    73, 410, 95, 440,
    fill="#8A542F",
    outline="#633D27",
    width=2
)

canvas.create_oval(
    120, 410, 140, 440,
    fill="#8A542F",
    outline="#633D27",
    width=2
)

# Eyes
canvas.create_oval(
    94, 425, 101, 432,
    fill="black"
)

canvas.create_oval(
    116, 425, 123, 432,
    fill="black"
)

# Nose
canvas.create_oval(
    103, 438, 113, 447,
    fill="black"
)

# Collar
canvas.create_line(
    88, 450, 127, 450,
    fill="#E84A5F",
    width=5
)

# Dog legs
canvas.create_rectangle(
    125, 470, 140, 495,
    fill="#A9683D",
    outline="#633D27"
)

canvas.create_rectangle(
    155, 470, 170, 495,
    fill="#A9683D",
    outline="#633D27"
)

# Tail
tail = canvas.create_arc(
    165, 430, 205, 475,
    start=270,
    extent=180,
    style=tk.ARC,
    outline="#C9824B",
    width=7
)

# =====================================================
# FLOWERS
# =====================================================

def flower(x, y):

    canvas.create_oval(
        x - 8, y - 8,
        x, y,
        fill="#FF6B81",
        outline=""
    )

    canvas.create_oval(
        x + 2, y - 8,
        x + 10, y,
        fill="#FF6B81",
        outline=""
    )

    canvas.create_oval(
        x - 8, y,
        x, y + 8,
        fill="#FF6B81",
        outline=""
    )

    canvas.create_oval(
        x + 2, y,
        x + 10, y + 8,
        fill="#FF6B81",
        outline=""
    )

    canvas.create_oval(
        x - 2, y - 2,
        x + 4, y + 4,
        fill="#FFD93D",
        outline=""
    )

    canvas.create_line(
        x + 1, y + 5,
        x + 1, y + 30,
        fill="#3E8E41",
        width=3
    )


flower(190, 430)
flower(520, 430)
flower(710, 440)

# =====================================================
# MOVING CAR
# =====================================================

car_x = -150

def create_car(x):

    body = canvas.create_rectangle(
        x, 485, x + 120, 520,
        fill="#E84A5F",
        outline="#8E2838",
        width=2
    )

    roof = canvas.create_polygon(
        x + 20, 485,
        x + 45, 455,
        x + 85, 455,
        x + 105, 485,
        fill="#E84A5F",
        outline="#8E2838",
        width=2
    )

    window = canvas.create_polygon(
        x + 48, 460,
        x + 78, 460,
        x + 92, 482,
        x + 42, 482,
        fill="#8ED6F5",
        outline=""
    )

    wheel1 = canvas.create_oval(
        x + 15, 510,
        x + 40, 535,
        fill="#222222",
        outline=""
    )

    wheel2 = canvas.create_oval(
        x + 85, 510,
        x + 110, 535,
        fill="#222222",
        outline=""
    )

    return [body, roof, window, wheel1, wheel2]


car_parts = create_car(car_x)


def move_car():

    global car_x

    car_x += 3

    for part in car_parts:
        canvas.move(part, 3, 0)

    if car_x > 900:
        car_x = -150

        for part in car_parts:
            canvas.move(part, -1050, 0)

    root.after(30, move_car)


# =====================================================
# FLYING BIRDS
# =====================================================

bird_x = 250
bird_y = 150

bird1 = canvas.create_arc(
    bird_x, bird_y,
    bird_x + 20, bird_y + 15,
    start=20,
    extent=140,
    style=tk.ARC,
    width=2
)

bird2 = canvas.create_arc(
    bird_x + 20, bird_y,
    bird_x + 40, bird_y + 15,
    start=20,
    extent=140,
    style=tk.ARC,
    width=2
)


def move_birds():

    canvas.move(bird1, 2, 0)
    canvas.move(bird2, 2, 0)

    position = canvas.coords(bird1)

    if position[0] > 900:
        canvas.move(bird1, -950, 0)
        canvas.move(bird2, -950, 0)

    root.after(40, move_birds)


# =====================================================
# DOG TAIL ANIMATION
# =====================================================

tail_angle = 0


def wag_tail():

    global tail_angle

    canvas.delete(tail)

    # This creates a simple wagging effect
    if tail_angle == 0:
        new_tail = canvas.create_arc(
            165, 425, 210, 470,
            start=250,
            extent=150,
            style=tk.ARC,
            outline="#C9824B",
            width=7
        )
        tail_angle = 1

    else:
        new_tail = canvas.create_arc(
            165, 425, 210, 470,
            start=290,
            extent=150,
            style=tk.ARC,
            outline="#C9824B",
            width=7
        )
        tail_angle = 0

    globals()["tail"] = new_tail

    root.after(300, wag_tail)


# =====================================================
# BLINKING HOUSE LIGHTS
# =====================================================

lights_on = False


def blink_lights():

    global lights_on

    if lights_on:

        canvas.itemconfig(window1, fill="#8ED6F5")
        canvas.itemconfig(window2, fill="#8ED6F5")

        lights_on = False

    else:

        canvas.itemconfig(window1, fill="#FFE680")
        canvas.itemconfig(window2, fill="#FFE680")

        lights_on = True

    root.after(1500, blink_lights)


# =====================================================
# START ANIMATIONS
# =====================================================

move_car()
move_birds()
wag_tail()
blink_lights()

# =====================================================
# TITLE
# =====================================================

canvas.create_text(
    450, 575,
    text="🏡 My Little Animated Neighborhood 🐶",
    font=("Arial", 18, "bold"),
    fill="#31572C"
)

root.mainloop()