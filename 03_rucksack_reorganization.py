

import string


def get_common_item(rucksack_content: str) -> str:
    mid = len(rucksack_content)//2
    first_compartment = sorted(rucksack_content[:mid])
    second_compartment = sorted(rucksack_content[mid:])

    i, j = 0, 0
    while i < mid and j < mid:
        if first_compartment[i] == second_compartment[j]:
            return first_compartment[i]
        elif first_compartment[i] > second_compartment[j]:
            j += 1
        elif first_compartment[i] < second_compartment[j]:
            i += 1
        else:
            "Unexpected outcome"


def sum_of_priorities(rucksacks_content: list, priority: dict) -> int:
    total_sum = 0
    for i in rucksacks_content:
        share_item = get_common_item(i)
        total_sum += priority[share_item]
    return total_sum


def get_3_elf_group_badge(group_rucksacks: list) -> str:
    rucksack_1, rucksack_2, rucksack_3 = [sorted(rucksack) for rucksack in group_rucksacks]
    x, y, z = 0, 0, 0

    while x < len(rucksack_1) and y < len(rucksack_2) and z < len(rucksack_3):
        if rucksack_1[x] == rucksack_2[y] and rucksack_1[x] == rucksack_3[z]:
            return rucksack_1[x]
        max_item = max([rucksack_1[x], rucksack_2[y], rucksack_3[z]])
        if rucksack_1[x] < max_item:
            x += 1
        if rucksack_2[y] < max_item:
            y += 1
        if rucksack_3[z] < max_item:
            z += 1


def sum_of_badge_priorities(rucksacks_content: list, priority: dict) -> int:
    total_sum = 0
    for i in range(0, len(rucksacks_content), 3):
        badge = get_3_elf_group_badge(rucksacks_content[i:i+3])
        total_sum += priority[badge]
    return total_sum


if __name__ == "__main__":
    with open("input/03_rucksack_reorganization.csv", "r") as file:
        rucksacks_content = file.read().splitlines()
    
    alphabet = list(string.ascii_lowercase)+list(string.ascii_uppercase)
    priority = dict(zip(alphabet, list(range(1,53))))

    test_data = ["vJrwpWtwJgWrhcsFMMfFFhFp", 
        "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
        "PmmdzqPrVvPwwTWBwg",
        "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
        "ttgJtRGJQctTZtZT",
        "CrZsJsPPZsGzwwsLwLmpwMDw"]

    assert sum_of_priorities(test_data, priority) == 157

    print(sum_of_priorities(rucksacks_content, priority))

    assert get_3_elf_group_badge(test_data[:3]) == "r"
    
    assert get_3_elf_group_badge(test_data[3:]) == "Z"

    assert sum_of_badge_priorities(test_data, priority) == 70

    print(sum_of_badge_priorities(rucksacks_content, priority))
