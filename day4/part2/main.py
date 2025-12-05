def getneighbors8(matrix, x, y, width, height):
    result = []

    for row_direction in (-1, 0, 1):

        for column_direction in (-1, 0, 1):

            if row_direction == 0 and column_direction == 0:
                continue

            row_selector = x + row_direction
            column_selector = y + column_direction

            if row_selector >= 0 and row_selector < width and column_selector >= 0 and column_selector < height:
                result.append(matrix[row_selector][column_selector])
        
    return result


input_matrix = []
result_matrix = []
max_adjacent = 3

with open("input2.txt", "r") as f:
    for line in f:
        row = list(line.rstrip("\n"))
        input_matrix.append(row)   

result_matrix = [row[:] for row in input_matrix]
height = len(input_matrix)
width = len(input_matrix[0])
sum = 0

while True:
    tmp_sum = sum
    for row in range(0, width):
        for col in range(0, height):
            if input_matrix[row][col] == '.':
                continue

            result = getneighbors8(input_matrix, row, col, width, height)
            #print("row", row, "col", col, "result", result)
            count_element = result.count('@')
            if count_element <= max_adjacent:
                #print("row", row, "col", col, "count", count_element)
                result_matrix[row][col] = '.'
                sum += 1

    input_matrix = [row[:] for row in result_matrix]
    if tmp_sum == sum:
        break

#print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in result_matrix]))
print("sum", sum)
