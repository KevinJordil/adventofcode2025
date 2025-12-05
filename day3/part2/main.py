with open("input2.txt") as f:
    lines = f.readlines()

number_of_digits = 12
total = 0

for line in lines:
    line = line.strip()

    digits = [0] * number_of_digits

    for sequence_index in range(0, len(line)):
        current_digit = int(line[sequence_index])

        for digit_index in range(0, number_of_digits):
            #print("sequence_index", sequence_index, "must be smaller than", (len(line) - number_of_digits + digit_index + 1), "for digit", digit_index, "current", current_digit)
            # Be sure a complete chain can be done
            if digits[digit_index] < current_digit and sequence_index < (len(line) - number_of_digits + digit_index + 1):
                digits[digit_index] = current_digit
                # Reset the rest of digits
                digits[digit_index + 1:] = [0] * (len(digits) - digit_index + 1)
                break
    
    # Genetate number
    number = 0
    for i in range(number_of_digits):
        number = number * 10 + digits[i]

    print(number)
    total += number

print("total", total)