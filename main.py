#main code
#use comments you dumbass 

#importing functions 
import functions
import random

#end importing

##player class
#add more to this lator 
class player:
    def __init__(self):
        #stats
        self.name = "name"
        self.is_dead = 1
        self.runCap = 0
        self.stamina = 0
        self.looking = -1
    #name set/get
    def set_name(self, name):
        self.name = f"{name}"

    def get_name(self):
        return(self.name)
    #dead set/get
    def set_motality(self, death):
        self.is_dead -= death
    
    def get_mortality(self):
        return(self.is_dead)
    #movment set/get
    def set_runcap(self, buff):
        self.runCap += buff

    def get_runcap(self):
        return(self.runCap)

    def move(self):
        if self.stamina > 0:
            self.stamina -= 1
        elif self.stamina == 0:
            return(0)
        elif self.stamina < 0:
            return(-1)
        #be careful with this   
    def set_stamina(self, buff):
        self.stamina = buff
        #____________________
    def get_stamina(self):
        return(self.stamina)

    def set_look(self, look_pos):
        if (look_pos  >= 0) and (look_pos <= 5):
            self.looking = look_pos
        else:
            print(f"bad look pos: {look_pos}")

    def get_look(self):
        return(self.looking)
            
#end classes

###main code
if __name__ == "__main__":
    #take inputs here
    with open("input.txt",  "r") as file:
        raw_input = []
        clener = []
        clean_input = {}
        for line in range(3):
            raw_input.append(file.readline().strip().split())
        for i in range(len(raw_input)):
            clener = raw_input[i][0].split(":")
            clean_input[clener[0]] = int(raw_input[i][1])
        height = clean_input["grid_height"]
        width = clean_input["grid_width"]



    grid = functions.generate_grid(height, width)
    with open("output.txt", "w") as file:
        display_grid = grid
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                for y in range(len(grid[i][j])):
                    if len(str(display_grid[i][j][y])) < (len(str(height)) or len(str(width))):
                        display_grid[i][j][y] = f"0{display_grid[i][j][y]}"
                    else:
                        display_grid[i][j][y] = f"{display_grid[i][j][y]}"

            temp_str = ""
            if (i % 2) != 0:
                temp_str = f"\t  {display_grid[i]}"
            else:
                temp_str = f"{display_grid[i]}"
            file.write(f"{temp_str} \n")
    #setting
    #player handling 
    amount_players = clean_input["num_characters"]
    player_dict = {}
    for i in range(amount_players):
        name = functions.generate_name()
        play = player()
        play.set_name(name)
        player_dict[name] = play
    with open("output.txt", "a") as file:
        read_players = list(player_dict.keys())
        
       
        for i in range(len(read_players)):
            #read_players[i] = read_players[i].strip()
            file.write(f"{read_players[i]}\n")
        print(read_players)