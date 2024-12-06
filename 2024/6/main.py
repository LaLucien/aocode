import numpy as np

DAY = 6
FILE = "input.txt"

def getInput():

    
    with open(f"2024/{DAY}/{FILE}", "r") as file:
        input = np.array([np.array([c for c in line.strip()], dtype=str)  for line in file.readlines()])


    
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i,j] == "^" :
                 input[i,j] = "."
                 return (input, np.array([i,j]))
                

    
    

def solve1(input):
    floor = input[0]
    guardPosition = input[1]
    visited = []
    guardDirectionIndex = 0
    guardDirections = (np.array([-1,0]),np.array([0,1]),np.array([1,0]),np.array([0,-1]))
    

    while(True):
        visited.append(guardPosition)
        # outside check
        if( np.any(np.less(guardPosition + guardDirections[guardDirectionIndex], np.array([0,0]))) or
            np.any(np.greater(guardPosition + guardDirections[guardDirectionIndex], np.array([len(floor) -1, len(floor[0]) -1])))):
            break
        
        # wall check
        if(floor[np.add(guardPosition, guardDirections[guardDirectionIndex])[0], 
                    np.add(guardPosition, guardDirections[guardDirectionIndex])[1]] == "#"):
            guardDirectionIndex = (guardDirectionIndex + 1) % 4
        else:
            guardPosition = np.add(guardPosition, guardDirections[guardDirectionIndex])
        
        

    return len(np.unique(visited, axis=0))



def solve2(input):


    return 




if __name__ == "__main__":
    input = getInput()
    print(solve1(input))
    print(solve2(input))
