

import re


def get_top_crates(stack: dict) -> str:
    top_row = ""
    for i in stack.values():
        top_row += i[-1]
    return top_row


def top_crates_crate_mover_9000(stack: dict, moves: list) -> str:  
    move_list = [[int(x) for x in re.findall("\d+", i)] for i in moves]  
    for i in move_list:
        move, from_, to = i
        stack[to] = stack[to]+stack[from_][-1*move:][::-1]
        stack[from_] = stack[from_][:-1*move]

    return stack


def top_crates_crate_mover_9001(stack: dict, moves: list) -> str:    
    move_list = [[int(x) for x in re.findall("\d+", i)] for i in moves]  
    for i in move_list:
        move, from_, to = i
        crates = stack[from_][-1*move:]
        stack[from_] = stack[from_][:-1*move]
        stack[to] += crates

    return stack


#             [J]             [B] [W]
#             [T]     [W] [F] [R] [Z]
#         [Q] [M]     [J] [R] [W] [H]
#     [F] [L] [P]     [R] [N] [Z] [G]
# [F] [M] [S] [Q]     [M] [P] [S] [C]
# [L] [V] [R] [V] [W] [P] [C] [P] [J]
# [M] [Z] [V] [S] [S] [V] [Q] [H] [M]
# [W] [B] [H] [F] [L] [F] [J] [V] [B]
#  1   2   3   4   5   6   7   8   9 

if __name__ == "__main__":
    with open("input/05_supply_stacks.csv", "r") as file:
        crates_moves = file.read().splitlines()
        moves = []
        for line in crates_moves:  
            if line.strip().startswith("move"):
                moves.append(line)
            
    crate_stacks = dict(zip(range(1,10), 
        ["WMLF", "BZVMF", "HVRSLQ", "FSVQPMTJ", "LSW", "FVPMRJW", "JQCPNRF", "VHPSZWRB", "BMJCGHZW"]))

    test_crates = {1: "ZN", 2: "MCD", 3: "P"}
    test_data = [
        "move 1 from 2 to 1",
        "move 3 from 1 to 3",
        "move 2 from 2 to 1",
        "move 1 from 1 to 2"]

    test_result_for_9000 = top_crates_crate_mover_9000(test_crates.copy(), test_data)
    assert get_top_crates(test_result_for_9000) == "CMZ"  
    
    results_for_9000 = top_crates_crate_mover_9000(crate_stacks.copy(), moves)
    print(get_top_crates(results_for_9000))
    assert get_top_crates(results_for_9000) == "VRWBSFZWM"

    test_result_for_9001 = top_crates_crate_mover_9001(test_crates.copy(), test_data)
    assert get_top_crates(test_result_for_9001) == "MCD"

    results_for_9001 = top_crates_crate_mover_9001(crate_stacks.copy(), moves)
    print(get_top_crates(results_for_9001))
    assert get_top_crates(results_for_9001) == "RBTWJWMCF"
