from abc import ABC, abstractmethod 
from datetime import datetime 

## Custom Exceptions

class BankError(Exception):
    """ Base exception for Banking errors"""
    pass

class InvalidAmountError(BankError):
    pass


class InsufficientBalanceError(BankError):
    pass


class AccountNotFoundError(BankError):
    pass


class CustomerNotFoundError(BankError):
    pass


class AccountExistsError(BankError):
    pass
  
  
  
  ## Transaction Class
  
  
class Transaction:

    transaction_counter = 1000

    def __init__(self, transaction_type, amount, description=""):
        Transaction.transaction_counter += 1

        self.transaction_id = f"TXN{Transaction.transaction_counter}"
        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return (
            f"{self.transaction_id} | "
            f"{self.transaction_type:<10} | "
            f"₹{self.amount:>10.2f} | "
            f"{self.timestamp} | "
            f"{self.description}"
        )
        
        
class Account(ABC):
    
    account_counter = 1000
    
    def __init__(self, owner, initial_balance=0):
        
        Account.account_counter += 1
        
        self.account_number = f"ACC{Account.account_counter}"
        self.owner = owner
        
        ## Encapsultion 
        self.__balance = 0
        
        self.transactions = []
        
        if initial_balance > 0:
          pass