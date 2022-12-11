

def read_file(file_name: str) -> list:
    with open(file_name, "r") as file:
        data = file.read().splitlines()
    return data


def get_signal_strength(cycles: list) -> int:
    cycle_count = 0
    signal_strength = []
    current_x = 1
    for i in cycles:
        n_cycles = 1 if i=="noop" else 2
        for n in range(n_cycles):
            cycle_count += 1
            if cycle_count == 20 or (cycle_count-20)%40 == 0:
                signal_strength.append(cycle_count * current_x)
            if n == 1:
                current_x += int(i.split()[1])

    return sum(signal_strength)


def get_canvas(cycles: list) -> list:
    cycle_count = 0
    canvas = []
    sprite = 1
    crt_row = ""
    pos = 0
    for i in cycles:
        n_cycles = 1 if i=="noop" else 2
        for n in range(n_cycles):
            cycle_count += 1   
            if pos in [sprite-1, sprite, sprite+1]:
                crt_row += "#"
            else:
                crt_row += "."
            pos += 1
            if cycle_count > 0 and cycle_count%40 == 0:
                canvas.append(crt_row)
                crt_row = ""
                pos = 0
            if n == 1:
                sprite += int(i.split()[1])
    return canvas


if __name__ == "__main__":
    file_name = "input/10_cathode_ray_tube.csv"
    test_file_name = "input/10_cathode_ray_tube_test.csv"

    test_data = read_file(test_file_name)
    assert get_signal_strength(test_data.copy()) == 13140

    ##..##..##..##..##..##..##..##..##..##..
    ###...###...###...###...###...###...###.
    ####....####....####....####....####....
    #####.....#####.....#####.....#####.....
    ######......######......######......####
    #######.......#######.......#######.....

    # for i in get_canvas(test_data.copy()):
    #     print(i)

    data = read_file(file_name)
    print(get_signal_strength(data.copy()))

    for i in get_canvas(data.copy()):
        print(i)
