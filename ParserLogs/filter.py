from ParserLogs.LogStructure import LogStruct
import re


class Filer:
    def isrobot(self, log: LogStruct):
        return re.findall(r'B|bot', log.browser)

    def filtering(self, log):
        flag = True
        if self.isrobot(log):
            return not flag
        return flag
