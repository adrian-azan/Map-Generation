import random as ran
from rich.console import Console, ConsoleOptions, RenderResult
from rich.table import Table
from rich.text import Text
import time


class miner:
    def __init__(self,mine):
        self.maxEndurance = 500
        self.mine = mine
        self.endurance = 500
        self.size = 1
        self.Hx = 0
        self.Hy = 0
        self.ID = 1

    def reset(self, w, h):
        self.Hx = int(w / 2)
        self.Hy = int(h / 2)
        self.endurance = self.maxEndurance

        with open("reports\Miner Report " + str(self.ID) + ".txt", "w") as fout:
            console = Console(file=fout)
            console.print(self.mine.update())
        self.ID += 1

class generator:

    def __init__(self,width, height,goal):
        self.width = width
        self.height = height
        self.map = [[1 for j in range(width)] for i in range(height)]
        self.space = 0
        self.spaceGoal = goal
        self.Tom = miner(self)
        self.Tom.reset(self.width, self.height)


    def finished(self):
        if self.space >= self.spaceGoal:
            return True
        return False

    def stats(self):
        return

    def diffusion(self):
        change = False
        while self.space < self.spaceGoal and change == False:
            while self.Tom.endurance > 0 and change == False:
                direction = int(ran.randint(0, 4))
                #print(direction)
                if direction == 0 and self.Tom.Hx + self.Tom.size < self.width - 2:
                    self.Tom.Hx += self.Tom.size
                elif direction == 1 and self.Tom.Hy + self.Tom.size < self.height - 2:
                    self.Tom.Hy += self.Tom.size
                elif direction == 2 and self.Tom.Hx - self.Tom.size > 1:
                    self.Tom.Hx -= self.Tom.size
                elif direction == 3 and self.Tom.Hy - self.Tom.size > 1:
                    self.Tom.Hy -= self.Tom.size

                if self.map[self.Tom.Hy][self.Tom.Hx] == 1:
                    self.map[self.Tom.Hy][self.Tom.Hx] = 0
                    change = True
                    self.space += 1
                self.Tom.endurance -= 1

            if self.Tom.endurance <=0:

                self.Tom.reset(self.width,self.height)
        return self.map

    def update(self):
        table = Table()
        table.add_column("Map")
        table.add_column("Requirement")
        for row in range(self.height):
            output = ""
            for col in range(self.width):
                if self.map[row][col] == 1:
                    output += "#"
                elif self.map[row][col] == 0:
                    output += " "

            if (row == 0):
                table.add_row(output,"Space: {}/{}".format(self.space,self.spaceGoal))
            elif row == 1:
                table.add_row(output, "Miner ID: {}".format(self.Tom.ID))
            elif row == 2:
                table.add_row(output, "Endurance: {}/{}".format(self.Tom.endurance,self.Tom.maxEndurance))
            else:
                table.add_row(output,"")
        return table

    def __rich_console__(self, console: Console, options: ConsoleOptions) ->RenderResult:
        text = Text()
        """
        for row in range(self.height):
            for col in range(self.width):
                if self.map[row][col] == 1:
                    text.append("#")
                elif self.map[row][col] == 0:
                    text.append(" ")

           """
        text.append("Test")
        return text