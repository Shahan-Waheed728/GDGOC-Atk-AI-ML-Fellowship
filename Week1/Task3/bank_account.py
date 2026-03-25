
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance   # Encapsulation (private)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. Remaining balance: {self.__balance}")
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

    def __str__(self):
        return f"Account Owner: {self.owner}, Balance: {self.__balance}"


# Inheritance
class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        self.deposit(interest)
        print(f"Interest added: {interest}")


# Polymorphism example
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        # Overriding method
        print("Processing Current Account withdrawal...")
        super().withdraw(amount)


# Test
if __name__ == "__main__":
    acc1 = SavingsAccount("Ali", 1000)
    acc1.deposit(500)
    acc1.withdraw(200)
    acc1.add_interest()
    print(acc1)

    acc2 = CurrentAccount("Ahmed", 2000)
    acc2.withdraw(2500)