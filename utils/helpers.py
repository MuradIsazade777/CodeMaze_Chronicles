def check_collision(canvas, obj1, obj2):
    coords1 = canvas.coords(obj1)
    coords2 = canvas.coords(obj2)
    return not (
        coords1[2] < coords2[0] or
        coords1[0] > coords2[2] or
        coords1[3] < coords2[1] or
        coords1[1] > coords2[3]
    )
