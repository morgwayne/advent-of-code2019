# -- Day 4: Secure Container --


# Range of numbers to check between
lowest = 402328
highest = 864247
change = highest - lowest

matches = set()


# Iterates through the range of the numbers and checks to see if it meets the rule requirmements
# Could probably be done better initializing each rule as a separate function

def iterate():
    for i in range(change):
        c = False
        current_number = str(lowest + i)
        for num in range(len(current_number)):
            try:
                if current_number[num] == current_number[num + 1]:  # Checks for at least one duplicate in adjacent numbers
                    c = True
                    break
                else:
                    c = False
            except IndexError:
                continue
        if c:
            for num in range(len(current_number)):  # Checks for constant increase in adjacent numbers
                try:
                    c = True
                    if int(current_number[num + 1]) < int(current_number[num]):
                        c = False
                        break
                    else:
                        c = True
                except IndexError:
                    pass
            if c:
                matches.add(current_number)
    return len(matches)  # Returns the number of numbers that passed the rule checks


print(iterate())
