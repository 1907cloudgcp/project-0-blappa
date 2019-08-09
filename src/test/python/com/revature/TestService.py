#!/usr/bin/env python3




import unittest
from  entity import Users, Accounts
from service import AccountsService

class TestService(unittest.TestCase):

    #create user
    user = Users('Bertrick Lappa','bertricklappa@gmail.com','4054762371','10/12/19','blappa','xx123','10/12/95','10/12/95','1','1')

    #create account
    account = Accounts('Bertrick L', '875421235689', 0.0, 'Checking', 'for travel', '10/12/19', '10/12/95', '1', '1')
    
    def test_deposit(self):

        #test deposit method
        self.assertEqual(
            AccountsService.Init()
            .deposit(self.user, self.account, 1500.00, 'for school', '10/12/19', '10/12/19'),
            1500.00)
        """ current balance : 0.0
            transaction deposit 1500.00
            the new balance should return 1500.00
                          """


    def test_withdraw(self):
   
        #test withdraw method
        self.assertEqual(
             AccountsService.Init()
            .withdraw(self.user, self.account, 200.00, 'for school', '10/12/19', '10/12/19'),
            1300.00)
        """ current balance : 1500.00
            transaction withdraw 200.00
            the new balance should return 1300.00
                        """


if __name__ == '__main__':
    unittest.main()
