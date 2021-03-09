from generator import Generator
import random as ran

class Life(Generator):

    def __init__(self,width, height, limit,noise):
        super().__init__(width+1,height+1,0)
        self.generation = 0
        self.stagnant = False
        self.limit = limit
        self.noise = noise
        self.restart()



    #life RULES:
    #>6  - dead
    #4-6 - Stays the same
    #2-3   - becomes alive
    #<=1 - dead

    def life(self):
        self.generation += 1
        self.stagnant = True
        next = [[1 for j in range(self.width)] for i in range(self.height)]
        for i in range(1,self.height-1):
           # print()
            for j in range(1,self.width-1):
                sum = 0
                sum += self.map[i+1][j] #bottom
                sum += self.map[i-1][j] #top
                sum += self.map[i][j+1] #right
                sum += self.map[i][j-1] #lef
                sum += self.map[i+1][j+1] #bottom right
                sum += self.map[i+1][j-1] #bottom left
                sum += self.map[i-1][j+1] #top right
                sum += self.map[i-1][j-1] #top left
                #print(sum,sep="",end="")
                """if sum > 5 or sum <= 1:
                    next[i][j] = 0
                    self.stagnant = False
                elif sum >= 2 and sum < 4:
                    next[i][j] = 1
                    self.stagnant = False"""
                if sum >= 6:
                    next[i][j] = 1
                elif sum == 3:
                    next[i][j] = self.map[i][j]
                else:
                    next[i][j] = 0

        self.map = next

    def finished(self):
        return self.generation >= self.limit

    def restart(self):
        for i in range(1, self.height - 1):
            for j in range(1, self.width - 1):
                chance = ran.randint(0, 100)
                if chance >= self.noise:
                    self.map[i][j] = 0
                else:
                    self.map[i][j] = 1
        self.generation = 0

    def update(self):
        return super().updateSuper(["Generation: {}".format(self.generation)])

    def print(self):
        for i in range(0,self.height):
            for j in range(0,self.width):
                print(self.map[i][j], sep="",end="")
            print()