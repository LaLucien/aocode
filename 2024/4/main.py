import numpy as np

def getInput():

    
    with open("2024/4/input.txt", "r") as file:
        lines = file.readlines()
    
    input = []
    for line in lines:
        # line = line.replace("\n", "")
        input.append(np.array([c for c in line if c.isalpha()], dtype=str))
    
    return np.array(input)



def solve1(input):
    """really shitty but works"""
    xmasCount = 0
    linelengt = len(input[0])
    for i in range(len(input)):
        for j in range(linelengt):
            if input[i,j] == 'X':
                Right = True
                RightDown = True
                Down = True
                LeftDown = True
                Left  = True
                LeftUp  = True
                Up = True
                RightUp = True
                for offset, c in enumerate("XMAS"):
                    #right
                    if j + offset >= linelengt or input[i, j+offset] != c:
                        Right = False
                    #left
                    if j - offset < 0 or input[i, j-offset] != c:
                        Left = False
                    #Up
                    if i - offset < 0 or input[i-offset, j] != c:
                        Up = False
                    #Down
                    if i + offset >= len(input) or input[i+offset, j] != c:
                        Down = False
                    #RightUp
                    if i - offset < 0 or j + offset >= linelengt  or input[i-offset, j+offset] != c:
                        RightUp = False
                    #RightDown
                    if i + offset >= len(input) or j + offset >= linelengt or  input[i+offset, j+offset] != c:
                        RightDown = False
                    #LeftDown
                    if i + offset >= len(input) or j - offset < 0 or  input[i+offset, j-offset] != c:
                        LeftDown = False
                    #LeftUp
                    if i - offset < 0 or j - offset < 0 or input[i-offset, j-offset] != c:
                        LeftUp = False

                if Up:
                    xmasCount += 1
                if LeftUp:
                    xmasCount += 1
                if Left:
                    xmasCount += 1
                if LeftDown:
                    xmasCount += 1
                if Down:
                    xmasCount += 1
                if RightDown:
                    xmasCount += 1
                if Right:
                    xmasCount += 1
                if RightUp:
                    xmasCount += 1
                    
    return xmasCount
    



def solve2(input):
    xmasCount = 0
    debug = np.zeros_like(input)

    linelengt = len(input[0])
    for i in range(1, len(input) -1):
        for j in range(1, linelengt-1):
            # if (input[i-1,j-1] == 'M' and input[i-1, j+1] == 'S' and
            #                     input[i,j] == 'A' and
            #     input[i+1, j] == 'M' and input[i+1, j+1] == 'S'):
            #     xmasCount += 1
            if input[i,j] != 'A':
                continue
            if (((input[i-1,j-1] == 'M' and input[i+1, j+1] == 'S') or
                (input[i-1,j-1] == 'S' and input[i+1, j+1] == 'M')) and
                ((input[i+1,j-1] == 'M' and input[i-1, j+1] == 'S') or
                (input[i+1,j-1] == 'S' and input[i-1, j+1] == 'M'))):
                
                xmasCount += 1



    return  xmasCount




if __name__ == "__main__":
    input = getInput()

    print(solve1(input))
       

    print(solve2(input))
