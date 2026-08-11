from .account import Account
from .transaction import Transaction
from .exceptions import (
    InvalidAmountError,
    InsufficientBalanceError
)


class CurrentAccount(Account):

    OVERDRAFT_LIMIT = 10000

    def withdraw(self, amount):

        if amount <= 0:
            raise InvalidAmountError(
                "Withdrawal amount must be greater than zero."
            )

        available_balance = (
            self._balance +
            self.OVERDRAFT_LIMIT
        )

        if amount > available_balance:
            raise InsufficientBalanceError(
                "Withdrawal exceeds overdraft limit."
            )

        self._balance -= amount

        transaction = Transaction(
            "WITHDRAW",
            amount,
            "Money withdrawn"
        )

        self.transactions.append(transaction)

    def get_available_balance(self):

        return (
            self._balance +
            self.OVERDRAFT_LIMIT
        )