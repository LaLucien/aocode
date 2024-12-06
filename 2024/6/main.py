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

def printFloor(floor):
    for row in floor:
        line = []
        for tile in row:
            line.append(np.array2string(tile))
        print(line)
        print("\n")

def solve2(input):
    defaultFloor = input[0]
    # guardPosition = input[1]
    initialGuartPosition = np.copy(input[1])
    # visited = []
    # guardDirectionIndex = 0
    guardDirections = (np.array([-1,0]),np.array([0,1]),np.array([1,0]),np.array([0,-1]))
    guardDirectionSymbol = ["u", "r", "d", "l"]

    possibleChanges = 0
    
    defaultFloor = np.array([np.array([np.array([c,"","","",""], dtype=str) for c in row]) for row in defaultFloor])
    # n2floor = []
    # for row in defaultFloor:
    #     n2row = []
    #     for c in row:
    #         n2row.append(np.array)


    
    for i in range(len(defaultFloor)):
        for j in range(len(defaultFloor[i])):
            print(i,j)
            if np.all(np.equal(defaultFloor[i,j], np.array(["#","","","",""]))) or np.all(np.equal(initialGuartPosition, np.array([i,j]))):
                continue
            floor = np.copy(defaultFloor)
            didntLeave = True
            floor[i,j,0] = "#"
            # visited = []
            guardDirectionIndex = 0
            guardPosition = np.copy(initialGuartPosition)

            # print("new floor")
            # printFloor(floor)
            while(True):
                # print("move")
                # visited.append(guardPosition)
                # print(floor[guardPosition[0], guardPosition[1]], guardDirections[guardDirectionIndex])

                # outside check
                if( np.any(np.less(np.add(guardPosition , guardDirections[guardDirectionIndex]), np.array([0,0]))) or
                    np.any(np.equal(np.add(guardPosition , guardDirections[guardDirectionIndex]), np.array([len(floor), len(floor[0])])))):
               
                    didntLeave = False
                    # print("moved out")
                    break
                # cycle check
                if guardDirectionSymbol[guardDirectionIndex] in floor[guardPosition[0], guardPosition[1]]:
                    # print("found cycle")
                    break
                
                floor[guardPosition[0], guardPosition[1],guardDirectionIndex + 1] = guardDirectionSymbol[guardDirectionIndex]
                
                # wall check
                if("#" in floor[np.add(guardPosition, guardDirections[guardDirectionIndex])[0], 
                            np.add(guardPosition, guardDirections[guardDirectionIndex])[1]]):
                    guardDirectionIndex = (guardDirectionIndex + 1) % 4
                else:
                    guardPosition = np.add(guardPosition, guardDirections[guardDirectionIndex])
                    
        
            # printFloor(floor)
            if didntLeave:
                
                possibleChanges += 1

    return possibleChanges

     




if __name__ == "__main__":
    input = getInput()
    # print(solve1(input))
    print(solve2(input))
