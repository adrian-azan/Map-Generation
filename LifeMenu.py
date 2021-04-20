from Menu import Menu
from rich.layout import Layout
from rich.console import Console
from rich.padding import Padding

class LifeMenu(Menu):
    
    def __init__(self, options = None):
        super().__init__(options)
        
        self.layout.split(
            Layout(name="upper"),
            Layout(name="lower")
        )
        
        self.layout["lower"].update(self.menu)
        self.layout["upper"].update(Padding("",(8,8,2,2)))
        self.populate()
        
    """
    Returns menu selection to MenuManager
    """
    def select(self):
        if self.selection == 3:
            print()        
        if self.selection == 4:
            return "main"
        
        return "none"
        
    def updateMenu(self):
        self.layout["lower"].update(self.menu)
        