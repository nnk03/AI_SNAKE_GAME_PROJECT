def is_adjacent(coord1,coord2):
    if coord1[0]==coord2[0]:
        if coord1[1]==coord2[1]+10:
            return True
        elif coord1[1]==coord2[1]-10:
            return True

    elif coord1[1]==coord2[1]:
        if coord1[0]==coord2[0]+10:
            return True
        elif coord1[0]==coord2[0]-10:
            return True

    return False

def safe_manhattan(direction,snake_position,fruit_position,snake_1_body,snake_2_body,snake_3_body,window_x,window_y):
    if direction=="UP":
        available_moves=["UP","RIGHT","LEFT"]

        if snake_position[1]>fruit_position[1]:
            flag=True
            next_position=[snake_position[0],snake_position[1]-10]

            for block in snake_1_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_1_body[0],next_position):
                flag=False

            for block in snake_2_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_2_body[0],next_position):
                flag=False

            for block in snake_3_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_3_body[0],next_position):
                flag=False


            if flag:
                return "UP"
            else:
                available_moves.remove("UP")

        if snake_position[0]<=fruit_position[0]:
            flag=True
            next_position=[snake_position[0]+10,snake_position[1]]

            if snake_position[0]==window_x-10:
                flag=False
            
            for block in snake_1_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_1_body[0],next_position):
                flag=False

            for block in snake_2_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_2_body[0],next_position):
                flag=False

            for block in snake_3_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_3_body[0],next_position):
                flag=False

            if flag:
                return "RIGHT"
            else:
                available_moves.remove("RIGHT")

        else:
            flag=True
            next_position=[snake_position[0]-10,snake_position[1]]

            for block in snake_1_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_1_body[0],next_position):
                flag=False

            for block in snake_2_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_2_body[0],next_position):
                flag=False

            for block in snake_3_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_3_body[0],next_position):
                flag=False

            if flag:
                return "LEFT"
            else:
                available_moves.remove("LEFT")

        if available_moves:
            return available_moves[0]
        else:
            return direction

    elif direction=="DOWN":
        available_moves=["DOWN","RIGHT","LEFT"]

        if snake_position[1]<fruit_position[1]:
            flag=True
            next_position=[snake_position[0],snake_position[1]+10]

            for block in snake_1_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_1_body[0],next_position):
                flag=False

            for block in snake_2_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_2_body[0],next_position):
                flag=False

            for block in snake_3_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_3_body[0],next_position):
                flag=False


            if flag:
                return "DOWN"
            else:
                available_moves.remove("DOWN")

        if snake_position[0]<=fruit_position[0]:
            flag=True
            next_position=[snake_position[0]+10,snake_position[1]]

            if snake_position[0]==window_x-10:
                flag=False
            
            for block in snake_1_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_1_body[0],next_position):
                flag=False

            for block in snake_2_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_2_body[0],next_position):
                flag=False

            for block in snake_3_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_3_body[0],next_position):
                flag=False

            if flag:
                return "RIGHT"
            else:
                available_moves.remove("RIGHT")

        else:
            flag=True
            next_position=[snake_position[0]-10,snake_position[1]]

            for block in snake_1_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_1_body[0],next_position):
                flag=False

            for block in snake_2_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_2_body[0],next_position):
                flag=False

            for block in snake_3_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_3_body[0],next_position):
                flag=False

            if flag:
                return "LEFT"
            else:
                available_moves.remove("LEFT")

        if available_moves:
            return available_moves[0]
        else:
            return direction

    elif direction=="LEFT":
        
        available_moves=["DOWN","UP","LEFT"]

        if snake_position[0]>fruit_position[0]:
            flag=True
            next_position=[snake_position[0]-10,snake_position[1]]

            for block in snake_1_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_1_body[0],next_position):
                flag=False

            for block in snake_2_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_2_body[0],next_position):
                flag=False

            for block in snake_3_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_3_body[0],next_position):
                flag=False


            if flag:
                return "LEFT"
            else:
                available_moves.remove("LEFT")

        if snake_position[1]<=fruit_position[1]:
            flag=True
            next_position=[snake_position[0],snake_position[1]+10]

            if snake_position[0]==window_y-10:
                flag=False
            
            for block in snake_1_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_1_body[0],next_position):
                flag=False

            for block in snake_2_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_2_body[0],next_position):
                flag=False

            for block in snake_3_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_3_body[0],next_position):
                flag=False

            if flag:
                return "DOWN"
            else:
                available_moves.remove("DOWN")

        else:
            flag=True
            next_position=[snake_position[0],snake_position[1]-10]

            for block in snake_1_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_1_body[0],next_position):
                flag=False

            for block in snake_2_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_2_body[0],next_position):
                flag=False

            for block in snake_3_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_3_body[0],next_position):
                flag=False

            if flag:
                return "UP"
            else:
                available_moves.remove("UP")

        if available_moves:
            return available_moves[0]
        else:
            return direction

    else:
        available_moves=["DOWN","UP","RIGHT"]

        if snake_position[0]<fruit_position[0]:
            flag=True
            next_position=[snake_position[0]+10,snake_position[1]]

            for block in snake_1_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_1_body[0],next_position):
                flag=False

            for block in snake_2_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_2_body[0],next_position):
                flag=False

            for block in snake_3_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_3_body[0],next_position):
                flag=False


            if flag:
                return "RIGHT"
            else:
                available_moves.remove("RIGHT")

        if snake_position[1]<=fruit_position[1]:
            flag=True
            next_position=[snake_position[0],snake_position[1]+10]

            if snake_position[0]==window_y-10:
                flag=False
            
            for block in snake_1_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_1_body[0],next_position):
                flag=False

            for block in snake_2_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_2_body[0],next_position):
                flag=False

            for block in snake_3_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_3_body[0],next_position):
                flag=False

            if flag:
                return "DOWN"
            else:
                available_moves.remove("DOWN")

        else:
            flag=True
            next_position=[snake_position[0],snake_position[1]-10]

            for block in snake_1_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_1_body[0],next_position):
                flag=False

            for block in snake_2_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_2_body[0],next_position):
                flag=False

            for block in snake_3_body:
                if block==next_position:
                    flag=False

            if is_adjacent(snake_3_body[0],next_position):
                flag=False

            if flag:
                return "UP"
            else:
                available_moves.remove("UP")

        if available_moves:
            return available_moves[0]
        else:
            return direction
