def draw_hud(canvas):
    canvas.create_text(700, 20, text="Health: 100", font=("Arial", 12), fill="black", tag="hud")
    canvas.create_text(700, 40, text="Score: 0", font=("Arial", 12), fill="black", tag="hud")
