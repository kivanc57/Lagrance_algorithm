from matplotlib.pyplot import imshow, show
from numpy import reshape, copy, ma, allclose
from copy import deepcopy
from random import choices

#Step 1: Generate the game map
def get_map(side_length, missing_values):
    game_map = list()
    special_indexes = list()

    #Create the sides with random values between 1 and 9
    for _ in range(side_length):
        row = [float(value) for value in choices(range(1, side_length), k=side_length)]
        game_map.append(row)
    
    #Adjust missing values as 0s to the game map and store their values in special_indexes
    for _ in range(missing_values):
        i_coordinates = tuple(choices(range(side_length), k=2)) #Mutuability is not desired, convert list to tuple.
        game_map[i_coordinates[0]][i_coordinates[1]] = 0.0
        special_indexes.append(i_coordinates)
    return game_map, special_indexes


# Step 2: Perform Lagrance smoothing on adjacent numerical values
def set_lagrance(any_list, special_indexes):
    new_list = deepcopy(any_list)
    max_i = len(any_list)

    for i in special_indexes:
        total = []
        #Check the neighbours if they are not BORDERs and ZEROs,
        #If not, add to list 'total' to calculate later

        y, x = i[0], i[1]
        # Check left neighbour
        if (x != 0) and (x % max_i != 0) and (any_list[y][x-1] != 0):
            total.append(any_list[y][x-1])

        # Check right neighbour
        if ((x + 1) % max_i != 0) and (any_list[y][x+1] != 0):
            total.append(any_list[y][x+1])

        # Check upper neighbour
        if (y != 0) and any_list[y-1][x] != 0:
            total.append(any_list[y-1][x])

        # Check lower neighbour
        if (y + 1 !=  max_i) and any_list[y+1][x] != 0:
            total.append(any_list[y+1][x])

        # Replace the element by the sum divided by length and round it to one decimal
        if len(total) > 0:
            new_list[y][x] = round(sum(total) / len(total), 1)

    return new_list, special_indexes

# Step 3: Visualize it
def make_image(data):
    data = copy(data)
    data = reshape(data, (len(data), len(data)))

    # Set custom color for 0.0s to white
    cmap = 'viridis'
    data[data == 0.0] = float('nan')

    # Use masked array to ignore nan values during colormap normalization
    masked_data = ma.masked_where(ma.getmask(data), data)

    imshow(masked_data, interpolation='none', cmap=cmap)
    show()


def main():
    random_map, indexes = get_map(side_length=4, missing_values=4)
    make_image(random_map) #Visualize the first map with missing values
    tolerance = 1e-2 #Tolerance limit to set precision
    step_limit = len(indexes) * 4 + 1
    for step in range(1, step_limit):  # Limit the number of steps to avoid infinite loop
        print(f'This is STEP: {step}')
        new_map, indexes = set_lagrance(any_list=random_map, special_indexes=indexes)
        make_image(new_map) #Visualize current map
        # Check if the arrays are almost equal (within a small tolerance)
        if allclose(new_map, random_map, atol=tolerance):
            print(f'No more changes! Final STEP: {step}')
            break

        random_map = new_map

if __name__ == '__main__':
    main()
