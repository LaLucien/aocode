import re

def getInput():

    input = []
    with open("2024/3/test.txt", "r") as file:
        lines = file.readlines()


    return lines

def solve1(input):
    sume = 0
    for line in input:
        matches = re.findall(r'mul\(\d*,\d*\)',line )
        # print (matches)
        for match in matches:
            left, right = match.split(",")
            left = re.findall(r'\d*', left)[-2]
            right = re.findall(r'\d*', right)[0]
            print(left,"*", right)
            sume += int(left) * int(right)

    return sume



def solve2(input):
    sume = 0
    for line in input:
        line = line.sub(r'don\'t\(\).*do\(\)')
        matches = re.findall(r'mul\(\d*,\d*\)',line )
        print (matches)
        for match in matches:
            left, right = match.split(",")
            left = re.findall(r'\d*', left)[-2]
            right = re.findall(r'\d*', right)[0]
            print(left,"*", right)
            sume += int(left) * int(right)

    return sume




if __name__ == "__main__":
    input = getInput()

    # print(solve1(input))
    # 173419328

    print(solve2(input))