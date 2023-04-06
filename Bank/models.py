# Хорошо, давайте начнем с создания базовых классов для нашего проекта. 
# Нам нужен класс Bank для представления банка и класс Customer для представления клиента банка.

# Создайте класс Bank, который будет иметь атрибут name для хранения названия банка и атрибут customers, который будет хранить список всех клиентов банка.

# Затем создайте класс Customer, который будет иметь атрибуты name, address и phone_number для хранения персональной информации клиента. 
# Класс Customer также должен иметь атрибут accounts, который будет хранить список всех банковских счетов, открытых клиентом в банке.

class Bank:
    def __init__(self, name, customers) -> None:
        self.name = name
        self.customers = customers

    def open_account(self):
        pass

    def close_account(self):
        pass

    def find_account(self):
        pass

    def get_total_assets(self):
        pass

    def transfer_money(self):
        pass


class Customer:
    def __init__(self, name, address, phone_number) -> None:
        self.name = name
        self.address = address
        self.phone_number = phone_number

# Отлично, начнем проект с банковской системы. 
# Первое задание, которое мне приходит в голову, это создать класс BankAccount, 
# который будет представлять банковский счет. Класс должен иметь следующие методы:

# __init__(self, account_number, balance, owner): конструктор, принимающий номер счета, текущий баланс и владельца счета.
# deposit(self, amount): метод, принимающий сумму, которую нужно внести на счет. Он должен увеличить баланс счета на эту сумму.
# withdraw(self, amount): метод, принимающий сумму, которую нужно снять со счета. Он должен уменьшить баланс счета на эту сумму.
# get_balance(self): метод, возвращающий текущий баланс счета.
# get_account_number(self): метод, возвращающий номер счета.
# get_owner(self): метод, возвращающий владельца счета.

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
    
# Давайте добавим класс Bank из нашего предыдущего задания и реализуем методы для работы с банковскими счетами, 
# такие как открытие нового счета, закрытие существующего счета, а также поиск счета по номеру.

# Добавьте метод open_account в класс Bank, который будет создавать новый банковский счет с начальным балансом и владельцем счета.

# Добавьте метод close_account в класс Bank, который будет закрывать существующий банковский счет.

# Добавьте метод find_account в класс Bank, который будет находить банковский счет по его номеру.

# Добавьте метод get_total_assets в класс Bank, который будет возвращать общую сумму всех денег на всех счетах в банке.

# Добавьте метод transfer_money в класс BankAccount, который будет переводить деньги со счета одного владельца на счет другого владельца.