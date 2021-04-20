from Menu import Menu
from MainMenu import MainMenu
from LifeMenu import LifeMenu
import keyboard
"""
Keeps track of which menu is currently being
displayed to the screen
"""
class MenuManager:

    
    def __init__(self):
        
        #Available Menus
        self.menus = dict()
        self.menus['main'] = MainMenu(["1. Hulk", "2. Life", "3. Exit"])
        #self.menus['diffusion'] = "HULK"
        self.menus['life'] = LifeMenu(["1. Noise Level", "2. Generation Cap", "3. Width", "4. Height", "5. Exit"])
        self.active = self.menus['main']             

        #
        self.quit = False

         
        #Keys will control which menu options is 
        #used on the active menu
        keyboard.add_hotkey('down', self.down)
        keyboard.add_hotkey('up', self.up)
        keyboard.add_hotkey('s', self.down)
        keyboard.add_hotkey('w', self.up)
        
        keyboard.add_hotkey('enter', self.select)        
        
    def up(self):
        self.active.up()
    
    def down(self):
        self.active.down()
    
    def select(self):        
        #Gets selected option from active menu
        choice = self.active.select()             
        if choice == "exit":
            self.quit = True
        try:            
            #Sets new active menu
            self.active = self.menus[choice]
           
        except KeyError:
            print(choice, "Does not exist")
        except:
            print("MENUMANAGER: SELECT ERROR")
        