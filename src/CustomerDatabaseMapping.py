from Customer import Customer
from ReadCSVFile import ReadCSVFile
from DBSetup import DBSetup
from DatabaseGetData import DatabaseGetData
from unittest.mock import MagicMock

class CustomerDatabaseMapping:

    customerTableName = Customer.dataSourceName

    emailAddressPosition = 0
    firstNamePosition = 1
    lastNamePosition = 2
    passwordPosition = 3

    dataSourceFields = ["emailAddress","firstName","lastName","password"]

    dbSetup = None
    dataSource = DatabaseGetData()

    def __init__(self,dbSetup):
        self.dbSetup = dbSetup

    def createCustomer(self, customerDetails):
        customer = Customer(
            customerDetails[self.emailAddressPosition],
            customerDetails[self.firstNamePosition],
            customerDetails[self.lastNamePosition],
            customerDetails[self.passwordPosition]
        )
        return customer
    

    def getCustomerDataFromFile(self):
        customerFileReader = ReadCSVFile()
        return customerFileReader.getFileData("Entities/",self.customerTableName + ".csv")

    def customerDataBaseSetup(self):
        self.dbSetup.dropTable(self.customerTableName)
        self.dbSetup.createTable(self.customerTableName,self.dataSourceFields)
        customerInsertSql = self.dbSetup.generateInsertStatement(self.customerTableName,self.dataSourceFields)
        customerData = self.getCustomerDataFromFile()
        self.dbSetup.populateEntity(customerInsertSql,customerData)

    def getCustomerData(self):
        return self.dataSource.getData(self.customerTableName,self.dataSourceFields)

    def createAllCustomers(self):
        allCustomers = []
        allCustomerData = self.getCustomerData()
        for customerRow in allCustomerData:
            customer = self.createCustomer(customerRow)
            allCustomers.append(customer)
        return allCustomers

    def CustomerFromStub(self):
        readFile = ReadCSVFile()

        return readFile.getFileDataForStub()

    def CustomerFromMock(self):
        mockdata = [['test@yahoo.com', 'Samuel', 'Lip', '1234']]

        readFile = MagicMock(return_value=mockdata)
        return readFile()

           
    def CustomerFromFake(self):
        readFile = ReadCSVFile()

        return readFile.getFileDataForFake()

    def testData(self):

        expected = [['test@yahoo.com', 'Samuel', 'Lip', '1234']]
    

def main():
    dbSetup = DBSetup()
    customerDatabaseMapping = CustomerDatabaseMapping(dbSetup)
    dbExecuteSQL = DBExecuteSQL()
    customerDatabaseMapping.customerDataBaseSetup()
    print(customerDatabaseMapping.getCustomerData())
    allCustomers = customerDatabaseMapping.createAllCustomers()
    print(len(allCustomers))
    print(customerDatabaseMapping.CustomerFromStub())

if __name__ == "__main__":
    main()
