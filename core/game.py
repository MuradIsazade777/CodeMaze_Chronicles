import tkinter as tk
from core.config import *
from core.maze_generator import generate_maze
from core.player import Player
from core.enemy import Enemy
from ui.hud import draw_hud

def start_game():
    root = tk.Tk()
    root.title("CodeMaze Chronicles")
    canvas = tk.Canvas(root, width=SCREEN_WIDTH, height=SCREEN_HEIGHT, bg=FLOOR_COLOR)
    canvas.pack()

    maze = generate_maze(20, 20)
    tile_size = 30

   
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            x = c * tile_size
            y = r * tile_size
            if maze[r][c] == 1:
                color = WALL_COLOR
            elif maze[r][c] == 2:
                color = EXIT_COLOR
            else:
                color = FLOOR_COLOR
            canvas.create_rectangle(x, y, x+tile_size, y+tile_size, fill=color)

    player = Player(canvas, tile_size, tile_size, tile_size, PLAYER_COLOR)
    enemy = Enemy(canvas, 10 * tile_size, 10 * tile_size, tile_size, ENEMY_COLOR)
    draw_hud(canvas)

    def is_walkable(x, y):
     col = int(x // tile_size)
     row = int(y // tile_size)
     if 0 <= row < len(maze) and 0 <= col < len(maze[0]):
        return maze[row][col] != 1
     return False


    def move_player(dx, dy):
        coords = canvas.coords(player.rect)
        new_x = coords[0] + dx
        new_y = coords[1] + dy
        if is_walkable(new_x, new_y):
            canvas.move(player.rect, dx, dy)

    def update():
        enemy.move()
        root.after(int(1000 / FPS), update)

    def key(event):
        key_map = {
            "Up": (0, -tile_size),
            "Down": (0, tile_size),
            "Left": (-tile_size, 0),
            "Right": (tile_size, 0)
        }
        if event.keysym in key_map:
            dx, dy = key_map[event.keysym]
            move_player(dx, dy)

    root.bind("<KeyPress>", key)
    update()
    root.mainloop()
