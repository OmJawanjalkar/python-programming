from bank.bank import Bank
from bank.exceptions import BankError

from utils.helpers import (
    get_amount,
    pause
)


def create_customer_menu(bank):

    print("\n" + "=" * 60)
    print("CREATE CUSTOMER")
    print("=" * 60)

    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")

    try:

        customer = bank.create_customer(
            name,
            email,
            phone
        )

        print(
            "\nCustomer created successfully!"
        )

        print(
            f"Customer ID: "
            f"{customer.customer_id}"
        )

    except ValueError as error:

        print(f"\nError: {error}")


def create_account_menu(bank):

    print("\n" + "=" * 60)
    print("CREATE ACCOUNT")
    print("=" * 60)

    customer_id = input(
        "Enter customer ID: "
    ).upper()

    print("\n1. Savings Account")
    print("2. Current Account")

    choice = input(
        "Choose account type: "
    )

    if choice == "1":

        account_type = "savings"

    elif choice == "2":

        account_type = "current"

    else:

        print("\nInvalid choice.")
        return

    initial_balance = get_amount()

    try:

        account = bank.create_account(
            customer_id,
            account_type,
            initial_balance
        )

        print(
            "\nAccount created successfully!"
        )

        print(
            f"Account Number: "
            f"{account.account_number}"
        )

    except BankError as error:

        print(f"\nError: {error}")

    except ValueError as error:

        print(f"\nError: {error}")


def deposit_menu(bank):

    print("\n" + "=" * 60)
    print("DEPOSIT MONEY")
    print("=" * 60)

    account_number = input(
        "Enter account number: "
    ).upper()

    amount = get_amount()

    try:

        bank.deposit(
            account_number,
            amount
        )

        print(
            f"\n₹{amount:.2f} deposited successfully."
        )

    except BankError as error:

        print(f"\nError: {error}")


def withdraw_menu(bank):

    print("\n" + "=" * 60)
    print("WITHDRAW MONEY")
    print("=" * 60)

    account_number = input(
        "Enter account number: "
    ).upper()

    amount = get_amount()

    try:

        bank.withdraw(
            account_number,
            amount
        )

        print(
            f"\n₹{amount:.2f} withdrawn successfully."
        )

    except BankError as error:

        print(f"\nError: {error}")


def transfer_menu(bank):

    print("\n" + "=" * 60)
    print("TRANSFER MONEY")
    print("=" * 60)

    sender = input(
        "Enter sender account: "
    ).upper()

    receiver = input(
        "Enter receiver account: "
    ).upper()

    amount = get_amount()

    try:

        bank.transfer(
            sender,
            receiver,
            amount
        )

        print(
            f"\n₹{amount:.2f} transferred successfully."
        )

    except BankError as error:

        print(f"\nError: {error}")

    except ValueError as error:

        print(f"\nError: {error}")


def account_details_menu(bank):

    account_number = input(
        "Enter account number: "
    ).upper()

    try:

        bank.show_account(
            account_number
        )

    except BankError as error:

        print(f"\nError: {error}")


def transaction_menu(bank):

    account_number = input(
        "Enter account number: "
    ).upper()

    try:

        account = bank.find_account(
            account_number
        )

        account.show_transactions()

    except BankError as error:

        print(f"\nError: {error}")


def main():

    bank = Bank(
        "Python OOP Bank"
    )

    while True:

        print("\n")
        print("=" * 70)
        print("              PYTHON OOP BANK")
        print("=" * 70)

        print("1. Create Customer")
        print("2. Create Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Check Account Details")
        print("7. Transaction History")
        print("8. Show All Customers")
        print("9. Show All Accounts")
        print("10. Exit")

        print("=" * 70)

        choice = input(
            "Enter your choice: "
        )

        if choice == "1":

            create_customer_menu(bank)

        elif choice == "2":

            create_account_menu(bank)

        elif choice == "3":

            deposit_menu(bank)

        elif choice == "4":

            withdraw_menu(bank)

        elif choice == "5":

            transfer_menu(bank)

        elif choice == "6":

            account_details_menu(bank)

        elif choice == "7":

            transaction_menu(bank)

        elif choice == "8":

            bank.show_customers()

        elif choice == "9":

            bank.show_all_accounts()

        elif choice == "10":

            print(
                "\nThank you for using "
                "Python OOP Bank!"
            )

            break

        else:

            print(
                "\nInvalid choice."
            )

        pause()


if __name__ == "__main__":
    main()