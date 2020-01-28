# --- Day 5: Sunny with a Chance of Asteroids ---
# Part #2

# Initialize input and convert to integers
inp = []


# Resets input list to default
def refresh_input():
    global inp
    inp = []
    # string_input = '3,3,1105,-1,9,1101,0,0,12,4,12,99,1'
    string_input = '3,225,1,225,6,6,1100,1,238,225,104,0,1002,114,19,224,1001,224,-646,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1101,40,62,225,1101,60,38,225,1101,30,29,225,2,195,148,224,1001,224,-40,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1001,143,40,224,101,-125,224,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,101,29,139,224,1001,224,-99,224,4,224,1002,223,8,223,1001,224,2,224,1,224,223,223,1101,14,34,225,102,57,39,224,101,-3420,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1101,70,40,225,1102,85,69,225,1102,94,5,225,1,36,43,224,101,-92,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,1102,94,24,224,1001,224,-2256,224,4,224,102,8,223,223,1001,224,1,224,1,223,224,223,1102,8,13,225,1101,36,65,224,1001,224,-101,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,677,226,224,1002,223,2,223,1006,224,329,1001,223,1,223,1108,226,226,224,1002,223,2,223,1005,224,344,101,1,223,223,1108,226,677,224,1002,223,2,223,1006,224,359,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,374,101,1,223,223,1107,226,226,224,1002,223,2,223,1005,224,389,101,1,223,223,107,677,677,224,102,2,223,223,1006,224,404,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,419,101,1,223,223,108,677,226,224,1002,223,2,223,1006,224,434,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,449,101,1,223,223,1008,677,226,224,102,2,223,223,1006,224,464,1001,223,1,223,108,677,677,224,102,2,223,223,1005,224,479,101,1,223,223,7,677,677,224,102,2,223,223,1005,224,494,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,509,101,1,223,223,107,677,226,224,1002,223,2,223,1005,224,524,1001,223,1,223,7,677,226,224,1002,223,2,223,1005,224,539,1001,223,1,223,1007,226,677,224,1002,223,2,223,1005,224,554,1001,223,1,223,8,677,677,224,102,2,223,223,1006,224,569,101,1,223,223,7,226,677,224,102,2,223,223,1006,224,584,1001,223,1,223,1008,677,677,224,102,2,223,223,1005,224,599,101,1,223,223,1007,677,677,224,1002,223,2,223,1006,224,614,101,1,223,223,1107,677,226,224,1002,223,2,223,1006,224,629,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,659,1001,223,1,223,108,226,226,224,102,2,223,223,1006,224,674,101,1,223,223,4,223,99,226'
    string_input = string_input.split(',')
    for i in string_input:
        inp.append(int(i))


# Initialize input
refresh_input()


def intcode():
    refresh_input()
    position = 0
    while position < len(inp):
        # Convert opcode to string so we can determin
        # e immediate/position mode
        # This is necessary as ints cannot have preceding zeroes
        inp[position] = str(inp[position])

        # Add preceding zeroes to all opcodes to allow for consistent function
        while len(inp[position]) < 5:
            inp[position] = '0' + inp[position]

        # Adds parameters 1 and 2
        if inp[position][4] == '1':

            # Each if/else statement determines whether the given parameter is in immediate or position mode
            if inp[position][2] == '1':
                parameter_1 = int(inp[position + 1])
            else:
                parameter_1 = int(inp[inp[position + 1]])

            if inp[position][1] == '1':
                parameter_2 = int(inp[position + 2])
            else:
                parameter_2 = int(inp[inp[position + 2]])

            if inp[position][0] == '1':
                inp[position + 3] = parameter_1 + parameter_2
            else:
                inp[inp[position + 3]] = parameter_1 + parameter_2
            position += 4


        # Multiplies parameters 1 and 2
        elif inp[position][4] == '2':

            # Each if/else statement determines whether the given parameter is in immediate or position mode
            if inp[position][2] == '1':
                parameter_1 = int(inp[position + 1])
            else:
                parameter_1 = int(inp[inp[position + 1]])

            if inp[position][1] == '1':
                parameter_2 = int(inp[position + 2])
            else:
                parameter_2 = int(inp[inp[position + 2]])

            if inp[position][0] == '1':
                inp[position + 3] = parameter_1 * parameter_2
            else:
                inp[inp[position + 3]] = parameter_1 * parameter_2
            position += 4


        # Sets the parameter as user input
        elif inp[position][4] == '3':

            # Each if/else statement determines whether the given parameter is in immediate or position mode
            if inp[position][2] == '1':
                inp[position + 1] = int(input('input? >>> '))
            else:
                inp[inp[position + 1]] = int(input('input? >>> '))
            position += 2


        # Prints out the parameter's value
        elif inp[position][4] == '4':

            # Each if/else statement determines whether the given parameter is in immediate or position mode
            if inp[position][2] == '1':
                print(inp[position + 1])
            else:
                print(inp[inp[position + 1]])
            position += 2


        # changes the position variable to the second parameter if the first parameter is a non-zero
        elif inp[position][4] == '5':

            if inp[position][2] == '1':
                parameter_1 = inp[position + 1]
            else:
                parameter_1 = inp[inp[position + 1]]

            if inp[position][1] == '1':
                parameter_2 = inp[position + 2]
            else:
                parameter_2 = inp[inp[position + 2]]

            if parameter_1 != 0:
                position = parameter_2
            else:
                position += 3


        # changes the position variable to the second parameter if the first parameter is zero
        elif inp[position][4] == '6':

            if inp[position][2] == '1':
                parameter_1 = inp[position + 1]
            else:
                parameter_1 = inp[inp[position + 1]]

            if inp[position][1] == '1':
                parameter_2 = inp[position + 2]
            else:
                parameter_2 = inp[inp[position + 2]]

            if parameter_1 == 0:
                position = parameter_2
            else:
                position += 3


        # if first parameter less-than second, third parameter == 1, else third parameter == 0
        elif inp[position][4] == '7':

            if inp[position][2] == '1':
                parameter_1 = inp[position + 1]
            else:
                parameter_1 = inp[inp[position + 1]]

            if inp[position][1] == '1':
                parameter_2 = inp[position + 2]
            else:
                parameter_2 = inp[inp[position + 2]]

            if parameter_1 < parameter_2:
                if inp[position][0] == '1':
                    inp[position + 3] = 1
                else:
                    inp[inp[position + 3]] = 1
            else:
                if inp[position][0] == '1':
                    inp[position + 3] = 0
                else:
                    inp[inp[position + 3]] = 0
            position += 4


        # if first parameter equal to second, third parameter == 1, else third parameter == 0
        elif inp[position][4] == '8':

            if inp[position][2] == '1':
                parameter_1 = inp[position + 1]
            else:
                parameter_1 = inp[inp[position + 1]]

            if inp[position][1] == '1':
                parameter_2 = inp[position + 2]
            else:
                parameter_2 = inp[inp[position + 2]]

            if parameter_1 == parameter_2:
                if inp[position][0] == '1':
                    inp[position + 3] = 1
                else:
                    inp[inp[position + 3]] = 1
            else:
                if inp[position][0] == '1':
                    inp[position + 3] = 0
                else:
                    inp[inp[position + 3]] = 0
            position += 4


        # If opcode == '99', stop the program
        elif inp[position][4] == '9' and inp[position][3] == '9':
            break

        # If opcode doesn't match any other opcode, print this error
        else:
            print('Error! Invalid opcode.')
            break


intcode()

# Prevents python from immediately closing
input('end >>> ')
