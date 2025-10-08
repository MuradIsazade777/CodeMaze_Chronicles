import tkinter as tk
from core.game import start_game

def launch_menu():
    root = tk.Tk()
    root.title("CodeMaze Chronicles")
    root.geometry("400x300")

    label = tk.Label(root, text="CodeMaze Chronicles", font=("Arial", 20))
    label.pack(pady=40)

    start_btn = tk.Button(root, text="Start Game", command=lambda: [root.destroy(), start_game()])
    start_btn.pack(pady=10)

    exit_btn = tk.Button(root, text="Exit", command=root.quit)
    exit_btn.pack(pady=10)

    root.mainloop()
