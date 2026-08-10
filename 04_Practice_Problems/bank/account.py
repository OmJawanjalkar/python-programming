from abc import ABC, abstractmethod

from streamlit import form

from .transaction import Transaction
from .exceptions import InvalidAmountError


class Account(ABC):
  
    account_counter = 1000
    
    def __init__(self, owner, initial_balance=0):
        
        Account.account_counter += 1
        
        self.account_number = (
          f"ACC{Account.account_counter}"
                )
        
        self.owner = owner 
        
        ## Encapsultion
        
        self._balance = 0
        
        self.transactions = []
        
        if initial_balance > 0:
            
            self._balance = initial_balance
            
            transaction = Transaction(
                "DEPOSIT", initial_balance, "Initial Deposit"
            )
            self.transactions.append(transaction)
            
    def deposit(self, amount):
        
        if amount <= 0:
            raise InvalidAmountError(
                "Deposit amount must be greater than zero."
            )
            
        self._balance += amount
        
        transaction = Transaction("DEPOSIT", amount, "Money Deposited")
        self.transactions.append(transaction)
        
    @abstractmethod
    def withdraw(self, amount):
      pass

    def get_balance(self):
        return self._balance
      
        def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def show_transactions(self):

        if not self.transactions:
            print("\nNo transactions found.")
            return

        print("\n" + "=" * 90)
        print("TRANSACTION HISTORY")
        print("=" * 90)

        for transaction in self.transactions:
            print(transaction)

    def __str__(self):

        return (
            f"Account Number : {self.account_number}\n"
            f"Account Holder : {self.owner.name}\n"
            f"Account Type   : {self.__class__.__name__}\n"
            f"Balance        : ₹{self._balance:.2f}"
        
        )