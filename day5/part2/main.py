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

    def __lt__(self, other):
        return self.start < other.start

    def __repr__(self):
        return f"{self.start}-{self.end}"

    def nbr(self):
        return self.end - self.start + 1


class Stock:

    def __init__(self):
        self.ranges = []
        self.size = 0

    def add_range(self, r):
        self.ranges.append(r)

    def concat_ranges(self):
        self.ranges = sorted(self.ranges)
        i = 0

        while i < len(self.ranges):
            if (i + 1) < len(self.ranges):
                _next = self.ranges[i + 1]
                _current = self.ranges[i]

                if _next.start <= _current.end:
                    if _next.end >= _current.end:
                        _current.end = _next.end
                        del self.ranges[i + 1]
                        i -= 1
                    elif _next.end <= _current.end:
                        del self.ranges[i + 1]
                        i -= 1

            i += 1


    def counter(self):
        counter = 0
        for r in self.ranges:
            counter += r.nbr()

        return counter


lines = [] 

with open("input2.txt", "r", encoding="utf-8") as f:
    for line_number, raw_line in enumerate(f, start=1):
        line = raw_line.rstrip("\n")
        lines.append(Range(line))


stock = Stock()

for r in lines:
    stock.add_range(r)

stock.concat_ranges()

#print(stock.ranges)
print(stock.counter())