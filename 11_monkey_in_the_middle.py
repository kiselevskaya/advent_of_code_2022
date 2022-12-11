

import re
import copy


def read_file(file_name: str) -> list:
    with open(file_name, "r") as file:
        data = file.read().splitlines()
    return data


def preprocess_data(data: list) -> dict:
    monkeys = {}

    for i in range(0, len(data), 6):
        n_monkey = int(re.findall(r"\d+", data[i])[0])
        monkeys[int(n_monkey)] = {}
        
        items = [int(x) for x in data[i+1].split(":")[1].split(",")]
        monkeys[int(n_monkey)]["Starting item"] = items
        
        opperand = re.findall(r"\*|\+", data[i+2].split("=")[1])[0]
        num = re.findall(r"\d+", data[i+2])
        num = None if len(num)==0 else int(num[0])
        monkeys[int(n_monkey)]["Operations"] = [opperand, num]

        monkeys[int(n_monkey)]["Test"] = int(re.findall(r"\d+", data[i+3])[0])

        monkeys[int(n_monkey)]["true"] = int(re.findall(r"\d+", data[i+4])[0])
        monkeys[int(n_monkey)]["false"] = int(re.findall(r"\d+", data[i+5])[0])

    return monkeys


def get_monkey_business(data: dict) -> int:
    business = []
    for k, v in data.items():
        business.append(v["business"])
    top_two = sorted(business)[-2:]
    return top_two[0]*top_two[1]


def get_monkey_n_rounds_managed(data: dict, rounds: int=20) -> int:
    while rounds > 0:
        for m in data.keys():
            data[m]["business"] =  data[m].get("business", 0)+len(data[m]["Starting item"])
            for item in data[m]["Starting item"]:
                num = item if data[m]["Operations"][1] is None else data[m]["Operations"][1]
                if data[m]["Operations"][0] == "*":
                    inspected = (item * num) // 3
                elif data[m]["Operations"][0] == "+":
                    inspected = (item + num) // 3
                if (inspected % data[m]["Test"]) == 0:
                    data[data[m]["true"]]["Starting item"].append(inspected)
                else:
                    data[data[m]["false"]]["Starting item"].append(inspected)
            data[m]["Starting item"] = []
        rounds -= 1    
    business = get_monkey_business(data.copy())

    return business


def get_manage_worry(data: dict) -> int:
    relief = 1
    for k, v in data.items():
        relief *= v["Test"]
    return relief


def get_monkey_n_rounds(data: dict, rounds: int=20) -> int:
    managed = get_manage_worry(data.copy())
    while rounds > 0:
        for m in data.keys():
            data[m]["business"] =  data[m].get("business", 0)+len(data[m]["Starting item"])
            for item in data[m]["Starting item"]:
                num = item if data[m]["Operations"][1] is None else data[m]["Operations"][1]
                if data[m]["Operations"][0] == "*":
                    inspected = (item * num) % managed
                elif data[m]["Operations"][0] == "+":
                    inspected = (item + num) % managed
                if (inspected % data[m]["Test"]) == 0:
                    data[data[m]["true"]]["Starting item"].append(inspected)
                else:
                    data[data[m]["false"]]["Starting item"].append(inspected)
            data[m]["Starting item"] = []
        rounds -= 1
    business = get_monkey_business(data.copy())
    return business


if __name__ == "__main__":
    file_name = "input/11_monkey_in_the_middle.csv"
    test_file_name = "input/11_monkey_in_the_middle_test.csv"

    test_data = read_file(test_file_name)
    test_preprocessed = preprocess_data([x for x in test_data.copy() if x!=""])
    assert get_monkey_n_rounds_managed(copy.deepcopy(test_preprocessed)) == 10605

    assert get_monkey_n_rounds(copy.deepcopy(test_preprocessed), 10_000) == 2713310158

    data = read_file(file_name)
    data_preprocessed = preprocess_data([x for x in data.copy() if x!=""])
    print(get_monkey_n_rounds_managed(copy.deepcopy(data_preprocessed)))

    print(get_monkey_n_rounds(copy.deepcopy(data_preprocessed), 10_000))

