

def read_file(file_name: str) -> list:
    with open(file_name, "r") as file:
        data = file.read().splitlines()
    nested = [[int(y) for y in list(x)] for x in data]
    return nested


def get_visible_trees_num(forest: list) -> int:    
    row_size = len(forest[0])
    column_size = len(forest)
    visible_trees = 2*(row_size+column_size)-4
    for n in range(column_size):
        # skip edges
        if n in [0, column_size-1]:
            continue
        for m in range(row_size):
            # skip edges
            if m in [0, row_size-1]:
                continue  
            row = forest[n]
            column = [row[m] for row in forest]
            # check left
            if row[m] > sorted(row[:m])[-1]:
                visible_trees += 1
            # check right
            elif row[m] > sorted(row[m+1:])[-1]:
                visible_trees += 1
            # check up
            elif row[m] > sorted(column[:n])[-1]:
                visible_trees += 1
            # check down
            elif row[m] > sorted(column[n+1:])[-1]:
                visible_trees += 1   
    return visible_trees


def get_one_side_scenic(view: list, tree_hight: int):
    side_score = 0
    for i in range(len(view)):
        if view[i] < tree_hight:
            side_score += 1
        elif view[i] >= tree_hight:
            side_score += 1
            return side_score
    return side_score


def get_scenic_score(forest: list) -> int:
    row_size = len(forest[0])
    column_size = len(forest)
    best_score = 1
    for n in range(column_size):
        # skip edges
        if n in [0, column_size-1]:
            continue
        for m in range(row_size):
            # skip edges
            if m in [0, row_size-1]:
                continue  
            row = forest[n]
            column = [row[m] for row in forest]
            # check left
            left = get_one_side_scenic(row[:m][::-1], row[m])
            # check right
            right = get_one_side_scenic(row[m+1:], row[m])
            # check up
            up = get_one_side_scenic(column[:n][::-1], row[m])
            # check down
            down = get_one_side_scenic(column[n+1:], row[m])
            tree_score = left*right*up*down
            if tree_score > best_score:
                best_score = tree_score
    return best_score


if __name__ == "__main__":
    file_name = "input/08_treetop_tree_house.csv"

    test_data = [[3,0,3,7,3], [2,5,5,1,2], [6,5,3,3,2], [3,3,5,4,9], [3,5,3,9,0]]
    assert get_visible_trees_num(test_data.copy()) == 21

    forest = read_file(file_name)
    print(get_visible_trees_num(forest.copy()))

    assert get_scenic_score(test_data.copy()) == 8

    print(get_scenic_score(forest.copy()))
