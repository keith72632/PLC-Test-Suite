from colorama import Fore, init, Style, Back

class Menu:
    def print_logo():
        #Initiates colorama
        init(autoreset=True)
        logo = r'''
    
                                                                                   _____                    
               _____           _____        ___________   _______    ______   _____\    \ ___________       
          _____\    \_       /      |_      \          \  \      |  |      | /    / |    |\          \      
         /     /|     |     /         \      \    /\    \  |     /  /     /|/    /  /___/| \    /\    \     
        /     / /____/|    |     /\    \      |   \_\    | |\    \  \    |/|    |__ |___|/  |   \_\    |    
       |     | |_____|/    |    |  |    \     |      ___/  \ \    \ |    | |       \        |      ___/     
       |     | |_________  |     \/      \    |      \  ____\|     \|    | |     __/ __     |      \  ____  
       |\     \|\        \ |\      /\     \  /     /\ \/    \|\         /| |\    \  /  \   /     /\ \/    \ 
       | \_____\|    |\__/|| \_____\ \_____\/_____/ |\______|| \_______/ | | \____\/    | /_____/ |\______| 
       | |     /____/| | ||| |     | |     ||     | | |     | \ |     | /  | |    |____/| |     | | |     | 
        \|_____|     |\|_|/ \|_____|\|_____||_____|/ \|_____|  \|_____|/    \|____|   | | |_____|/ \|_____| 
               |____/                                                             |___|/                    
                          
                                    Allen Bradley PLC Applicaton Audit Tool
                                                version 1.0.0
                                        Developed by Keith Horton                                  
        '''
        print(Fore.RED + logo)
    
    def menu_select():
        prompt = '''
Select from the following:
    Test Analog Inputs                 [1]
    Generate Alarm Configuration Audit [2]
    Quit                               [9]
'''
        
        selection = input(Style.BRIGHT + prompt)
        return selection