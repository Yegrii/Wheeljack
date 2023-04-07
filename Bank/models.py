# Хорошо, давайте начнем с создания базовых классов для нашего проекта. 
# Нам нужен класс Bank для представления банка и класс Customer для представления клиента банка.

# Создайте класс Bank, который будет иметь атрибут name для хранения названия банка и атрибут customers,
# который будет хранить список всех клиентов банка.

# Затем создайте класс Customer, который будет иметь атрибуты name, address и phone_number для хранения персональной
# информации клиента. Класс Customer также должен иметь атрибут accounts, который будет хранить список всех
# банковских счетов, открытых клиентом в банке.

# Давайте добавим класс Bank из нашего предыдущего задания и реализуем методы для работы с банковскими счетами, 
# такие как открытие нового счета, закрытие существующего счета, а также поиск счета по номеру.

# Добавьте метод open_account в класс Bank, который будет создавать новый банковский счет с начальным балансом и
# владельцем счета.

# Добавьте метод close_account в класс Bank, который будет закрывать существующий банковский счет.

# Добавьте метод find_account в класс Bank, который будет находить банковский счет по его номеру.

# Добавьте метод get_total_assets в класс Bank, который будет возвращать общую сумму всех денег на всех счетах в банке.

# Добавьте метод transfer_money в класс BankAccount, который будет переводить деньги со счета одного владельца на
# счет другого владельца.

class Bank:
    def __init__(self, name, customers) -> None:
        self.name = name
        self.customers = customers
        self.accounts = []

    def open_account(self, account_number, balance, owner):
        # метод, создающий новый банковский счет и добавляющий его в список счетов банка
        new_account = BankAccount(account_number, balance, owner)
        self.accounts.append(new_account)
        return new_account

    def close_account(self, account_number):
        # метод, удаляющий существующий банковский счет из списка счетов банка
        for account in self.accounts:
            if account.get_account_number() == account_number:
                self.accounts.remove(account)
                return True
        return False

    def find_account(self, account_number):
        # метод, находящий банковский счет по его номеру.
        for account in self.accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def get_total_assets(self):
        # метод, возвращающий общую сумму всех денег на всех счетах в банке.
        total = 0
        for account in self.accounts:
            total += account.get_balance()
        return total


class Customer:
    def __init__(self, name, address, phone_number) -> None:
        self.name = name
        self.address = address
        self.phone_number = phone_number


# Отлично, начнем проект с банковской системы.
# Первое задание, которое мне приходит в голову, это создать класс BankAccount, 
# который будет представлять банковский счет. Класс должен иметь следующие методы:

# __init__(self, account_number, balance, owner): конструктор, принимающий номер счета, текущий баланс и владельца
# счета. deposit(self, amount): метод, принимающий сумму, которую нужно внести на счет. Он должен увеличить баланс
# счета на эту сумму. withdraw(self, amount): метод, принимающий сумму, которую нужно снять со счета. Он должен
# уменьшить баланс счета на эту сумму. get_balance(self): метод, возвращающий текущий баланс счета.
# get_account_number(self): метод, возвращающий номер счета. get_owner(self): метод, возвращающий владельца счета.

class BankAccount:
    # конструктор, принимающий номер счета, текущий баланс и владельца счета.
    def __init__(self, account_number, balance, owner) -> None:
        self.account_number = account_number
        self.balance = balance
        self.owner = owner

    def deposit(self, amount):
        # метод, принимающий сумму, которую нужно внести на счет. Он должен увеличить баланс счета на эту сумму.
        self.balance += amount

    def withdraw(self, amount):
        # метод, принимающий сумму, которую нужно снять со счета. Он должен уменьшить баланс счета на эту сумму.
        self.balance -= amount

    def get_balance(self):
        # метод, возвращающий текущий баланс счета.
        return self.balance

    def get_account_number(self):
        # метод, возвращающий номер счета.
        return self.account_number

    def get_owner(self):
        # метод, возвращающий владельца счета.
        return self.owner

    def transfer_money(self, recipient_account, amount):
        # метод, переводящий деньги со счета одного владельца на счет другого владельца.
        if self.balance >= amount:
            self.withdraw(amount)
            recipient_account.deposit(amount)
            return True
        else:
            return False


account1 = Customer('John', '123 Main St', '555-1234')
account2 = Customer('Jane', '456 Main St', '555-5678')
account3 = Customer('Bob', '789 Main St', '555-9012')

bank = Bank('My Bank', [account1, account2, account3])

account1 = bank.open_account('123-456', 1000, account1)
account2 = bank.open_account('456-789', 2000, account2)
account3 = bank.open_account('789-012', 3000, account3)

print(bank.get_total_assets())