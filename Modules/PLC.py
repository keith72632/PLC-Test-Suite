from pylogix import PLC
from datetime import datetime
from colorama import Fore, init


class Alarm:
    __properties = [
        'Cfg_DelayTm',
        'Cfg_MaxShelfTm',
    ]
    __full_name = []
    def __init__(self, alarm_name):
        for prop in self.__properties:
            self.__full_name.append(alarm_name + '.' + prop)
        self.__num_props = len(self.__properties)
    
    def clear_full_name(self):
        self.__full_name.clear()
    @property
    def full_name(self):
        return self.__full_name
class CPU:
    __alarm_names = []
    __alarms = []
    __properties = [
        'Cfg_PCmdClear',
        'Cfg_Exists',
        'Cfg_Target',
        'Cfg_Latched',
        'Cfg_AckReqd',
        'Cfg_AllowShelve',
        'Cfg_AllowDisable',
        'Cfg_DelayTm',
        'Cfg_MinOnTm',
        'Cfg_Severity',
        'Cfg_MaxShelfTm',
    ]
    def __init__(self, ip_address):
        self.__ip_address = ip_address
        self.__comm =  PLC(self.__ip_address)
    def read_val(self, tag_name):
        ret = self.__comm.Read(tag_name)
        return ret.Value
    def get_alarm_list(self):
        tags = self.__comm.GetTagList()
        for t in tags.Value:
            if 'AOI_P_Alarm' in t.DataType:
                self.__alarm_names.append(t.TagName)
        for name in self.__alarm_names:
            row = [(name + '.' + prop) for prop in self.__properties]
            self.__alarms.append(row)
        print(f'\nNumber of alarm tags: {len(self.__alarm_names)}\n')

    def print_alarm_val(self):
        for alarm in self.__alarms:
            for prop in alarm:
                self.read_val(prop)
    
    def generate_report(self):
        """
        Generates a report. Report name formatted with time and date.
        """
        report_file_name = f'Reports/Alarms_{datetime.now().strftime("%Y-%m-%d %H-%M-%S")}.txt'
        print(f'Generating report {report_file_name}\n')
        with open(report_file_name, 'w', newline='') as report_file:
            report_file.writelines('ALARM CONFIGURATIONS\n\n')
            for index, name in enumerate(self.__alarm_names):
                report_file.writelines(name + ':\n')
                for prop in self.__alarms[index]:
                    val = f'\t {prop.replace(name, '')} = {self.read_val(prop)}\n'
                    report_file.writelines(str(val))

        print(f'Report {report_file_name} complete\n')
    def close(self):
        self.__comm.Close()
