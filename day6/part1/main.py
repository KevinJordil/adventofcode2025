items = []

with open("input2.txt", "r", encoding="utf-8") as f:
    for line_number, raw_line in enumerate(f, start=1):
        line = raw_line.rstrip("\n")
        items.append(line.split())


operators = items.pop()
results = [int(x) for x in items[0]]

for row in range(1, len(items)):
    for col in range(0, len(items[row])):
        #print("row", row, "col", col, "operator", operators[col], "num", int(items[row][col]))
        if operators[col] == '*':
            results[col] *= int(items[row][col])
        elif operators[col] == '+':
            results[col] += int(items[row][col])
        



print(sum(results))