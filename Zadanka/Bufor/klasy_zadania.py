#Zadanie BANKOMAT

#bank.py
class Bank(object):
   def __init__(self,account_dict):
       self.accounts = account_dict

#ATM.py
class ATM(object):
    def __init__(self,bank):
        self.bank = bank
        self.account = None

    def menu(self):
        number = input("Podaj numer konta : ")
        password = input("Poddaj hasło : ")

        self.bank = bank
        for account_number in self.bank.accounts:
            if account_number == number:
                if password == self.bank.accounts[account_number].password:
                    self.account = self.bank.accounts[account_number]

        if not self.account:
            print("nie znaleziono konta")
        else:
            print("MENU")
            print("1. Wyświetl saldo")

            numer_operacji = input("Podaj co chcesz zrobić: ")
            if numer_operacji == "1":
                print(self.account.balance)
#account.py
class Account(object):
    def __init__(self,number,password,balance = 0):
        self.balance = balance
        self.number = number
        self.password = password
#Bank.py


bank = Bank({
    "1501232123" : Account("1501232123","alalal"),
    "2004535430" : Account("2004535430","tomektomek"),
    "2000353400" : Account("2000353400","siadama")})
print(bank.accounts)

atm = ATM(bank)
atm.menu()

atm = ATM(bank)
