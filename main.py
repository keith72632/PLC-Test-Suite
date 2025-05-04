import os
from Modules import plc_test
from Modules.chassis import Chassis # type: ignore

  
if __name__ == '__main__':
    #Creates Reports folder if one doesn't already exist
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
       
        
    #chassis class declaration
    rack = Chassis('Config/chassis.ini')
    rack.build()
   
    
    #session class declaration
    session = plc_test.DDE_Session('_82PLC')
    session.conversation_init()
    session.test_analogs(rack.num_ain_chan, rack.ain_modules)
    session.generate_report()
    session.kill_server()
    

    