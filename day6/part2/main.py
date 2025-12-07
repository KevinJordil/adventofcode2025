import operator

grid = []

with open("input2.txt", "r") as f:
    for line in f:
        line = line.rstrip("\n")
        row = list(line)
        grid.append(row)

# Transpose
grid = list(map(list, zip(*grid)))

numbers = []
results = []

for row in range(len(grid)):
    if grid[row][-1] == "*":
        op = operator.mul
    elif grid[row][-1] == "+":
        op = operator.add
        
    number = ""
    for col in range(len(grid[row]) - 1):
        number += grid[row][col]
        #print("number", number, "grid", grid[row][col])
        
    if row == (len(grid) - 1) or number.strip() != "":
        numbers.append(number)
    
    if number.strip() == "" or row == (len(grid) - 1):
        print(numbers)
        result = int(numbers[0])
        for i in range(1, len(numbers)):
            result = op(result, int(numbers[i]))
        results.append(result)
        numbers = []


print(sum(results))