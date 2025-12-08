grid = []

with open("input2.txt", "r") as f:
    for line in f:
        line = line.rstrip("\n")
        row = list(line)
        grid.append(row)

for row in grid:
    print(" ".join(row))

divided = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == "S":
            grid[row + 1][col] = "|"
            
        elif grid[row][col] == "^" and grid[row - 1][col] == "|":
                
            divided += 1
                
            if row + 1 < len(grid):
                if col - 1 >= 0 and grid[row + 1][col - 1] != "|":
                    grid[row + 1][col - 1] = "|"
                    
                if col + 1 < len(grid[row]) and grid[row + 1][col + 1] != "|":
                    grid[row + 1][col + 1] = "|"
                    

        elif grid[row][col] == "|":
            if row + 1 < len(grid) and grid[row + 1][col] == ".":
                grid[row + 1][col] = "|"
                
print("Result")
for row in grid:
    print(" ".join(row))

print(divided)