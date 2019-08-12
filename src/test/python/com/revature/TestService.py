#!/usr/bin/env python3




import unittest
from  entity import Users, Accounts, Transactions
from service import AccountsService, TransactionsService

class TestService(unittest.TestCase):

    #create user
    user = Users('Bertrick Lappa','bertricklappa@gmail.com','4054762371','10/12/19','blappa','xx123','10/12/95','10/12/95','1','1')

    #create account for Bertrick Lappa with 0.0 balance
    account = Accounts('Bertrick L', '875421235689', 0.0, 'Checking', 'for travel', '10/12/19', '10/12/95', '1', '1')
    
    transactionDeposit = Transactions('deposit11004', '', 'deposit', '10/12/19', '10/12/19', '10/12/19', '10/12/19', 1, account)

    transactionWithdraw = Transactions('withdraw11004', '', 'withdraw', '10/12/19', '10/12/19', '10/12/19', '10/12/19', 1, account)

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
        self.assertEqual(
            TransactionsService.Init()
            .save(self.transactionDeposit),
            True)
        """  this transaction should retrurn True
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
        #save transaction
        self.assertEqual(
            TransactionsService.Init()
            .save(self.transactionWithdraw),
            True) 
        """  this trasction should retrurn True
                                      """



if __name__ == '__main__':
    unittest.main()
