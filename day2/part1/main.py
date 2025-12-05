with open("input2.txt") as f:
    lines = f.readlines()


sum = 0

# All data are on first line
# split with comma
ranges = lines[0].strip().split(",")

for r in ranges:
    start, end = r.split("-")
    #print(f"Start: {start}, End: {end}")
    for i in range(int(start), int(end) + 1):
        # Count digits
        digit_count = len(str(i))
        # Check if first part and last part have same digits
        if digit_count % 2 == 0:
            first_half = str(i)[:digit_count // 2]
            second_half = str(i)[digit_count // 2:]
            if first_half == second_half:
                #print(f"Matching number found: {i}")
                sum += i

print("Total matching numbers:", sum)