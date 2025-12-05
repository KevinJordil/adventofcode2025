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


class Stock:

    def __init__(self):
        self.stock = []
        self.size = 0

    def add_range(self, r):
        self.adapt_array_size(r.end)
        for i in range(r.start, r.end + 1):
            self.stock[i] = 1
    
    def adapt_array_size(self, end):
        if end >= self.size:
            size_to_add = end - self.size + 1
            #print("end", end, "size", self.size, "size_to_add", size_to_add)
            self.stock += [0] * size_to_add
            self.size += size_to_add

    def counter(self):
        return self.stock.count(1)


ranges = [] 

with open("input2.txt", "r", encoding="utf-8") as f:
    for line_number, raw_line in enumerate(f, start=1):
        line = raw_line.rstrip("\n")
        ranges.append(Range(line))


stock = Stock()

for r in ranges:
    stock.add_range(r)


#print(stock.stock)
print(stock.counter())