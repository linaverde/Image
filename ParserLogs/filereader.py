class FileReader:
    def readlogs(self, filepath):
        f = open(filepath)
        return f.read().split('\n')
