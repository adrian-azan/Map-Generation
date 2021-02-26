import time
from rich.console import Console
from rich.layout import Layout
from rich.table import Table
from rich.live import Live
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from diffusion import Diffusion

from diffusion import Diffusion
import keyboard

class Menu:

    def __init__(self, options = None):
        self.layout = Layout()
        self.options = options
        self.menu = Text()
        self.selection = 0
        self.selectionStyle = "red on black"
        self.populate()


    def setStyle(self,style):
        self.selectionStyle = style

    def populate(self):
        self.menu = Text()
        for i in range(len(self.options)):
            if i == self.selection:
                self.menu.append(self.options[i]+"\n", self.selectionStyle)
            else:
                self.menu.append(self.options[i]+"\n")


    def down(self):
        keyboard.press("backspace")
        self.selection += 1
        self.selection %= len(self.options)
        self.populate()

    def up(self):
        keyboard.press("backspace")
        self.selection -=1
        if self.selection < 0:
            self.selection = len(self.options)-1
        self.populate()

    def select(self, select):
        if select > 0 and select < len(self.options):
            self.selection = select
        self.populate()

class MainMenu(Menu):
    def __init__(self, options = None):
        super().__init__(options)
        self.layout.split(
            Layout(name='upper'),
            Layout(name='lower')
        )
        self.layout["lower"].update(self.menu)

        self.populate()

        self.maps = dict()
        self.maps["diffusion"] = Diffusion(80,30, 300)
        self.layout["upper"].update(self.maps["diffusion"])
        self.layout["upper"].size = 35

    def updateMenu(self):
        self.layout["lower"].update(self.menu)
        self.maps["diffusion"].diffusion()
        self.layout["upper"].update(self.maps["diffusion"].update())