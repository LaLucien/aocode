import numpy as np
from numba import jit, njit, prange

DAY = 7
FILE = "test.txt"

def getInput():

    solutions = []
    equations = []
    with open(f"2024/{DAY}/{FILE}", "r") as file:
        lines = file.readlines()

    for line in lines:
        solutions.append(int(line.split(":")[0]))
        numbers = []
        for snum in line.strip().split(": ")[1].split(" "):
            numbers.append(int(snum))
        equations.append(np.array(numbers))
    
    return (np.array(solutions), equations)


def countPossibilities(sol, numbers, currentValue, currentIndex):
    # correct
    if (sol == currentValue and currentIndex >= len(numbers) - 1):
        return 1
    #overshoot, no more numbers
    if(sol < currentValue or currentIndex >=  len(numbers) - 1):
        return 0
    

    foundPossibilities = countPossibilities(sol, numbers, numbers[currentIndex] + numbers[currentIndex + 1], currentIndex + 1)
    return   foundPossibilities + countPossibilities(sol, numbers, numbers[currentIndex] * numbers[currentIndex + 1], currentIndex + 1) 
    

    


def solve1(input):
    solutions = input[0]
    equations = input[1]
    # operators = np.array(["+", "*"])

    rightPossibilities = 0

    for i in prange(len(solutions)):
        rightPossibilities += countPossibilities(solutions[i], equations[i],   equations[i][0] + equations[i][0 + 1], 1)
        rightPossibilities += countPossibilities(solutions[i], equations[i],   equations[i][0] * equations[i][0 + 1], 1)

    return rightPossibilities



def solve2(input):


    return 




if __name__ == "__main__":
    input = getInput()
    print(solve1(input))
    print(solve2(input))
