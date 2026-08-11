class Customer:

    # Class variable
    customer_counter = 1000

    def __init__(self, name, email, phone):

        Customer.customer_counter += 1

        self.customer_id = (
            f"CUST{Customer.customer_counter}"
        )

        self.name = name
        self.email = email
        self.phone = phone

        # Composition
        self.accounts = []

    def add_account(self, account):

        self.accounts.append(account)

    def show_accounts(self):

        if not self.accounts:
            print("\nNo accounts found.")
            return

        print("\n" + "=" * 60)
        print("CUSTOMER ACCOUNTS")
        print("=" * 60)

        for account in self.accounts:

            print(
                f"Account: {account.account_number} | "
                f"Type: {account.__class__.__name__} | "
                f"Balance: ₹{account.get_balance():.2f}"
            )

    def __str__(self):

        return (
            f"\nCustomer ID : {self.customer_id}\n"
            f"Name        : {self.name}\n"
            f"Email       : {self.email}\n"
            f"Phone       : {self.phone}\n"
            f"Accounts    : {len(self.accounts)}"
        )