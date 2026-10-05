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
root.title("Beautiful Simple House")
root.geometry("700x550")
root.resizable(False, False)

canvas = tk.Canvas(root, width=700, height=550, bg="#87CEEB")
canvas.pack()

# =========================
# SKY
# =========================

# Sun - right side
canvas.create_oval(555, 60, 635, 140, fill="#FFD93D", outline="#F4B400", width=3)

# Sun rays
for x1, y1, x2, y2 in [
    (595, 45, 595, 25),
    (595, 155, 595, 175),
    (540, 100, 520, 100),
    (650, 100, 670, 100),
    (550, 55, 535, 40),
    (640, 55, 655, 40),
    (550, 145, 535, 160),
    (640, 145, 655, 160)
]:
    canvas.create_line(x1, y1, x2, y2, fill="#FFD93D", width=4)

# Clouds
def cloud(x, y):
    canvas.create_oval(x, y + 15, x + 50, y + 45,
                       fill="white", outline="")
    canvas.create_oval(x + 25, y, x + 75, y + 45,
                       fill="white", outline="")
    canvas.create_oval(x + 55, y + 12, x + 105, y + 45,
                       fill="white", outline="")
    canvas.create_rectangle(x + 20, y + 25, x + 80, y + 45,
                            fill="white", outline="")

cloud(70, 70)
cloud(400, 45)

# =========================
# GROUND
# =========================

canvas.create_rectangle(0, 400, 700, 550,
                        fill="#79C267", outline="")

# Small grass lines
for x in range(10, 700, 25):
    canvas.create_line(x, 410, x + 5, 400,
                       fill="#4E9F3D", width=2)

# =========================
# HOUSE SHADOW
# =========================

canvas.create_oval(120, 390, 510, 430,
                   fill="#5B9E4A", outline="")

# =========================
# HOUSE BODY
# =========================

# Main wall
canvas.create_rectangle(170, 210, 470, 400,
                        fill="#FFF1B8", outline="#8B5E3C", width=4)

# Right side wall for 3D effect
canvas.create_polygon(
    470, 210,
    510, 230,
    510, 400,
    470, 400,
    fill="#E8C982",
    outline="#8B5E3C",
    width=3
)

# =========================
# ROOF
# =========================

# Main roof
canvas.create_polygon(
    135, 210,
    320, 75,
    505, 210,
    fill="#C94C4C",
    outline="#743737",
    width=4
)

# Roof highlight
canvas.create_line(
    160, 200, 320, 90, 480, 200,
    fill="#E76F51",
    width=8
)

# Roof tiles
for i in range(5):
    canvas.create_line(
        180 + i * 30, 185 - i * 22,
        200 + i * 30, 200 - i * 22,
        fill="#9E3D3D",
        width=2
    )

# =========================
# CHIMNEY
# =========================

canvas.create_rectangle(390, 115, 430, 175,
                        fill="#B85C4A",
                        outline="#743737",
                        width=3)

# Chimney top
canvas.create_rectangle(385, 108, 435, 120,
                        fill="#8E4638",
                        outline="#743737",
                        width=2)

# =========================
# DOOR
# =========================

# Door frame
canvas.create_rectangle(275, 290, 365, 400,
                        fill="#754C32",
                        outline="#4E3324",
                        width=4)

# Door
canvas.create_rectangle(285, 300, 355, 400,
                        fill="#A66A3F",
                        outline="#593B27",
                        width=3)

# Door panels
canvas.create_rectangle(295, 315, 345, 350,
                        fill="#B8794A",
                        outline="#754C32",
                        width=2)

canvas.create_rectangle(295, 360, 345, 390,
                        fill="#B8794A",
                        outline="#754C32",
                        width=2)

# Door knob
canvas.create_oval(335, 350, 345, 360,
                   fill="#FFD700", outline="#A87900")

# =========================
# WINDOWS
# =========================

def window(x, y):
    # Frame
    canvas.create_rectangle(x, y, x + 65, y + 65,
                            fill="#6B432C",
                            outline="#4B3021",
                            width=3)

    # Glass
    canvas.create_rectangle(x + 7, y + 7, x + 58, y + 58,
                            fill="#8ED6F5",
                            outline="")

    # Cross
    canvas.create_line(x + 32, y + 7, x + 32, y + 58,
                       fill="white", width=3)

    canvas.create_line(x + 7, y + 32, x + 58, y + 32,
                       fill="white", width=3)

    # Window shine
    canvas.create_line(x + 13, y + 13, x + 25, y + 13,
                       fill="white", width=3)

window(195, 245)
window(390, 245)

# =========================
# FLOWERS
# =========================

def flower(x, y):
    canvas.create_oval(x - 8, y - 8, x, y,
                       fill="#FF6B81", outline="")
    canvas.create_oval(x + 2, y - 8, x + 10, y,
                       fill="#FF6B81", outline="")
    canvas.create_oval(x - 8, y, x, y + 8,
                       fill="#FF6B81", outline="")
    canvas.create_oval(x + 2, y, x + 10, y + 8,
                       fill="#FF6B81", outline="")

    canvas.create_oval(x - 2, y - 2, x + 4, y + 4,
                       fill="#FFD93D", outline="")

    canvas.create_line(x + 1, y + 5, x + 1, y + 30,
                       fill="#3E8E41", width=3)

flower(150, 425)
flower(535, 435)
flower(570, 415)

# =========================
# DOG HOUSE - LEFT SIDE
# =========================

# Dog house body
canvas.create_rectangle(35, 350, 140, 425,
                        fill="#D99152",
                        outline="#704020",
                        width=3)

# Dog house roof
canvas.create_polygon(
    25, 350,
    87, 300,
    150, 350,
    fill="#9E4F3D",
    outline="#65352A",
    width=3
)

# Dog house entrance
canvas.create_oval(65, 365, 110, 420,
                   fill="#4A3025",
                   outline="#633A28",
                   width=2)

# Dog house sign
canvas.create_rectangle(60, 330, 115, 350,
                        fill="#F6D58A",
                        outline="#704020")

canvas.create_text(87, 340,
                   text="DOG",
                   font=("Arial", 9, "bold"),
                   fill="#704020")

# =========================
# DOG
# =========================

# Dog body
canvas.create_oval(85, 425, 160, 475,
                   fill="#C9824B",
                   outline="#633D27",
                   width=3)

# Dog head
canvas.create_oval(55, 390, 115, 450,
                   fill="#C9824B",
                   outline="#633D27",
                   width=3)

# Ears
canvas.create_oval(48, 390, 70, 425,
                   fill="#8A542F",
                   outline="#633D27",
                   width=2)

canvas.create_oval(100, 390, 122, 425,
                   fill="#8A542F",
                   outline="#633D27",
                   width=2)

# Eyes
canvas.create_oval(70, 410, 77, 417,
                   fill="black")

canvas.create_oval(94, 410, 101, 417,
                   fill="black")

# Nose
canvas.create_oval(82, 425, 92, 434,
                   fill="black")

# Mouth
canvas.create_arc(78, 425, 98, 442,
                  start=0, extent=-180,
                  style=tk.ARC,
                  width=2)

# Dog legs
canvas.create_rectangle(100, 460, 115, 490,
                        fill="#A9683D",
                        outline="#633D27")

canvas.create_rectangle(135, 460, 150, 490,
                        fill="#A9683D",
                        outline="#633D27")

# Dog tail
canvas.create_arc(145, 420, 185, 465,
                  start=270, extent=180,
                  style=tk.ARC,
                  fill="#C9824B",
                  width=7)

# Dog collar
canvas.create_line(68, 440, 105, 440,
                   fill="#E84A5F", width=5)

# =========================
# EXTRA BUSHES
# =========================

def bush(x, y):
    canvas.create_oval(x, y, x + 50, y + 40,
                       fill="#4E9F3D", outline="#397A30", width=2)
    canvas.create_oval(x + 25, y - 15, x + 75, y + 40,
                       fill="#5EAA48", outline="#397A30", width=2)
    canvas.create_oval(x + 50, y, x + 100, y + 40,
                       fill="#4E9F3D", outline="#397A30", width=2)

bush(500, 365)
bush(600, 375)

# =========================
# TITLE
# =========================

canvas.create_text(
    350, 525,
    text="My Little Dream House 🏡",
    font=("Arial", 18, "bold"),
    fill="#31572C"
)

root.mainloop()