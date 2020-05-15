import os
from DataSourceInterface import DataSourceInterface

class CustomerFromStub(DataSourceInterface):

    def getEmail(self):
        return ['test@yahoo.com', 'test@icloud.com', 'test@google.com']

    def getFirstName(self):
        return ["Megan", "Logan", "Ross"]

    def getLastName(Self):
        return ["Domp", "Lille", "Amazon"]