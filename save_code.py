#do not run this file
throw 


#save code for lator
po_moves = {}


for i in range(3):
    if i == 0:
        looking_left = (looking - 1)
        if looking_left == (-1):
            looking_left == 5 
        po_moves[i] = diretions[looking_left]
    elif i == 1:
        po_moves[i] = diretions[looking]
    elif i == 2:
        looking_right = looking + 1
        if looking_right == 6:
            looking_right = 0
        po_moves[i] = diretions[looking_right]
move = random.randint(1, 7)
if move <= 2:
    new_cords = po_moves[0]
elif (move >= 3) and (move <= 5):
    new_cords = po_moves[1]
elif move >= 7:
    new_cords = po_moves[2]
return(new_cords)
#-------------------------------
line_cont = len(file.readlines())
for i in range(0, line_cont, 2):
#-----------------------------------------
for i in range(len(raw_input)):
            for j in range(len(raw_input[i])):
                clener.append(raw_input[i][j].split())
        for i in range(0, len(raw_input), 2):
            clean_input[clener[i][0]] = "temp"
            print(i)

    

