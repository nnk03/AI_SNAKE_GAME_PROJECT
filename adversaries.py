def manhattan(direction,snake_position,fruit_position):
    if direction=="UP" or direction=="DOWN":
        if snake_position[0]<=fruit_position[0]:
            return "RIGHT"
        else:
            return "LEFT"

    else:
        if snake_position[1]<=fruit_position[1]:
            return "DOWN"
        else:
            return "UP"
