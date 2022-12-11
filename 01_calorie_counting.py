

with open("input/01_calories_list.csv", "r") as file:
    elfs_list = file.read().splitlines()

top_three = [0, 0, 0]
max_calories = 0
current_elf_food = 0
for i in elfs_list:
    if i == "":
        if max_calories < current_elf_food:
            max_calories = current_elf_food
        if current_elf_food > any(top_three):
            top_three.append(current_elf_food)
            top_three = sorted(top_three)[1:]
        current_elf_food = 0
    else:
        current_elf_food += int(i)

print(f"Max calories carried by one elf: {max_calories}")
print(f"Sum of top three calories carried by one elfs: {sum(top_three)}")
