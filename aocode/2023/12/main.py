import numpy as np


def read_input():
    lines = []
    with open("input.txt", "r") as file:
        lines = file.readlines()
    springs =  []
    groups = []

    for line in lines:
        line = line.replace("\n", "")
        springs.append(line.split(" ")[0])
        curren = []
        for group in line.split(" ")[1].split(","):
            curren.append(int(group))
        groups.append(curren)

    return springs, groups


def is_valid(spr, group):
    print("validate: ", spr, str(group))
    running_count = 0
    curr_group = 0
    all_groups = np.zeros_like(group)
    for c in spr:
        # if curr_group >= len(group):
        #     return False
        if c == '.' :
            if curr_group < len(group) and group[curr_group] == running_count:
                all_groups[curr_group] = 1
                curr_group += 1
                running_count = 0
                continue
            if curr_group < len(group) and running_count > 0 and group[curr_group] > running_count:
                return False
            # Exception
        elif c == '#':
            if curr_group >= len(group):
                return False
            if running_count > group[curr_group]:
                return False
            running_count += 1
            continue
        # else:
            # Exception
    # return True
    if spr[-1] == '#' and running_count == group[curr_group]:
        all_groups[curr_group] = 1
    if sum(all_groups) == len(group):
        return True
    return False
    
        

        



def count_permutations(spring_line, grouping, index):
    if index == len(spring_line):
        # print(spring_line, str(grouping))
        if is_valid(spring_line, grouping):
            print("valid")
            return 1
        print("invalid")
        return 0
    count = 0
    if spring_line[index] == '?':
        spring_line = spring_line[:index] + '#' + spring_line[index + 1:]
        count += count_permutations(spring_line, grouping, index + 1)
        spring_line = spring_line[:index] + '.' + spring_line[index + 1:]

        count += count_permutations(spring_line, grouping, index + 1)
    else:
        count += count_permutations(spring_line, grouping, index + 1)
    return count


    


def solve(springs, groups):
    total_permutations = 0
    for i in range(len(springs)):
        current_perm = count_permutations(springs[i], groups[i], 0)
        print(current_perm, "\n")
        total_permutations += current_perm
    return total_permutations

def main():
    springs, groups = read_input()
    res = solve(springs, groups)
    print("Final Result: ", res) #7307
    pass



if __name__ == "__main__":
    main()