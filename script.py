import copy
import random


def laplace(any_list):
    new_list = copy.deepcopy(any_list)
    square_root = int(len(any_list) ** 0.5)
    special_indexes = []

    # Step 1: Identify and replace ['.'] values with numerical values
    for i in range(len(any_list)):
        if any_list[i] == ['.']:
            # Replace ['.'] with 0
            new_list[i] = [0]
            special_indexes.append(i)

    # Step 2: Perform Laplace smoothing on adjacent numerical values
    while True:
        for i in special_indexes:
            neighbour_list = [0, 0, 0, 0]
            neighbour_amount = 0
            total = 0
                
            #Check if the left neighbour is available
            if i != 0:
                if i % square_root != 0:
                    if any_list[i - 1] != ['.']:
                        neighbour_list[0] = any_list[i - 1][0]
                        total += any_list[i - 1][0]
                        neighbour_amount += 1

            ##Check if the right neighbour is available
            if (i + 1) % square_root != 0:
                if any_list[i + 1] != ['.']:
                    neighbour_list[1] = any_list[i + 1][0]
                    total += any_list[i + 1][0]
                    neighbour_amount += 1

            #Check if the upper neighbour is available
            if square_root <= i:
                if any_list[i - square_root] != ['.']:
                    neighbour_list[2] = any_list[ i - square_root ][0]
                    total += any_list[ i - square_root ][0]
                    neighbour_amount += 1
                    
            ##Check if the lower neighbour is available
            if i + square_root < len(any_list):
                if any_list[i + square_root] != ['.']:
                    neighbour_list[3] = any_list[ i + square_root][0]
                    total += any_list[ i + square_root][0]
                    neighbour_amount += 1

            #Replace the element by the total / neighbour_amount and round it to have one decimal
            new_list[i] = [round(total / neighbour_amount, 2)]




        

def main():
    my_list = [
    [5.0], [4.0], [4.0], [3.0],
    [2.0], ['.'], ['.'], [1.0],
    [1.0], ['.'], ['.'], [3.0],
    [3.0], [3.0], [2.0], [4.0]
    ]

    given_row_col = 10
    #Later get the number with user input() and generate the list randomly

    laplace(my_list)


if __name__ == '__main__':
    main()