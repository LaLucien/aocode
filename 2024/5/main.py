import numpy as np

DAY = 5
FILE = "input.txt"

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
                num.append(int(cnum))
            printingInput.append(np.array(num))
        else:
            left, right = int(line.split("|")[0]), int(line.split("|")[1])
            if left in beforeOrdering.keys():
                beforeOrdering[left].append(right)
            else:
                beforeOrdering[left] = [right]
            

    return (beforeOrdering, printingInput)

def solve1(input):
    ordering = input[0]
    printing = input[1]

    validPrintsMiddleSum = 0
    incorectlyOrder = []
    for print in printing:
        alreadyPrinted = []
        isValid = True
        for i in range(len(print)):
            currentPage = print[i]
            # if not in ordering doesnt matter
            if not (currentPage in ordering.keys()):
                alreadyPrinted.append(currentPage)
                continue
            

            for mustComeAfter in ordering[currentPage]:
                if mustComeAfter in alreadyPrinted:
                    isValid = False
                    incorectlyOrder.append(print)
                    break

            if not isValid:
                break


            # alreadyPrinted += ordering[currentPage]
            alreadyPrinted.append(currentPage)
        
        if isValid:
            validPrintsMiddleSum += print[int(len(print)/2)]

            



    return validPrintsMiddleSum, incorectlyOrder



def solve2(input):
    ordering = input[0]
    # printing = input[1]
    dontCare, wrongPrints = solve1(input)

    middleSum = 0
    # insertion sort
    for print in wrongPrints:
        i = 1
        while i < len(print):
            j = i
            # inserts elements that have no rules at end, inserts other where to be sorted page doesnt need to be after.
            while j > 0 and print[j] in ordering.keys() and print[j-1] in ordering[print[j]]:
                tmp = print[j]
                print[j] = print[j-1]
                print[j-1] = tmp
                j -=1
            i += 1
    
        middleSum += print[int(len(print)/2)]
            
    return middleSum




if __name__ == "__main__":
    input = getInput()
    print(solve1(input))
    print(solve2(input))
