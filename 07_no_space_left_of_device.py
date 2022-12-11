

import re
import queue


def get_dir_size(q: queue, filesystem: dict={}, dir: str=""):
    while not q.empty():
        command = q.get()
        # open folder
        if re.match(r"\$ cd [a-zA-Z/]+", command):
            files_size = get_dir_size(q, filesystem, f'{dir}\{command.split(" ")[-1]}')
            if dir != "":
                filesystem[dir] = filesystem.get(dir, 0) + files_size
            else:
                return filesystem
        # add file size
        elif re.match(r"\d+ .*", command):
            if dir not in filesystem:
                filesystem[dir] = int(command.split(" ")[0])
            else:
                filesystem[dir] += int(command.split(" ")[0])
        # back to previous folder
        elif re.match(r"\$ cd \.\.", command):
            return filesystem.get(dir, 0)
    return filesystem.get(dir, 0)
        

if __name__ == "__main__":
    with open("input/07_no_space_left_of_device.csv", "r") as file:
        terminal = file.read().splitlines()

    test_data = [
        "$ cd /",
        "$ ls",
        "dir a",
        "14848514 b.txt",
        "8504156 c.dat",
        "dir d",
        "$ cd a",
        "$ ls",
        "dir e",
        "29116 f",
        "2557 g",
        "62596 h.lst",
        "$ cd e",
        "$ ls",
        "584 i",
        "$ cd ..",
        "$ cd ..",
        "$ cd d",
        "$ ls",
        "4060174 j",
        "8033020 d.log",
        "5626152 d.ext",
        "7214296 k"]

    # test_q = queue.Queue()
    # for i in test_data:
    #     test_q.put(i)
    # test_result = get_dir_size(test_q)

    # assert sum([v for v in test_result.values() if v <= 100_000]) == 95437

    q = queue.Queue()
    for j in terminal:
        q.put(j)
    result = get_dir_size(q)

    # 1517599
    result_copy = result.copy()
    print(f"\033[032msum of folders size under 100k {sum([v for v in result_copy.values() if v < 100_000])}")

    root = """\\/"""
    requered_space = result[root]-40_000_000
    print(f"\033[032mrequared space to free {requered_space}")

    folders_size = sorted(result.copy().values())
    print(folders_size)
    for i in folders_size:
        if i < requered_space:
            continue
        else:
            print(i)
            break