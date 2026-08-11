class BankError(Exception):
    """Base exception for banking errors."""
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