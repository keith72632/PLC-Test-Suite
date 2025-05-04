from configparser import ConfigParser
from enum import Enum

class Chassis:
    # __server_type = ''
    # __server_name = ''
    # __topic_name = ''
    # __num_din_chan = 0
    # __num_ain_chan = 0
    # __chassis_size = 0
    __modules = []
    __ain_modules = []
    __din_modules = []

    class __ModType(Enum):
        DIn = 'DIn'
        AIn = 'AIn'
        DOut = 'DOut'
        AOut = 'AOut'

    def __init__(self, ini_path):
        self.__ini_path = ini_path

    def parse_ini(self):
        self.__config = ConfigParser()
        self.__config.read(self.__ini_path)
    def build_chassis(self):
        print(f'Scanning {self.__ini_path} for chassis configuration')
        #Building server
        self.__server_type = self.__config["Server"]["type"]
        print(f'Server type: {self.__server_type}')
        self.__server_name = self.__config["Server"]["name"]
        print(f'Server name: {self.__server_name}')
        self.__topic_name = self.__config["Server"]["topic"]
        print(f'Topic name: {self.__topic_name}')

        #Building number of channels for each module
        self.__num_din_chan = self.__config.getint('NumChannels', 'DIn')
        print(f'Number digital input channels per module: {self.__num_din_chan}')
        self.__num_ain_chan = self.__config.getint('NumChannels', 'AIn')
        print(f'Number analog input channels per module: {self.__num_ain_chan}')

        #Building chassis size
        self.__chassis_size = self.__config.getint('Server', 'chassis_size')
        print(f'Chassis size: {self.__chassis_size}')

        self.__modules = [i[1] for i in self.__config.items('Modules')]
        print(f'Chassis layout: {self.__modules}')

        for index, mod in enumerate(self.__modules):
            match mod:
                case self.__ModType.DIn.value:
                    self.__din_modules.append(index+1)
                case self.__ModType.AIn.value:
                    self.__ain_modules.append(index+1)
    
    
    @property
    def server_type(self):
        return self.__server_type
    
    @property
    def server_name(self):
        return self.__server_name
    
    @property
    def topic_name(self):
        return self.__topic_name
    
    @property
    def num_din_chan(self):
        return self.__num_din_chan
    
    @property
    def num_ain_chan(self):
        return self.__num_ain_chan
    
    @property
    def din_modules(self):
        return self.__din_modules
    
    @property
    def ain_modules(self):
        return self.__ain_modules
    
    def build(self):
        self.parse_ini()
        self.build_chassis()

