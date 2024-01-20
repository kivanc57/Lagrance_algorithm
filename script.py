from matplotlib.pyplot import imshow, show
from numpy import array, reshape, sqrt, nan
from copy import deepcopy

# Step 1: Identify and replace ['.'] values with numerical ['0'] values
def enumerate_list(any_list):
    special_indexes = []

    if ['.'] in any_list:
        for i in range(len(any_list)):
            if any_list[i] == ['.']:
                # Replace ['.'] with 0
                any_list[i] = [0]
                special_indexes.append(i)
    return any_list, special_indexes

# Step 2: Perform Lagrance smoothing on adjacent numerical values
def set_lagrance(any_list, special_indexes=[]):
    new_list = deepcopy(any_list)
    square_root = int(len(any_list) ** 0.5)

    for i in special_indexes:
        total = []
        #Check the neighbours if they are not BORDERs and ZEROs,
        #If not, add to list 'total' to calculate later

        # Check left neighbour
        if i != 0 and i % square_root != 0 and any_list[i - 1][0] != 0:
            total.append(any_list[i - 1][0])

        # Check right neighbour
        if (i + 1) % square_root != 0 and any_list[i + 1][0] != 0:
            total.append(any_list[i + 1][0])

        # Check upper neighbour
        if square_root <= i and any_list[i - square_root][0] != 0:
            total.append(any_list[i - square_root][0])

        # Check lower neighbour
        if i + square_root < len(any_list) and any_list[i + square_root][0] != 0:
            total.append(any_list[i + square_root][0])

        # Replace the element by the sum divided by length and round it to one decimal
        new_list[i] = [round(sum(total) / len(total), 1)]

    return new_list, special_indexes

# Determine the shape based on the length of the data, visualize it
def make_image(data):
    side_length = int(sqrt(len(data)))
    
    data = reshape(data, (side_length, -1))

    if 0 in data:
        data[data == 0] = nan

    imshow(data, interpolation='none', cmap='viridis')
    show()


def main():
    my_list = [
        [5.0], [4.0], [4.0], [3.0],
        [2.0], ['.'], ['.'], [1.0],
        [1.0], ['.'], ['.'], [3.0],
        [3.0], [3.0], [2.0], [4.0]
    ]

    rendered_list, indexes = enumerate_list(my_list)
    print('The list is tidied up and rendered from ZEROs')

    for step in range(1, 100):  # Limit the number of steps to avoid infinite loop
        print(f'This is STEP: {step}')
        make_image(array(rendered_list))
        new_list, indexes = set_lagrance(any_list=rendered_list, special_indexes=indexes)

        if new_list == rendered_list:
            print(f'No more changes! Final STEP: {step}')
            break

        rendered_list = new_list

if __name__ == '__main__':
    main()