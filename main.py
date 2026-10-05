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

root = tk.Tk()
root.title("My Beautiful House")
root.geometry("900x700")
root.resizable(False, False)

canvas = tk.Canvas(root, width=900, height=650, bg="#F7B267")
canvas.pack()

# =========================================================
# SKY - ANIME SUNSET
# =========================================================

# Sky background
canvas.create_rectangle(0, 0, 900, 650, fill="#6C63A8", outline="")

# Sunset bands
canvas.create_rectangle(0, 300, 900, 400, fill="#E98B73", outline="")
canvas.create_rectangle(0, 400, 900, 650, fill="#F2A65A", outline="")

# Sun glow
canvas.create_oval(
    680, 190, 850, 360,
    fill="#F7C873",
    outline=""
)

canvas.create_oval(
    715, 225, 815, 325,
    fill="#FFE69A",
    outline=""
)

# Clouds
clouds = [
    (70, 90, 220, 130),
    (180, 120, 330, 155),
    (570, 90, 730, 130),
    (720, 125, 880, 165),
]

for x1, y1, x2, y2 in clouds:
    canvas.create_oval(
        x1, y1, x2, y2,
        fill="#EFA3A2",
        outline=""
    )

# =========================================================
# DISTANT MOUNTAINS
# =========================================================

canvas.create_polygon(
    0, 410,
    130, 270,
    240, 390,
    370, 250,
    520, 400,
    650, 290,
    790, 410,
    900, 300,
    900, 500,
    0, 500,
    fill="#5D527F",
    outline=""
)

# Snow on mountains
canvas.create_polygon(
    370, 250,
    325, 310,
    370, 290,
    395, 315,
    420, 285,
    fill="#D9D5E8",
    outline=""
)

canvas.create_polygon(
    650, 290,
    610, 335,
    650, 315,
    680, 340,
    705, 315,
    fill="#D9D5E8",
    outline=""
)

# =========================================================
# GROUND
# =========================================================

canvas.create_rectangle(
    0, 430, 900, 650,
    fill="#6FA35B",
    outline=""
)

# Grass shadows
canvas.create_oval(
    80, 440, 400, 590,
    fill="#5B8C4A",
    outline=""
)

canvas.create_oval(
    560, 440, 850, 590,
    fill="#5B8C4A",
    outline=""
)

# =========================================================
# LEFT TREE
# =========================================================

# Tree trunk shadow
canvas.create_rectangle(
    80, 300, 125, 500,
    fill="#633F2A",
    outline=""
)

canvas.create_polygon(
    100, 330,
    40, 390,
    105, 365,
    55, 440,
    125, 390,
    150, 450,
    135, 350,
    fill="#70442C",
    outline=""
)

# Tree leaves
tree_colors = [
    "#285943",
    "#347A4E",
    "#3E8A55",
    "#559B58",
    "#70AA5A"
]

leaf_positions = [
    (20, 220, 160, 350),
    (70, 180, 220, 330),
    (10, 280, 170, 400),
    (110, 230, 260, 370),
    (45, 160, 170, 290)
]

for i, pos in enumerate(leaf_positions):
    canvas.create_oval(
        *pos,
        fill=tree_colors[i],
        outline=""
    )

# =========================================================
# RIGHT TREE
# =========================================================

canvas.create_rectangle(
    780, 320, 820, 500,
    fill="#633F2A",
    outline=""
)

canvas.create_polygon(
    800, 350,
    750, 410,
    810, 380,
    755, 450,
    830, 400,
    850, 460,
    835, 350,
    fill="#70442C",
    outline=""
)

right_leaves = [
    (730, 220, 870, 350),
    (690, 270, 850, 390),
    (760, 170, 900, 320),
    (680, 230, 800, 350)
]

for i, pos in enumerate(right_leaves):
    canvas.create_oval(
        *pos,
        fill=tree_colors[i],
        outline=""
    )

# =========================================================
# HOUSE MAIN BODY - 3D WALL
# =========================================================

# Right-side depth
canvas.create_polygon(
    650, 310,
    720, 340,
    720, 520,
    650, 500,
    fill="#C58F69",
    outline="#75452D",
    width=3
)

# Main wall
canvas.create_rectangle(
    190, 300, 650, 510,
    fill="#F5D7A1",
    outline="#70442D",
    width=4
)

# Wall shadow
canvas.create_polygon(
    190, 450,
    650, 450,
    650, 510,
    190, 510,
    fill="#D8AD7C",
    outline=""
)

# =========================================================
# ROOF - 3D EFFECT
# =========================================================

# Roof dark side
canvas.create_polygon(
    130, 305,
    420, 90,
    720, 305,
    650, 335,
    420, 150,
    190, 335,
    fill="#302B4D",
    outline="#211D35",
    width=4
)

# Main roof
canvas.create_polygon(
    130, 290,
    420, 80,
    720, 290,
    650, 315,
    420, 125,
    195, 315,
    fill="#40395F",
    outline="#241F39",
    width=5
)

# Roof highlight
canvas.create_line(
    150, 285,
    420, 95,
    695, 285,
    fill="#8D7690",
    width=5
)

# Roof tiles
for x in range(220, 640, 55):
    canvas.create_line(
        x, 285,
        x + 45, 255,
        fill="#625879",
        width=2
    )

# =========================================================
# CHIMNEY
# =========================================================

canvas.create_rectangle(
    570, 145, 635, 265,
    fill="#A84E45",
    outline="#65332F",
    width=3
)

# Chimney top
canvas.create_rectangle(
    560, 135, 645, 155,
    fill="#63352F",
    outline="#422521",
    width=3
)

# Chimney bricks
for y in range(170, 250, 25):
    canvas.create_line(
        570, y, 635, y,
        fill="#713936",
        width=2
    )

canvas.create_line(
    600, 155, 600, 170,
    fill="#713936",
    width=2
)

# Smoke
canvas.create_oval(
    585, 90, 625, 130,
    fill="#D5CBD4",
    outline=""
)

canvas.create_oval(
    605, 55, 650, 105,
    fill="#D5CBD4",
    outline=""
)

canvas.create_oval(
    630, 25, 680, 75,
    fill="#D5CBD4",
    outline=""
)

# =========================================================
# SECOND FLOOR WINDOW
# =========================================================

# Window shadow
canvas.create_rectangle(
    330, 165, 510, 275,
    fill="#6A412E",
    outline="#39251F",
    width=4
)

# Window
canvas.create_rectangle(
    345, 180, 495, 265,
    fill="#FFD98A",
    outline="#4A3025",
    width=5
)

# Window glow
canvas.create_rectangle(
    355, 190, 485, 255,
    fill="#FFE7A6",
    outline=""
)

# Window cross
canvas.create_line(
    420, 180, 420, 265,
    fill="#70442D",
    width=5
)

canvas.create_line(
    345, 222, 495, 222,
    fill="#70442D",
    width=5
)

# Window shutters
canvas.create_rectangle(
    315, 180, 340, 270,
    fill="#70442D",
    outline="#43291F",
    width=3
)

canvas.create_rectangle(
    500, 180, 525, 270,
    fill="#70442D",
    outline="#43291F",
    width=3
)

# =========================================================
# FLOWER BOX
# =========================================================

canvas.create_rectangle(
    340, 270, 500, 295,
    fill="#75452D",
    outline="#4C2D20",
    width=3
)

# Flowers
flower_positions = [
    (360, 265),
    (385, 260),
    (410, 268),
    (435, 258),
    (460, 267),
    (485, 260)
]

for x, y in flower_positions:
    canvas.create_oval(
        x - 7, y - 7,
        x + 7, y + 7,
        fill="#F58FA8",
        outline="#B94E70"
    )
    canvas.create_oval(
        x - 2, y - 2,
        x + 2, y + 2,
        fill="#FFD75E",
        outline=""
    )

# =========================================================
# FRONT PORCH ROOF
# =========================================================

canvas.create_polygon(
    300, 310,
    420, 235,
    540, 310,
    520, 335,
    420, 270,
    320, 335,
    fill="#71432D",
    outline="#43291F",
    width=4
)

# Porch light
canvas.create_oval(
    408, 285, 432, 309,
    fill="#FFE27A",
    outline="#A86635",
    width=3
)

# =========================================================
# FRONT DOOR
# =========================================================

# Door shadow
canvas.create_rectangle(
    350, 335, 490, 515,
    fill="#5A3427",
    outline="#3B241D",
    width=5
)

# Door
canvas.create_rectangle(
    365, 345, 475, 510,
    fill="#8A5135",
    outline="#43291F",
    width=4
)

# Door panels
canvas.create_rectangle(
    380, 360, 460, 415,
    fill="#70412D",
    outline="#B4774E",
    width=3
)

canvas.create_rectangle(
    380, 430, 460, 495,
    fill="#70412D",
    outline="#B4774E",
    width=3
)

# Door window
canvas.create_rectangle(
    390, 370, 450, 405,
    fill="#FFD77D",
    outline="#4D3023",
    width=3
)

# Door knob
canvas.create_oval(
    450, 425, 462, 437,
    fill="#FFD45C",
    outline="#8A5A20",
    width=2
)

# =========================================================
# LEFT WINDOW
# =========================================================

canvas.create_rectangle(
    220, 350, 315, 430,
    fill="#FFE08D",
    outline="#563526",
    width=5
)

canvas.create_line(
    267, 350, 267, 430,
    fill="#70442D",
    width=4
)

canvas.create_line(
    220, 390, 315, 390,
    fill="#70442D",
    width=4
)

# Curtains
canvas.create_polygon(
    225, 355,
    255, 355,
    255, 425,
    225, 410,
    fill="#F8E7D0",
    outline=""
)

canvas.create_polygon(
    280, 355,
    310, 355,
    310, 410,
    280, 425,
    fill="#F8E7D0",
    outline=""
)

# =========================================================
# RIGHT WINDOW
# =========================================================

canvas.create_rectangle(
    525, 350, 620, 430,
    fill="#FFE08D",
    outline="#563526",
    width=5
)

canvas.create_line(
    572, 350, 572, 430,
    fill="#70442D",
    width=4
)

canvas.create_line(
    525, 390, 620, 390,
    fill="#70442D",
    width=4
)

# Curtains
canvas.create_polygon(
    530, 355,
    560, 355,
    560, 425,
    530, 410,
    fill="#F8E7D0",
    outline=""
)

canvas.create_polygon(
    585, 355,
    615, 355,
    615, 410,
    585, 425,
    fill="#F8E7D0",
    outline=""
)

# =========================================================
# FLOWER POTS
# =========================================================

def flower_pot(x, y):
    canvas.create_polygon(
        x, y,
        x + 40, y,
        x + 32, y + 35,
        x + 8, y + 35,
        fill="#B86643",
        outline="#703B29",
        width=2
    )

    canvas.create_line(
        x + 20, y,
        x + 20, y - 25,
        fill="#3C7541",
        width=3
    )

    canvas.create_oval(
        x + 5, y - 35,
        x + 20, y - 20,
        fill="#F08BA5",
        outline="#A84D6A"
    )

    canvas.create_oval(
        x + 18, y - 30,
        x + 33, y - 15,
        fill="#F5B85E",
        outline="#B86A28"
    )

flower_pot(300, 480)
flower_pot(505, 480)

# =========================================================
# HOUSE FOUNDATION
# =========================================================

canvas.create_polygon(
    170, 505,
    665, 505,
    700, 540,
    140, 540,
    fill="#765A54",
    outline="#4A3935",
    width=3
)

# Foundation highlights
canvas.create_line(
    170, 510,
    665, 510,
    fill="#A28A82",
    width=4
)

# =========================================================
# STONE PATH
# =========================================================

path_points = [
    (390, 535, 500, 535),
    (370, 565, 520, 565),
    (345, 600, 545, 600),
    (315, 645, 575, 645)
]

for x1, y1, x2, y2 in path_points:
    canvas.create_polygon(
        x1, y1,
        x2, y1,
        x2 + 15, y2,
        x1 - 15, y2,
        fill="#B7A59A",
        outline="#75645C",
        width=2
    )

# =========================================================
# FENCE
# =========================================================

# Horizontal fence
canvas.create_rectangle(
    0, 555, 180, 575,
    fill="#8A5A3C",
    outline="#5A3828"
)

canvas.create_rectangle(
    700, 555, 900, 575,
    fill="#8A5A3C",
    outline="#5A3828"
)

# Fence posts
for x in [20, 80, 140, 750, 810, 870]:
    canvas.create_polygon(
        x, 530,
        x + 35, 530,
        x + 35, 610,
        x, 610,
        fill="#9B6847",
        outline="#5A3828",
        width=2
    )

# =========================================================
# FLOWERS IN GARDEN
# =========================================================

garden_flowers = [
    (100, 520, "#F48FA3"),
    (145, 500, "#FFD166"),
    (690, 510, "#DDA0DD"),
    (740, 490, "#FF8FA3"),
    (800, 520, "#FFE066"),
    (850, 500, "#F4A6D7"),
]

for x, y, color in garden_flowers:
    # stem
    canvas.create_line(
        x, y,
        x, y + 35,
        fill="#347A42",
        width=3
    )

    # petals
    canvas.create_oval(
        x - 9, y - 5,
        x + 9, y + 10,
        fill=color,
        outline=""
    )

    canvas.create_oval(
        x - 5, y - 10,
        x + 5, y + 14,
        fill=color,
        outline=""
    )

    canvas.create_oval(
        x - 3, y - 3,
        x + 3, y + 3,
        fill="#FFD45C",
        outline=""
    )

# =========================================================
# HOME SWEET HOME SIGN
# =========================================================

canvas.create_polygon(
    40, 570,
    180, 570,
    180, 630,
    40, 630,
    fill="#A66D48",
    outline="#593A2A",
    width=3
)

canvas.create_text(
    110, 595,
    text="HOME",
    font=("Arial", 16, "bold"),
    fill="#3E2A20"
)

canvas.create_text(
    110, 617,
    text="SWEET HOME",
    font=("Arial", 10, "bold"),
    fill="#3E2A20"
)

# =========================================================
# ANIME SPARKLES
# =========================================================

sparkles = [
    (270, 180),
    (750, 250),
    (160, 420),
    (680, 440)
]

for x, y in sparkles:
    canvas.create_line(
        x - 8, y, x + 8, y,
        fill="#FFF3B0",
        width=2
    )
    canvas.create_line(
        x, y - 8, x, y + 8,
        fill="#FFF3B0",
        width=2
    )

# =========================================================
# TITLE
# =========================================================

canvas.create_text(
    450, 30,
    text="MY BEAUTIFUL HOUSE",
    font=("Arial", 20, "bold"),
    fill="#FFF1D0"
)

root.mainloop()