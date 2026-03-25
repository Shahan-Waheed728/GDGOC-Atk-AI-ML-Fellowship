import logging
from bank import BankAccount
from utils import greet, square

logging.basicConfig(level=logging.INFO)
logging.info("Program started")  

acc = BankAccount("Ali", 1000)
acc.deposit(500)

print(acc.get_balance())
print(greet("Shahan"))
print(square(5))



