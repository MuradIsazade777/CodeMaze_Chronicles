import random

class Enemy:
    def __init__(self, canvas, x, y, size, color):
        self.canvas = canvas
        self.size = size
        self.rect = canvas.create_oval(x, y, x+size, y+size, fill=color)
        self.dx = random.choice([-2, 2])
        self.dy = random.choice([-2, 2])

    def move(self):
        self.canvas.move(self.rect, self.dx, self.dy)
