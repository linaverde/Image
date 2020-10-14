import os
import csv
import datetime


class FileWriter:
    def writetocsv(self, logs, prefixname='logs'):
        count = len(logs)
        filename = prefixname + ":" + str(count) + ":" + str(datetime.date.today()) + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(logs)

    def writetotxt(self, logs):
        pass
