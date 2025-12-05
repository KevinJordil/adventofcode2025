with open("input.txt") as f:
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
        # Find if it made only of some sequence of digits repeated at least twice
        for seq_len in range(1, digit_count // 2 + 1):
            if digit_count % seq_len == 0:
                seq = str(i)[:seq_len]
                repeated_seq = seq * (digit_count // seq_len)
                if repeated_seq == str(i):
                    print(f"Matching number found: {i}")
                    sum += i
                    break
            

print("Total matching numbers:", sum)