

import re


def sum_of_one_num_range_contain_another(data: list) -> int:
    count = 0
    for i in data:
        i = [int(x) for x in re.split(r',|-', i)]
        if (i[0]>=i[2] and i[1]<=i[3]) or (i[0]<=i[2] and i[1]>=i[3]):          
            count += 1
    return count


def sum_of_overlap_pairs(data: list) -> int:
    count = 0
    for i in data:
        i = [int(x) for x in re.split(r',|-', i)]         
        if (i[2]<=i[0]<=i[3]) or (i[3]>=i[1]>=i[2]):          
            count += 1
        elif (i[0]<=i[2]<=i[1]) or (i[1]>=i[3]>=i[0]):
            count += 1
    return count


if __name__ == "__main__":
    with open("input/04_camp_cleanup.csv", "r") as file:
        paired_ship_sections = file.read().splitlines()

    test_data = [
        '2-4,6-8', 
        '2-3,4-5',
        '5-7,7-9',
        '2-8,3-7',
        '6-6,4-6',
        '2-6,4-8']

    assert sum_of_one_num_range_contain_another(test_data)==2
    assert sum_of_overlap_pairs(test_data)==4

    print(sum_of_one_num_range_contain_another(paired_ship_sections))
    print(sum_of_overlap_pairs(paired_ship_sections))
