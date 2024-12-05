import numpy as np

DAY = 5
FILE = "test.txt"

def getInput():
    with open(f"2024/{DAY}/{FILE}", "r") as file:
        lines = file.readlines()

    beforeOrdering = {}
    printingInput = []
    secondPartReached = False
    for line in lines:
        line = line.strip()
        if line == "":
            secondPartReached = True
            continue

        if secondPartReached:
            num = []
            for cnum in line.split(","):
                num.append(cnum)
            printingInput.append(np.array(num))
        else:
            left, right = int(line.split("|")[0]), int(line.split("|")[1])
            if left in beforeOrdering.keys():
                beforeOrdering[left].append(right)
            else:
                beforeOrdering[left] = [right]
            

    return beforeOrdering, printingInput

def solve1(input):

    return 



def solve2(input):


    return 




if __name__ == "__main__":
    input = getInput()
    print(solve1(input))
    print(solve2(input))
