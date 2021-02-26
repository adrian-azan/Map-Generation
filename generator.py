import random as ran
import os.path
import time

from rich.console import Console, ConsoleOptions, RenderResult
from rich.table import Table
from rich.text import Text
from rich.live import Live
from rich.padding import Padding
from rich.box import Box
from rich import box
from rich.align import Align


class Miner:
    def __init__(self,mine,endurance,size):
        self.mine = mine
        self.maxEndurance = endurance
        self.endurance = endurance
        self.size = size
        self.X = 0
        self.Y = 0
        self.ID = 1

    def reset(self):
        self.endurance = self.maxEndurance
        self.ID += 1

    def pos(self,x,y):
        self.X = int(x)
        self.Y = int(y)



class Generator:
    def __init__(self,width, height,goal):
        self.width = width
        self.height = height
        self.map = [[1 for j in range(width)] for i in range(height)]
        self.space = 0
        self.spaceGoal = goal

    def finished(self):
        if self.space >= self.spaceGoal:
            return True
        return False

    def restart(self):
        self.map = [[1 for j in range(self.width)] for i in range(self.height)]
        self.space = 0


    def update(self):
        table = Table(box=box.SIMPLE)
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

        table.add_row(Padding("\n",1))
        return Align.center(table)

    def __rich_console__(self, console: Console, options: ConsoleOptions) ->RenderResult:
        output = Text()
        for row in range(self.height):
            for col in range(self.width):
                if self.map[row][col] == 1:
                    output += "#"
                elif self.map[row][col] == 0:
                    output += " "

            if (row == 0):
                output += "Space: {}/{}".format(self.space,self.spaceGoal)
            elif row == 1:
                output += "Miner ID: {}".format(self.Tom.ID)
            elif row == 2:
                output += "Endurance: {}/{}".format(self.Tom.endurance,self.Tom.maxEndurance)
            output += "\n"

        return output


