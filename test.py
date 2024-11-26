import functions
grid = functions.generate_grid(4, 3)
adj_grid = functions.hex_adjacency_finder(grid, 1, 2)
test = functions.first_move(adj_grid)
print(grid)
print("_______________________")
print(adj_grid)
print("_______________________")
print(test)

[
[[0, 0], [1, 0], [2, 0]], 
[[0, 1], [1, 1], [2, 1]], 
[[0, 2], [1, 2], [2, 2]], 
[[0, 3], [1, 3], [2, 3]]
]
[    [[0, 1], [1, 1]], 
 [[0, 2], [1, 2], [2, 2]], 
     [[0, 3], [1, 3]]]

name = functions.generate_name()

print(name)


