import random

# This function generates random weights for 3 cargos with total weight 713 kg 
# and puts them in one list.
def generate_weights(total_weight):
    weights = []
    cargo1 = random.randint(1, total_weight - 2)
    cargo2 = random.randint(1, total_weight - 1)
    cargo3 = total_weight - cargo1 - cargo2
    
    weights.append(cargo1)
    weights.append(cargo2)
    weights.append(cargo3)
    return weights

# The function generates list of 3 random positions, so they are not equal
# because more than 1 cargo can not be in 1 position
def generate_positions():
    box_positions = [random.randint(1, 8) for _ in range(3)]
    if box_positions[0] == box_positions[1] or box_positions[1] == box_positions[2] or box_positions[0] == box_positions[2]:
        generate_positions()
    return box_positions

def compare_positions(positions1, positions2):
    true_count = 0
    for i in range(3):
        if positions1[i] == positions2[i]:
            true_count += 1
    if true_count == 3:
        return True
    else:
        return False 

# This is the main function of our program. It gets 3 positions from user
# until it gets the correct ones with cargos with total weight 713 kg.
def find_cargo():
    total_weight = 713
    box_weights = generate_weights(total_weight)
    box_positions = generate_positions()

    while True:
        # Two proof of operation prints that were used in the development of the program:
        #print("\nCurrent positions:", box_positions)
        #print("Total weight:", sum(box_weights), "kg")

        new_positions = []
        for i in range(3):
            kilometer = int(input(f'Enter the kilometer mark for box {i + 1}: '))
            new_positions.append(kilometer)

        if compare_positions(box_positions, new_positions) == True and (box_weights[0] + box_weights[1] + box_weights
        [2] == 713):
            print("\nCongratulations! You found all the boxes. Total weight is", total_weight)
            break
        else:
            print("Sorry, the cargo is not found or positions are not valid. Boxes are moving to new locations.")

            box_positions = generate_positions()

find_cargo()
