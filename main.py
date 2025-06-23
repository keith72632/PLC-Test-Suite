import os
from Modules import plc_test
from Modules.chassis import Chassis # type: ignore
from Modules.PLC import CPU
from Modules.menu import Menu
from colorama import Fore, init, Style, Back


  
if __name__ == '__main__':

    Menu.print_logo()

    # #Creates Reports folder if one doesn't already exist
    reports_path = 'Reports'

    if os.path.exists(reports_path):
        print('Using existing reports folder')
    else:
        input('Reports folder not found. Create one?Yes[Y] No[N]')
        if input == 'y' or 'Y':
            os.makedirs(reports_path)
            print('Reports directory created')
        else:
            exit()

    
    selection = int(Menu.menu_select())


    match selection:
        case 1:
            #chassis class declaration
            rack = Chassis('Config/chassis.ini')
            rack.build()
   
            #session class declaration
            session = plc_test.DDE_Session('_82PLC')
            session.conversation_init()
            session.test_analogs(rack.num_ain_chan, rack.ain_modules)
            session.generate_report()
            session.kill_server()
        case 2:
            print('Generating Alarm Configuration Audit\n')
            ip_addr = input(Style.BRIGHT + 'Enter Ip Address of the PLC\n')
            #cpu = CPU("192.168.236.129")
            cpu = CPU(ip_addr)
            cpu.get_alarm_list()
            cpu.print_alarm_val()
            cpu.generate_report()
            cpu.close()
        case 9:
            print('Exiting program\n')
        case _:
            print('Error\n')

    
 
       
        
    #chassis class declaration
    

   

    

    