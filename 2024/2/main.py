import numpy as np
from numba import jit, njit, prange

def getInput():

    input = []
    with open("2024/2/input.txt", "r") as file:
        lines = file.readlines()
    
    for line in lines:
        line = line.replace("\n","")
        input.append(np.array(line.split(" "), dtype=int))
    

    return input


def correctMargin(num1, num2):
    return abs(num1 - num2) >= 1 and abs(num1 - num2) <= 3

def solve1():
    input = getInput()

    valid = 0
    for line in input:
        lineIsValid = True
        if line[0] < line[1]:
            isIncreasing = True
        elif line[0] > line[1]:
            isIncreasing = False
        else:
            continue

        for i in range(len(line)-1):
            if (line[i] < line[i+1]) and isIncreasing and correctMargin(line[i], line[i+1]):
                continue
            if(line[i] > line[i+1]) and not isIncreasing and correctMargin(line[i], line[i+1]):
                continue
            lineIsValid = False
            break

        if(lineIsValid):
            valid += 1
    

    return valid


def checkIncreasing(line):
    for i in range(len(line)-1):
            if (line[i] < line[i+1])and correctMargin(line[i], line[i+1]):
                continue
            return i
    return -1
    
def checkDecreasing(line):
    for i in range(len(line)-1):
            if (line[i] > line[i+1]) and correctMargin(line[i], line[i+1]):
                continue
            return i
    return -1

def solve2():
    input = getInput()
    valid = 0
    for line in input:
        indexInc = checkIncreasing(line)
        indexDec = checkDecreasing(line)
        if indexInc == -1 or indexDec == -1:
            valid += 1
            continue
        if indexInc != -1 and -1 == checkIncreasing(np.concatenate((line[0:indexInc], line[indexInc + 1:]))):
            valid += 1
            continue
        if indexDec != -1 and -1 == checkDecreasing(np.concatenate((line[0:indexDec], line[indexDec + 1:]))):
            valid += 1
            continue

    return valid



            

if __name__ == "__main__":
    # print(solve1())
    print(solve2())