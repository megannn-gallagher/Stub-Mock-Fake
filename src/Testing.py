import unittest
from DBSetup import DBSetup
from CustomerDatabaseMapping import CustomerDatabaseMapping

class Testing(unittest.TestCase):

    dbSetup = DBSetup()
    customerMapping = CustomerDatabaseMapping(dbSetup)

    def testCustomerFromStub(self):
        customer = self.customerMapping.CustomerFromStub()
        data = [['test@yahoo.com', 'Samuel', 'Lip', '1234']]
        

        self.assertEqual(customer, data)

    def testCustomerFromMock(self):
        customer = self.customerMapping.CustomerFromMock()
        data = [['test@yahoo.com', 'Samuel', 'Lip', '1234']]

        self.assertEqual(customer, data)

    def testCustomerFromFake(self):
        customer = self.customerMapping.CustomerFromFake()
        test = self.customerMapping.testData()

        self.assertEquals(customer, test)




def main():
    unittest.main()

if __name__ == "__main__":
    unittest.main()

