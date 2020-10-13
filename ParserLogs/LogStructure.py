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
        day = datetime[:3]
        month = ''
        datetime = datetime[3:]
        for i in datetime:
            if i != '/':
                month += i
            else:
                datetime = datetime[:datetime.find(i)]
        month = self.__getmonths(month)
        year = datetime[:4]
        datetime = datetime[5:]
        self.time = datetime[:7]
        self.zone = int(datetime[9:])
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
        delim = '<'
        return "{1}{0}{2}{0}{3}{0}{4}{0}{5}{0}{6}{0}{7}{0}{8}{0}{9}{0}{10}".format(delim, ip, user, date, time, zone,
                                                                                   request, response, bytesSent,
                                                                                   referer, browser)
