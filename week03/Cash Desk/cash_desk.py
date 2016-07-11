class Bill:
    # da ne zabrava da go razdelq v razl failove

    def errors(self, bill_amount):
        if bill_amount < 0:
            raise ValueError('amount %b is negative number' % (bill_amount))
        if type(bill_amount) is not int:
            raise TypeError('amount type %b is not int' % (bill_amount))

    def __init__(self, _bill_amount):
        self.errors(_bill_amount)
        self._bill_amount = _bill_amount

    all_bils = {}

    def __int__(self):
        return int(self._bill_amount)

    def __str__(self):
        return "A {}$ bill".format(self._bill_amount)

    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash(self._bill_amount)

    def __eq__(self, other):
        return self._bill_amount == other._bill_amount

    def total(self):
        return int(self._bill_amount)

    def get_amount(self):
        return self._amount


class BatchBill:
    def __init__(self, bills):
        self._bills = bills

    def __len__(self):
        return len(self._bills)

    def __getitem__(self, index):
        return self._bills[index]

    def __int__(self):
        # tova total e ot classa Bill
        return sum([bill.total() for bill in self._bills])

    def total(self):
        return int(self)


class CashDesk:
    def __init__(self):
        self._amount = []

    def take_money(self, obj):
        self._amount.append(obj)

    def total(self):
        return sum([obj.total() for obj in self._amount])

    def inspect(self):
        bills_amount = {
            5: 0,
            10: 0,
            15: 0,
            20: 0,
            50: 0,
            100: 0
        }
        total_cash = 0
        for money_pile in bills_amount:
            if isinstance(money_pile, BatchBill):
                for bill in money_pile:
                    if int(bill._amount) in bills_amount:
                        bills_amount[int(bill.get_amount())] += 1
            else:
                print(money_pile)
                bills_amount[int(money_pile.get_amount())] += 1
        for bill_value in self.divbills:
            total_cash += int(bill_value)*bills_amount[bill_value]
        message = 'We have a total of {}$ in the desk\n'.format(total_cash)
        message += 'We have the following count of bills, sorted in ascending order:'
        for bill_value in sorted(bills_amount.keys()):
            if bills_amount[bill_value]:
                message += '\n{}$ bills - {}'.format(bill_value, bills_amount[bill_value])
        return message


values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]

batch = BatchBill(bills)

desk = CashDesk()

desk.take_money(batch)
desk.take_money(Bill(10))

print(desk.total())
# 390
desk.inspect()
