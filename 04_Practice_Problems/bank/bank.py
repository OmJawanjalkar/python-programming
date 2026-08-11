from .customer import Customer
from .savings_account import SavingsAccount
from .current_account import CurrentAccount
from .exceptions import (
    CustomerNotFoundError,
    AccountNotFoundError,
    InvalidAmountError
)


class Bank:

    def __init__(self, bank_name):

        self.bank_name = bank_name

        self.customers = {}
        self.accounts = {}

    @staticmethod
    def validate_name(name):

        if not name.strip():
            raise ValueError(
                "Name cannot be empty."
            )

    @staticmethod
    def validate_email(email):

        if "@" not in email:
            raise ValueError(
                "Invalid email address."
            )

    @staticmethod
    def validate_phone(phone):

        if not phone.isdigit() or len(phone) != 10:
            raise ValueError(
                "Phone number must contain exactly 10 digits."
            )

    def create_customer(self, name, email, phone):

        self.validate_name(name)
        self.validate_email(email)
        self.validate_phone(phone)

        customer = Customer(
            name,
            email,
            phone
        )

        self.customers[
            customer.customer_id
        ] = customer

        return customer

    def create_account(
        self,
        customer_id,
        account_type,
        initial_balance
    ):

        if customer_id not in self.customers:
            raise CustomerNotFoundError(
                "Customer not found."
            )

        if initial_balance < 0:
            raise InvalidAmountError(
                "Initial balance cannot be negative."
            )

        customer = self.customers[customer_id]

        if account_type.lower() == "savings":

            if (
                initial_balance
                < SavingsAccount.MINIMUM_BALANCE
            ):
                raise InvalidAmountError(
                    f"Savings account requires "
                    f"minimum ₹{SavingsAccount.MINIMUM_BALANCE}."
                )

            account = SavingsAccount(
                customer,
                initial_balance
            )

        elif account_type.lower() == "current":

            account = CurrentAccount(
                customer,
                initial_balance
            )

        else:

            raise ValueError(
                "Invalid account type."
            )

        customer.add_account(account)

        self.accounts[
            account.account_number
        ] = account

        return account

    def find_account(self, account_number):

        if account_number not in self.accounts:
            raise AccountNotFoundError(
                "Account not found."
            )

        return self.accounts[account_number]

    def deposit(self, account_number, amount):

        account = self.find_account(
            account_number
        )

        account.deposit(amount)

    def withdraw(self, account_number, amount):

        account = self.find_account(
            account_number
        )

        # Polymorphism
        account.withdraw(amount)

    def transfer(
        self,
        sender_account_number,
        receiver_account_number,
        amount
    ):

        if sender_account_number == receiver_account_number:
            raise ValueError(
                "Sender and receiver cannot be the same."
            )

        sender = self.find_account(
            sender_account_number
        )

        receiver = self.find_account(
            receiver_account_number
        )

        sender.withdraw(amount)
        receiver.deposit(amount)

    def show_account(self, account_number):

        account = self.find_account(
            account_number
        )

        print("\n" + "=" * 60)
        print("ACCOUNT DETAILS")
        print("=" * 60)

        print(account)

    def show_customers(self):

        if not self.customers:
            print("\nNo customers found.")
            return

        for customer in self.customers.values():

            print(customer)
            print("-" * 60)

    def show_all_accounts(self):

        if not self.accounts:
            print("\nNo accounts found.")
            return

        print("\n" + "=" * 80)
        print("ALL ACCOUNTS")
        print("=" * 80)

        for account in self.accounts.values():

            print(
                f"{account.account_number:<12} | "
                f"{account.__class__.__name__:<16} | "
                f"{account.owner.name:<20} | "
                f"₹{account.get_balance():>10.2f}"
            )