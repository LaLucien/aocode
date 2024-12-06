import numpy as np

DAY = 6
FILE = "test.txt"

def getInput():

    
    with open(f"2024/{DAY}/{FILE}", "r") as file:
        input = np.array([np.array([c for c in line.strip()], dtype=str)  for line in file.readlines()])


    
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i,j] == "^" :
                 input[i,j] = "."
                 
                 return (input, (i,j))
                

    
    

def solve1(input):

    return 



def solve2(input):


    return 




if __name__ == "__main__":
    input = getInput()
    print(solve1(input))
    print(solve2(input))
