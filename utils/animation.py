def animate_object(canvas, obj_id, dx, dy, steps, delay):
    def step(count):
        if count < steps:
            canvas.move(obj_id, dx, dy)
            canvas.after(delay, lambda: step(count + 1))
    step(0)
