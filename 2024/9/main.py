import numpy as np

DAY = 9
FILE = "test.txt"

def getInput():

    
    with open(f"2024/{DAY}/{FILE}", "r") as file:
        line = file.readline()


    return line

def generate_blocks(input):
    isdot = False
    id = 0
    blockFile = []
    for c in input:
        if(isdot):
            for i in range(int(c)):
                blockFile.append(".")
            id += 1
            isdot = False
        else:
            for i in range(int(c)):
                blockFile.append(str(id))
            isdot = True
    return np.array(blockFile, dtype=str)


def solve1(input):
    blockFile = generate_blocks(input)
    
    i = 0
    j = len(blockFile) - 1
    while(i<j):
        if blockFile[i] == ".":
            blockFile[[i,j]] = blockFile[[j,i]]
            j -= 1
        else:
            i += 1
    
    checksum = 0
    for id, num in enumerate(blockFile):
        if num == ".":
            break
        checksum += id * int(num)
    return checksum



def solve2(input):
    blockFile = generate_blocks(input)

    i = 0
    j = len(blockFile) - 1
    while(i < len(blockFile)):
        # idea
        # decreasej until not same number
        # find space
        # swap elements



    return 




if __name__ == "__main__":
    input = getInput()
    print(solve1(input))
    print(solve2(input))
