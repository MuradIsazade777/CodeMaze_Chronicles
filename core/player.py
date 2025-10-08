class Player:
    def __init__(self, canvas, x, y, size, color):
        self.canvas = canvas
        self.size = size
        self.rect = canvas.create_rectangle(x, y, x+size, y+size, fill=color)
        self.dx = 0
        self.dy = 0

    def move(self):
        self.canvas.move(self.rect, self.dx, self.dy)

    def set_direction(self, dx, dy):
        self.dx = dx
        self.dy = dy
