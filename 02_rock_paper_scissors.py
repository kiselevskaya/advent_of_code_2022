
# 
def shape_2_shape_scores(shape_weight: dict, round_outcome: dict) -> dict:
    all_possible_scores = {}
    for i in ["A", "B", "C"]:
        for j in ["X", "Y", "Z"]:
            if shape_weight[i] == shape_weight[j]:
                all_possible_scores[f"{i} {j}"] = round_outcome["draw"]+shape_weight[j]        
            elif (shape_weight[i]-shape_weight[j]) in [-1, 2]:
                all_possible_scores[f"{i} {j}"] = round_outcome["won"]+shape_weight[j]
            else:
                all_possible_scores[f"{i} {j}"] = round_outcome["lost"]+shape_weight[j]
    return all_possible_scores


def shape_2_outcome_scores(shape_weight: dict, round_outcome: dict) -> dict:
    move_outcomes = {}
    for i in ["A", "B", "C"]:
        for j in ["X", "Y", "Z"]:
            if j == "Y":
                print(i, j, round_outcome[j], shape_weight[i])
                move_outcomes[f"{i} {j}"] = round_outcome[j]+shape_weight[i]

            opponent_move_index = list(shape_weight.keys()).index(i)

            if j == "Z":
                move_weight = list(shape_weight.values())[(opponent_move_index+1)%6]
                move_outcomes[f"{i} {j}"] = round_outcome[j]+move_weight
            elif j == "X":
                move_weight = list(shape_weight.values())[(opponent_move_index+2)%6]
                move_outcomes[f"{i} {j}"] = round_outcome[j]+move_weight
    return move_outcomes


def total_score(all_rounds: list, combinations: dict) -> int:
    total_score = 0
    for i in all_rounds:
        total_score += combinations[i]
    return total_score


if __name__ == "__main__":
    with open("input/02_rock_paper_scissors.csv", "r") as file:
        strategy_guide = file.read().splitlines()

    shape_weight = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    round_outcome = {"lost": 0, "draw": 3, "won": 6, "X": 0, "Y": 3, "Z": 6}

    shape_2_shape = shape_2_shape_scores(shape_weight, round_outcome)
    shape_2_outcome = shape_2_outcome_scores(shape_weight, round_outcome)

    print(shape_2_shape)
    print(shape_2_outcome)

    print(total_score(strategy_guide, shape_2_shape))
    print(total_score(strategy_guide, shape_2_outcome))
