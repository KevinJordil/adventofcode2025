class Range:
    
    def __init__(self, string_range):
        range = string_range.strip().split("-")
        self.start = int(range[0])
        self.end = int(range[1])

    def in_range(self, number):
        if number >= self.start and number <= self.end:
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.start}-{self.end}"



second_part = False
ranges = [] 
items = []

with open("input2.txt", "r", encoding="utf-8") as f:
    for line_number, raw_line in enumerate(f, start=1):
        line = raw_line.rstrip("\n")
        if line == "":
            second_part = True
        else:
            if second_part:
                items.append(int(line))
            else:
                ranges.append(Range(line))


counter = 0

for item in items:
    for range in ranges:
        if range.in_range(item):
            counter += 1
            break


print(counter)