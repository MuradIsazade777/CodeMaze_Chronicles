import tkinter as tk

def show_game_over():
    root = tk.Tk()
    root.title("Game Over")
    root.geometry("400x200")

    label = tk.Label(root, text="Game Over", font=("Arial", 24), fg="red")
    label.pack(pady=40)

    exit_btn = tk.Button(root, text="Exit", command=root.quit)
    exit_btn.pack(pady=10)

    root.mainloop()
