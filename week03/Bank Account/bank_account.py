class BankAccount:

    def __init__(self, name, balance, currency):

        self._name = name

        if balance < 0:
            raise ValueError('amount %b is negative number' % (balance))

        self._balance = balance
        self._currency = currency
        self._history = []
        self._history.append('Account was created')

    def deposit(self, amount):
        if amount >= 0:
            self._balance += amount
            self._history.append('Deposited {}{}'.format(amount, self._currency))
        else:
            raise ValueError('amount %a is negative number' % (amount))

    def balance(self):
        msg = 'Balance check -> {}{}'
        self._history.append(msg.format(self._balance, self._currency))
        return self._balance

    def withdraw(self, amount):

        self._history.append('{}{} was withdrawed'.format(amount, self._currency))

        if self.__int__() >= amount:

            self._balance -= amount
            return True
        else:
            return False

    def __str__(self):

        return "Bank account for {} with balance of {}{}".format(self._name, self._balance, self._currency)

    def __int__(self):
        self._history.append('__int__ check -> {}{}'.format(self._balance, self._currency))

        return int(self._balance)

    def transfer_to(self, account, amount):

        self.withdraw(amount)
        account._balance += amount

        self._history.append('Transfer to Ivo for {}{}'.format(amount, self._currency))
        account._history.append('Transfer to Ivo for {}{}'.format(amount, self._currency))

    def history(self):
        return self._history


account = BankAccount("Rado", 0, "$")
print(account)
account.deposit(-1000)
print(account.balance())
print(str(account))
print(int(account))
print(account.history())
print(account.withdraw(500))
print(account.balance())
print(account.history())
print(account.withdraw(1000))
print(account.balance())
print(account.history())
rado = BankAccount("Rado", 1000, "BGN")
ivo = BankAccount("Ivo", 0, "BGN")
print(rado.transfer_to(ivo, 500))
print(rado.balance())
print(ivo.balance())
print(rado.history())
print(ivo.history())

