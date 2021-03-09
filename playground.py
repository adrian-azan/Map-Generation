import time
from rich.console import Console
from rich.layout import Layout
from rich.table import Table
from rich.live import Live
from rich import print
from rich.panel import Panel
from diffusion import Diffusion
from Menu import Menu
from Menu import MainMenu
from Life import Life

import keyboard
def end():
    keyboard.press("backspace")
    global stop
    stop = True


"""
with Live(menu, refresh_per_second=1) as live:
    while True:
        menu.display()
        live.update(menu)
        keyboard.wait()
"""


t = Live()
c = Console()

mainMenu = MainMenu(["1. Diffusion", "2. Hulk", "3. Exit"])
mainMenu.setStyle("red on black")
keyboard.add_hotkey('down', mainMenu.down)
keyboard.add_hotkey('up', mainMenu.up)
keyboard.add_hotkey('3', end)

test = Life(10,10,800)
while True:
    test.life()
    time.sleep(1)
    test.print()
    print()

stop = False
with Live(mainMenu.layout,refresh_per_second=4) as live:
    while stop == False:
        mainMenu.updateMenu()
        if mainMenu.maps["diffusion"].finished():
            mainMenu.maps["diffusion"].restart()
        time.sleep(.05)

