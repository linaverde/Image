class LogStruct:
    def __getmonths(self, monthname):
        months = {
            "Jan": "01",
            "Feb": "02",
            "Mar": "03",
            "Apr": "04",
            "May": "05",
            "Jun": "06",
            "Jul": "07",
            "Aug": "08",
            "Sept": "09",
            "Oct": "10",
            "Nov": "11",
            "Dec": "12",
        }
        return months[monthname]

    def __formatdate(self, datetime):
        slash = datetime.find('/')
        day = datetime[:slash]
        datetime = datetime[slash + 1:]
        slash = datetime.find('/')
        month = datetime[:slash]
        datetime = datetime[slash + 1:]
        month = self.__getmonths(month)
        twopoint = datetime.find(':')
        year = datetime[:twopoint]
        datetime = datetime[twopoint + 1:]
        space = datetime.find(' ')
        self.time = datetime[: space]
        self.zone = int(datetime[space + 1:])
        self.date = year + '-' + month + '-' + day

    def __init__(self, ip, user, datetime, request, response, bytesSent, referer, browser):
        self.ip = ip
        self.user = user
        self.request = request
        self.response = response
        self.bytesSent = bytesSent
        self.referer = referer
        self.browser = browser
        self.__formatdate(datetime)

    def __str__(self):
        delim = '|'
        return "{1}{0}{2}{0}{3}{0}{4}{0}{5}{0}{6}{0}{7}{0}{8}{0}{9}{0}{10}\n".format(delim, self.ip, self.user,
                                                                                     self.date,
                                                                                     self.time, self.zone,
                                                                                     self.request, self.response,
                                                                                     self.bytesSent,
                                                                                     self.referer, self.browser)
