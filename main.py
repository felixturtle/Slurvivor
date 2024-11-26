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
    #creating and showing a play grid
    with open("input.txt",  "r") as file:
        line_one = file.readline()
        line_one = line_one.split()
        hight = int(line_one[-1])
        line_two = file.readline()
        line_two = line_two.split()
        width = int(line_two[-1])
    grid = functions.generate_grid(hight, width)
    with open("output.txt", "w") as file:
        display_grid = grid
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                for y in range(len(grid[i][j])):
                    if len(str(display_grid[i][j][y])) < (len(str(hight)) or len(str(width))):
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
    
     