

def read_file(file_name: str) -> list:
    with open(file_name, "r") as file:
        data = file.read().splitlines()
    return data


def trace_knots(motions: list) -> int:
    # start position [y, x] = [0,0]
    visited = {(0,0):1}
    knot = dict([(i,[0,0]) for i in list(range(10))])
    for move in motions:
        direction, steps = move[0], int(move.split()[1])
        
        while steps > 0:
            if direction == "R":
                knot[0][1] += 1
            elif direction == "L":
                knot[0][1] -= 1
            elif direction == "U":
                knot[0][0] += 1
            elif direction == "D":
                knot[0][0] -= 1

            for i in range(9):
                
                if abs(knot[i][1] - knot[i+1][1]) > 1 and abs(knot[i][0]-knot[i+1][0]) > 1:
                    if knot[i][1] >= knot[i+1][1]:  
                        if knot[i][0] >= knot[i+1][0]:
                            knot[i+1] = [knot[i][0]-1, knot[i][1]-1]
                        else:
                            knot[i+1] = [knot[i][0]+1, knot[i][1]-1]
                    else:
                        if knot[i][0] >= knot[i+1][0]:
                            knot[i+1] = [knot[i][0]-1, knot[i][1]+1]
                        else:
                            knot[i+1] = [knot[i][0]+1, knot[i][1]+1]
                elif abs(knot[i][1] - knot[i+1][1]) > 1:
                    if knot[i][1] >= knot[i+1][1]:
                        knot[i+1] = [knot[i][0], knot[i][1]-1]
                    else:
                        knot[i+1] = [knot[i][0], knot[i][1]+1]
                elif abs(knot[i][0]-knot[i+1][0]) > 1:
                    if knot[i][0] >= knot[i+1][0]:
                        knot[i+1] = [knot[i][0]-1, knot[i][1]]
                    else: 
                        knot[i+1] = [knot[i][0]+1, knot[i][1]]
                else:
                    break

            steps -= 1
            visited[tuple(knot[9])] = visited.get(tuple(knot[9]), 0)+1

    return len(visited.items())


def count_visited_pos(motions: list) -> int:
    # start position [y, x] = [0,0]
    head = [0,0]
    tail = [0,0]
    visited = {(0,0):1}
    for move in motions:
        direction, steps = move[0], int(move.split()[1])
        
        while steps > 0:
            if direction == "R":
                head[1] += 1
            elif direction == "L":
                head[1] -= 1
            elif direction == "U":
                head[0] += 1
            elif direction == "D":
                head[0] -= 1

            if abs(head[1] - tail[1]) > 1:
                if head[1] >= tail[1]:
                    tail = [head[0], head[1]-1]
                else:
                    tail = [head[0], head[1]+1]
            elif abs(head[0]-tail[0]) > 1:
                if head[0] >= tail[0]:
                    tail = [head[0]-1, head[1]]
                else: 
                    tail = [head[0]+1, head[1]]

            steps -= 1
            visited[tuple(tail)] = visited.get(tuple(tail), 0)+1

    return len(visited.items())


if __name__ == "__main__":
    file_name = "input/09_rope_bridge.csv"

    test_data = [
        "R 4", 
        "U 4", 
        "L 3", 
        "D 1", 
        "R 4", 
        "D 1", 
        "L 5", 
        "R 2"]

    assert count_visited_pos(test_data) == 13

    motions = read_file(file_name)
    print(count_visited_pos(motions.copy()))
    print(trace_knots(motions.copy()))
