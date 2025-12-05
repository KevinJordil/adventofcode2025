class Dial:
    
    def __init__(self, starting_position=0):
        self.position = starting_position
        self.crossing_zero_counter = 0

    def rotate(self, direction, number):
        if direction == "R":
            crossing_zero_passes = (self.position + number) // 100

            self.position = (self.position + number) % 100

        elif direction == "L":
            flipped_position = (100 - self.position) % 100
            crossing_zero_passes = (flipped_position + number) // 100
            
            self.position = (self.position - number) % 100

        self.crossing_zero_counter += crossing_zero_passes

    def crossing_zero(self):
        return self.crossing_zero_counter




# open txt file and read lines
with open("input2.txt") as f:
    lines = f.readlines()

dial = Dial(starting_position=50)

for line in lines:
    line = line.strip()
    
    # Extract first character
    direction = line[0]
    # Extract number (assuming it's an integer)
    number = int(line[1:])

    dial.rotate(direction, number)

print("Number of times at position 0:", dial.crossing_zero())