import numpy as np
import os
from numba import jit, njit, prange
NUMBER_OF_TIMES = 5


def read_input():
    lines = []
    print(os.getcwd)
    with open("2023/12/input.txt", "r") as file:
        lines = file.readlines()
    springs =  []
    groups = []

    for line in lines:
        line = line.replace("\n", "")
        sline = ""
        curren = []
        for i in range(NUMBER_OF_TIMES):
            sline += line.split(" ")[0]
            sline += '?'
            for group in line.split(" ")[1].split(","):
                curren.append(int(group))
        groups.append(np.array(curren))
        sline = sline[:-1]
        springs.append(np.array([c for c in sline]))

    return springs, groups

# @jit
# def is_valid(spr, group):
#     # print("validate: ", spr, str(group))
#     running_count = 0
#     curr_group = 0
#     all_groups = np.zeros_like(group)
#     for c in spr:
#         # if curr_group >= len(group):
#         #     return False
#         if c == '.' :
#             if curr_group < len(group) and group[curr_group] == running_count:
#                 all_groups[curr_group] = 1
#                 curr_group += 1
#                 running_count = 0
#                 continue
#             if curr_group < len(group) and running_count > 0 and group[curr_group] > running_count:
#                 return False
#             # Exception
#         elif c == '#':
#             running_count += 1
#             if curr_group >= len(group):
#                 return False
#             if running_count > group[curr_group]:
#                 return False
#             continue
#         # else:
#             # Exception
#     # return True
#     if spr[-1] == '#' and running_count == group[curr_group]:
#         all_groups[curr_group] = 1
#     if sum(all_groups) == len(group):
#         return True
#     return False
    

# @jit
# def count_permutations(spring_line, grouping, index):
#     if index == len(spring_line):
#         # print(spring_line, str(grouping)) 
#         if is_valid(spring_line, grouping):
#             # print("valid")
#             return 1
#         # print("invalid")
#         return 0
#     count = 0
#     if spring_line[index] == '?':
#         # spring_line = spring_line[:index] + '#' + spring_line[index + 1:]
#         spring_line[index] = '#'
#         count += count_permutations(np.copy(spring_line), grouping, index + 1)
#         # spring_line = spring_line[:index] + '.' + spring_line[index + 1:]
#         spring_line[index] = '.'

#         count += count_permutations(np.copy(spring_line), grouping, index + 1)
#     else:
#         count += count_permutations(np.copy(spring_line), grouping, index + 1)
#     return count


    

# @njit(parallel = True)
# def solve(springs, groups):
#     total_permutations = 0
#     for i in prange(len(springs)):
#         current_perm = count_permutations(springs[i], groups[i], 0)
#         print(f"The {i} line in the file has {current_perm}\n")
#         total_permutations += current_perm
        
#     return total_permutations



@jit(nopython=True)
def is_valid_better(spring, grouping):
    running_count = 0
    current_group = 0
    checked = np.zeros_like(grouping)
    for c in spring:
        if c == '?':
            return True
        if c == '.' and running_count:
            if running_count != grouping[current_group]:
                return False
            checked[current_group] = 1
            current_group += 1
            running_count = 0
            continue
        if c == '#':
            running_count += 1
            if len(grouping) <= current_group or running_count > grouping[current_group]:
                return False
    
    
    # if grouping[-1] != running_count or current_group != len(grouping):
    #     return False
    # return True
    if spring[-1] == '#' and running_count == grouping[current_group]:
        checked[current_group] = 1
    if sum(checked) == len(checked):
        return True
    return False



@jit(nopython = True)
def count_permutations_better(springs, grouping, index):
    # print("\n")
    # print(f"{index}, {springs}, {grouping}")
    # if index >= len(springs):
    #     if is_valid_better(np.copy(springs), grouping):
    #         print("counted")
    #         return 1
    #     return 0
    # print(f"validate {springs}")
    if not is_valid_better(springs, grouping):
        # print("Invalid")
        return 0
    if index == len(springs):
        # print("valid", springs, grouping)
        return 1
    # print("valid")
    if springs[index] != '?':
        return count_permutations_better(np.copy(springs), grouping, index + 1)
    
    count = 0
    springs[index] = '.'
    count += count_permutations_better(np.copy(springs), grouping, index + 1)
    springs[index] = '#' 
    count += count_permutations_better(np.copy(springs), grouping, index + 1) 
    return count
    




@njit(parallel = True)
def solve_better(springs, groups):
    total_permutations = 0
    for i in prange(len(springs)):
        
        current_perm = count_permutations_better(springs[i], groups[i], 0)
        total_permutations += current_perm
        print(f"The {i} line in the file has {current_perm} permutations\n")

    return total_permutations



def main():
    springs, groups = read_input()
    # res = solve(springs, groups)
    completed = 0
    res = solve_better(springs, groups)
    print("Final Result: ", res) #7307 ex1
    pass



if __name__ == "__main__":
    main()