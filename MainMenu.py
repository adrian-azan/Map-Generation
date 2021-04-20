from Menu import Menu
import time
from rich.console import Console
from rich.layout import Layout
from rich.table import Table
from rich.live import Live
from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.align import Align
from Life import Life
from diffusion import Diffusion
import keyboard


class MainMenu(Menu):
    def __init__(self, options = None):
        super().__init__(options)
        
        #Upper is interactive map preview
        #Lower is menu options
        self.layout.split(
            Layout(name='upper'),
            Layout(name='lower')
        )
        
        self.sleepTime = .5
        
        self.maps = dict()
        self.maps["diffusion"] = Diffusion(80,30, 300)
        self.maps["life"] = Life(140,30,5,80)

        self.layout["upper"].size = 35
        self.layout["lower"].update(self.menu)
        self.populate()

    def restart(self):
        if self.selection == 0:
            self.maps["diffusion"].restart()
        if self.selection == 1:
            self.maps["life"].restart()
    
    """
    Returns selected option to menuManager
    """
    def select(self):
        if self.selection == 0:
            return "diffusion"
        if self.selection == 1:
            return "life"
        if self.selection == 2:
            return "exit"

    """
    Performs selected map generation and displays result
    to the menu. Checks if map is finished to restart
    """
    def updateMenu(self):
        self.layout["lower"].update(self.menu)
        if self.selection == 0:
            self.maps["diffusion"].diffusion()
            self.layout["upper"].update(self.maps["diffusion"].update())
            return self.maps["diffusion"].finished()
        if self.selection == 1:
            self.maps["life"].life()
            self.layout["upper"].update(self.maps["life"].update())
            return self.maps["life"].finished()