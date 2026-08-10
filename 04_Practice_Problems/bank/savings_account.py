from .account import Account
from .transaction import Transaction
from .exceptions import InvalidAmountError, InsufficientBalanceError

class SavingsAccount(Account):
   
   MINIMUM_BALANCE = 500
   MAX_WITHDRAWAL = 20000
   INTEREST_RATE = 4


   def withdraw(self, amount):
    
     if amount <= 0:
          raise InvalidAmountError(
              "Withdrawal amount must be greater than zero."
          )
          
     if amount > self.MAX_WITHDRAWAL:
            raise InvalidAmountError(
                f"Maximum withdrawal limit is "
                f"₹{self.MAX_WITHDRAWAL}."
            )
            
     if self._balance - amount < self.MINIMUM_BALANCE:
            raise InsufficientBalanceError(
                f"Savings account must maintain "
                f"a minimum balance of ₹{self.MINIMUM_BALANCE}."
            )
            
     self._balance -= amount
     
     transaction  = Transaction("WITHDRAWAL", amount, "Money Withdrawn")
     self.transactions.append(transaction)
     
   def  calculate_interest(self):
      return(
        self._balance * self.INTEREST_RATE / 100
      )
