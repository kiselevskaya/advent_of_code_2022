

def get_first_start_of_packet(buffer: str, subsequence: int) -> int:
    buffer = list(buffer)
    for i in range(len(buffer)):
        if len(set(buffer[i:i+subsequence])) < subsequence:
            continue
        else:
            return i+subsequence


if __name__ == "__main__":
    with open("input/06_tuning_trouble.csv", "r") as file:
        buffer = file.readline().replace("\n","")
    
    test_data = [
        "bvwbjplbgvbhsrlpgdmjqwftvncz", 
        "nppdvjthqldpwncqszvftbrmjlhg",
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw",
        "mjqjpqmgbljsphdztnvjfqwrcgsmlb",
        "bvwbjplbgvbhsrlpgdmjqwftvncz",
        "nppdvjthqldpwncqszvftbrmjlhg",
        "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg",
        "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"]
    
    assert get_first_start_of_packet(test_data[0], 4) == 5
    assert get_first_start_of_packet(test_data[1], 4) == 6
    assert get_first_start_of_packet(test_data[2], 4) == 10
    assert get_first_start_of_packet(test_data[3], 4) == 11

    assert get_first_start_of_packet(test_data[4], 14) == 19
    assert get_first_start_of_packet(test_data[5], 14) == 23
    assert get_first_start_of_packet(test_data[6], 14) == 23
    assert get_first_start_of_packet(test_data[7], 14) == 29
    assert get_first_start_of_packet(test_data[8], 14) == 26

    print(get_first_start_of_packet(buffer, 4))
    print(get_first_start_of_packet(buffer, 14))
