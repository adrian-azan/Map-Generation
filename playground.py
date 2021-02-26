import time
from rich.console import Console
from rich.layout import Layout
from rich.table import Table
from rich.live import Live
from rich import print
from rich.panel import Panel
from rich.text import Text
from diffusion import Diffusion
from Menu import Menu
from rich.align import Align
import keyboard


class Menu:

    def __init__(self, options = None):
        self.layout = Layout()
        self.options = options
        self.menu = Text()
        self.selection = 0
        self.selectionStyle = ""


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
        self.selection += 1
        self.selection %= len(self.options)
        self.populate()

    def up(self):
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


    def updateMenu(self):
        self.layout["lower"].update(self.menu)


from time import sleep
from rich.console import Console
console = Console()

with console.screen(style="bold white on red") as screen:
    for count in range(5, 0, -1):
        text = Align.center(
            Text.from_markup(f"[blink]Don't Panic![/blink]\n{count}", justify="center"),
            vertical="middle",
        )
        screen.update(Panel(text))
        sleep(1)




"""


t = Live()


mainMenu = MainMenu(["1. Diffusion", "2. Hulk", "3. Exit"])
mainMenu.setStyle("red on black")
keyboard.add_hotkey('down', mainMenu.down)
keyboard.add_hotkey('up', mainMenu.up)


with Live(mainMenu.layout,refresh_per_second=1) as live:
    while True:
        key = keyboard.read_key()
        mainMenu.updateMenu()
        if key == '3':
            break
        
        elif key == 'down':
            mainMenu.down()
            live.refresh()
        elif key == 'up':
            mainMenu.up()
            live.refresh()
        elif key in '1234567890':
            mainMenu.select(int(key)-1)
            live.refresh()
        

        time.sleep(.5)


"""