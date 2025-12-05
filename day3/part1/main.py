with open("input2.txt") as f:
    lines = f.readlines()

first_biggest_digit = 0
second_biggest_digit = 0

total = 0

for line in lines:
    first_biggest_digit = int(line[0])
    must_assign_second = 1

    for i in range(1, len(line) - 1):
        number = int(line[i])
        #print("first:", first_biggest_digit, "second", second_biggest_digit, "number", number, "must_assign_second", must_assign_second)

        if first_biggest_digit < number and i < len(line) - 2:    
            first_biggest_digit = number
            second_biggest_digit = 0

        elif second_biggest_digit < number:
            second_biggest_digit = number
        
    
    number = ((10 * int(first_biggest_digit)) + int(second_biggest_digit))
    print(number)
    total += number
    first_biggest_digit = 0
    second_biggest_digit = 0

print("total", total)