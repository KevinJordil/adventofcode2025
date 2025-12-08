grid = []

with open("input2.txt", "r") as f:
    for line in f:
        line = line.rstrip("\n")
        row = list(line)
        grid.append(row)

#for row in grid:
    #print(" ".join(row))

    
for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == "S":
            grid[row + 1][col] = "|"
            
        elif grid[row][col] == "^" and grid[row - 1][col] == "|":
            
            if col - 1 >= 0 and grid[row][col - 1] != "|":
                grid[row][col - 1] = "|"
                
            if col + 1 < len(grid[row]) and grid[row][col + 1] != "|":
                grid[row][col + 1] = "|"
                
                
            if row + 1 < len(grid):
                if col - 1 >= 0 and grid[row + 1][col - 1] != "|":
                    grid[row + 1][col - 1] = "|"
                    
                if col + 1 < len(grid[row]) and grid[row + 1][col + 1] != "|":
                    grid[row + 1][col + 1] = "|"
                    

        elif grid[row][col] == "|":
            if row + 1 < len(grid) and grid[row + 1][col] == ".":
                grid[row + 1][col] = "|"

s_pos_row = 0
s_pos_col = 0

for row in range(len(grid)):
    for col in range(len(grid[row])):
        if grid[row][col] == "^" and grid[row - 1][col] != "|":
            grid[row][col] = "."
        elif grid[row][col] == "S":
            s_pos_row = row
            s_pos_col = col
                


rows = len(grid)
cols = len(grid[0])
curr_rays = {s_pos_col: 1}

for row in range(s_pos_row, rows):
    next_rays = {}
    for col, weight in curr_rays.items():
        cell = grid[row][col]
        
        if cell in ['.', 'S', '|']:
            next_rays[col] = next_rays.get(col, 0) + weight
            
        elif cell == '^':
            left = col - 1
            if grid[row][left] == '|':
                next_rays[left] = next_rays.get(left, 0) + weight

            right = col + 1
            if grid[row][right] == '|':
                next_rays[right] = next_rays.get(right, 0) + weight

    curr_rays = next_rays

print("count:", sum(curr_rays.values()))
