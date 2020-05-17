import csv

class ReadCSVFile :

    filePathPrefix = "resource/"

    def getFileData(self, directory,  fileName):
        fileData = []
        with open(self.filePathPrefix+ directory + fileName,'rt')as dataFile:
            fileReader = csv.reader(dataFile)
            for row in fileReader:
                fileData.append(row)
        return fileData

    def getFileDataForStub(self):
        return [['test@yahoo.com', 'Samuel', 'Lip', '1234']]

    def getFileDataForFake(self):
        
        return self.getFileData("entities/", "CustomerForFake.csv")
