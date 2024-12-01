import numpy as np

def getInput():
    with open("2024/1/input.txt") as file:
        lines = file.readlines()
    
    left = []
    right = []
    for line in lines:
        line = line.replace("\n", "")
        # print(line.split(" "))
        left.append(int(line.split(" ")[0]))
        right.append(int(line.split(" ")[3]))

    return np.array(left), np.array(right)



def solve1():
    left, right = getInput()
    left.sort()
    right.sort()

    totalDistance = 0
    for lnum, rnum in zip(left, right):
        totalDistance += abs(lnum - rnum)
    

    print(totalDistance)


def solve2():
    left, right = getInput()

    rightUnique, rightCounts = np.unique(right, return_counts=True)
    rightOccurences = dict(zip(rightUnique, rightCounts))

    similarity = 0
    for lnum in left:
         if lnum in rightOccurences:
            similarity += lnum * rightOccurences[lnum]
    

    print(similarity)


if __name__ == "__main__":
    # solve1()

    solve2()