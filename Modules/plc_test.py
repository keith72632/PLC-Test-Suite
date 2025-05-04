import sys
import win32ui
import dde
import time
from datetime import datetime
from colorama import Fore, init
from enum import Enum

class DDE_Session:
 
    class __ModType(Enum):
        DIn = 'DIn'
        AIn = 'AIn'
        DOut = 'DOut'
        AOut = 'AOut'
    __server = None
    __conversation = None
    __report = []
    __ana_pos = []

    def __init__(self, topic):
        """
        Creates an instance of the DDE topic

        Args:
            topic - DDE topic name as string.
        """
        self.topic = topic
        
    def __create_server(self):
        """
        Creates the DDE server names PythonDDEClient
        """
        self.__server = dde.CreateServer()
        self.__server.Create('PythonDDEClient')

    def kill_server(self):
        """
        Closeds the DDE server
        """
        self.__server.Shutdown()
    def conversation_init(self):
        """
        Initiates conversation with an RSLinx DDE topic
        """
        self.__create_server()
        self.__conversation = dde.CreateConversation(self.__server)
        self.__conversation.ConnectTo('RSLinx', self.topic)
    def read_val(self, tag):
        """_summary_
        Reads the values of the PLC tag

        Args:
            tag - Tag name as a string.

        Returns:
            Tag value. Atmoic type.
        """
        try:
            value = self.__conversation.Request(tag)
            return value
        except Exception as e:
            print("Failed to read from PLC:", e)

    def write_val(self, tag, val):
        """
        Write value to PLC tag

        Args:
            tag (String): PLC tag to write data to
            val (Any): Value to write to the PLC tag

        Returns:
            Boolean: 1 = successful write, 0 = write failed
        """
    
        byte_val = str(val).encode("utf-8")
    
        try:
            self.__conversation.Poke(tag, byte_val)
            return True
        except Exception as e:
            print(f'Failed to write to tag {tag}', e)
            return False
        

    def test_analogs(self, num_chan, ain_modules):
        """
        Iterates through each analog channel on each module. Write 25%, 50%, 75%, and 100% to the input and reads the scaled value at each input reading.

        Args:
            num_chan (Integer): Number of channels in each module
        """
         #Initiates colorama
        init(autoreset=True)

        for i in range(0, (len(ain_modules))):
            #Writes analog module number
            self.__report.append(f'SLOT {ain_modules[i]} ANALOG MODULE:\n')
            print(Fore.GREEN + f'\nSLOT {ain_modules[i]} ANALOG MODULE:')

            #Write analog channel data
            for j in range(0, (num_chan)):
                print(Fore.CYAN + f'\nChannel {j}\n')
                self.__report.append(f'\tAnalog Channel {j}:\n')

                #Tests analog channel range
                for k in range(4, 21, 4):
                    load_bar = '=='
                    #Write to input channel
                    self.write_val(f'ENET_R01_{ain_modules[i]}_I.Ch{j}Data', k)
                    time.sleep(0.01)
                    #Reads scaled analog value
                    scaled_val = self.read_val(f'Program:P04_InputMapping.R01S0{ain_modules[i]}[{j}].Out_PV')
                    self.__report.append(f'\t\tScaled Value at {k} ma: {scaled_val}\n')
                    #Displays loading bar
                    sys.stdout.write(load_bar)
                    sys.stdout.flush()
                    load_bar = load_bar + '*'

    def generate_report(self):
        """
        Generates a report. Report name formatted with time and date.
        """
        report_file_name = f'Reports/Report_{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.txt'
        with open(report_file_name, 'w', newline='') as report_file:
            report_file.writelines(self.__report)