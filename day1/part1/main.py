# open txt file and read lines
with open("input2.txt") as f:
    lines = f.readlines()

current_position = 50
zero_counter = 0

for line in lines:
    line = line.strip()
    
    # Extract first character
    direction = line[0]
    # Extract number (assuming it's an integer)
    number = int(line[1:])

    if direction == "R":
        current_position = (current_position + number) % 100
    elif direction == "L":
        current_position = (current_position - number) % 100

    if current_position == 0:
        zero_counter += 1

print("Final Position:", current_position)
print("Number of times at position 0:", zero_counter)



