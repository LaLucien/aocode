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

def find_length_of_sequence(blockFile, startj):
    num = blockFile[startj]
    length = 0
    for i in range(startj, -1, -1):
        if blockFile[i] != num:
            break
        length += 1
    return length

def find_space_for(blockFile, sequenceLength):
    for i in range(0, len(blockFile)):
        if blockFile[i] != ".":
            continue
        space = True
        if i + sequenceLength < len(blockFile) and blockFile[i] == "." and blockFile[i + sequenceLength -1 ] == ".":
            for j in range(i, i + sequenceLength - 1):
                if blockFile[j] != ".":
                    space = False
                    break
            if space:
                return i
    # no space
    return -1

def solve2(input):
    blockFile = generate_blocks(input)

    i = 0
    # j = len(blockFile) - 1
    currentFile = int(max(blockFile)) + 1
    for j in range(len(blockFile) -1, -1, -1):
        # idea
        # decreasej until not same number
        # find space
        # swap elements
        if blockFile[j] == "." or int(blockFile[j]) >= currentFile:
            continue
        
        currentFile = int(blockFile[j])
        sequenceLength = find_length_of_sequence(blockFile, j)
        spaceStartsAt = find_space_for(blockFile, sequenceLength)
        # no space anywere
        if spaceStartsAt < 0 or spaceStartsAt >= j:
            continue
        for k in range(0, sequenceLength):
            blockFile[[spaceStartsAt + k, j - k]] = blockFile[[j - k, spaceStartsAt + k]]
            print(blockFile)

        
    print(blockFile)
    checksum = 0 
    for i, num in enumerate(blockFile):
        if num == ".":
            continue
        checksum += i * int(num)


    return checksum




if __name__ == "__main__":
    input = getInput()
    print(solve1(input))
    print(solve2(input))
