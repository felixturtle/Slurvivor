
import random

def multi_append(*args):
    final = []
    for args in args:
        final.append(args)
    return(final)

def generate_grid(hight, width):
    final = []
    for i in range(hight):
        row = []
        for j in range(width):
            cord = [(j), (i)]
            row.append(cord)
        final.append(row)
    return(final)

def hex_adjacency_finder(grid, x, y):
    temp_grid = []
    for i in range(3):
        y_ind = y + (i - 1)
        row = []
        for j in range(3):
            x_ind = x + (j - 1)
            row.append(grid[y_ind][x_ind])
        temp_grid.append(row)
    if y % 2 == 1:
        temp_grid[0].pop(0)
        temp_grid[2].pop(0)
    elif y % 2 == 0:
        temp_grid[0].pop(2)
        temp_grid[2].pop(2)
    return(temp_grid)

def first_move(adj_grid):
    final = {}
    looking = random.randint(0, 5)
    diretions = {0:adj_grid[0][1], 1:adj_grid[1][2], 2:adj_grid[2][1], 3:adj_grid[2][0], 4:adj_grid[1][0], 5:adj_grid[0][0]}
    new_cords = diretions[looking]
    final["move"] = new_cords
    final["look_diretion"] = looking
    return(final)

def directions(adj_grid):
    direttions_grid = {0:adj_grid[0][1], 1:adj_grid[1][2], 2:adj_grid[2][1], 3:adj_grid[2][0], 4:adj_grid[1][0], 5:adj_grid[0][0]}
    return(direttions_grid)

def generate_name():
    first_list = []
    with open("first_names.txt", "r") as file:
        for i in file:
            first_list.append(i)
    last_list = []
    with open("last_names.txt", "r") as file:
        for i in file:
            last_list.append(i)
    first_ind = random.randint(0, (len(first_list)))
    last_ind = random.randint(0, (len(last_list)))
    name = f"{first_list[first_ind].strip()} {last_list[last_ind].strip()}"
    return(name)


