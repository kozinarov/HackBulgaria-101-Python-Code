import unittest
from bank_account import BankAccount
# poslednite dva testa me murzi

class TestBankAccount(unittest.TestCase):

    def setUp(self):
        self.Ivo = BankAccount("Ivo", 1000, "$")
        self.Rado = BankAccount("Rado", 500, "$")


    def test_bank_account_init(self):
        self.assertEqual(self.Ivo._name, "Ivo")
        self.assertEqual(self.Ivo._balance, 1000)
        self.assertEqual(self.Ivo._currency, "$")

    def test_deposit(self):
        self.Ivo.deposit(200)
        self.assertEqual(self.Ivo._balance, 1200)

    def test_balance(self):
        self.assertEqual(self.Ivo.balance(), 1000)

    def test_withdraw(self):
        self.assertEqual(self.Ivo.withdraw(400), True)
        self.assertEqual(self.Ivo.withdraw(1400), False)

    def test___str__(self):
        self.assertEqual(str(self.Ivo), "Bank account for Ivo with balance of 1000$")

    def test___int__(self):
        self.assertEqual(int(self.Ivo), 1000)
"""
    def test_transfer_to(self):
        self.Ivo.transfer_to(400, self.Rado)
        self.assertEqual(self.Ivo._balance(), 600)
       #  self.assertEqual(self.Rado.balance(), 900)

"""
if __name__ == '__main__':
    unittest.main()
    