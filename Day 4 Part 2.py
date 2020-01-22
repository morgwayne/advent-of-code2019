# -- Day 4: Secure Container --
# -- Part Two --

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
            if current_number[0] == current_number[1] and current_number[0] == current_number[2] and current_number[0] == current_number[3] and current_number[0] != current_number[4] and current_number[4] == current_number[5]:
                c = True
                break

            # Handles index out of range errors that shouldn't matter
            try:
                # Different algorithms depending on if we're analyzing the end of the number string, or the beginning.
                if 0 < num < 5:
                    if current_number[num] == current_number[num + 1] and current_number[num + 1] != current_number[num + 2] and current_number[num + 1] != current_number[num - 1]:  # Checks for at least one duplicate in adjacent numbers
                        c = True
                        break
                    else:
                        c = False

                # End of string algorithm
                elif num == 5:
                    if current_number[num] == current_number[num - 1] and current_number[num] != current_number[num - 2]:  # Checks for at least one duplicate in adjacent numbers
                        c = True
                        break
                    else:
                        c = False

                # Beginning of string algorithm
                else:
                    if current_number[num] == current_number[num + 1]:
                        if current_number[num + 1] != current_number[num + 2]:
                            if current_number[num + 2] != current_number[num]:
                                c = True
                                break
                    else:
                        c = False

            except IndexError:
                continue

        # Checks for constant increase in adjacent numbers
        if c:
            for num in range(len(current_number)):
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
            # Using a set here, for some reason using a list appends each number twice, not really sure why honestly.
            # Sets are better anyway.
            matches.add(current_number)
    # Returns the number of numbers that passed the rule checks
    return matches


print(len(iterate()))