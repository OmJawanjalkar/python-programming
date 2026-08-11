from datetime import datetime


class Transaction:

    transaction_counter = 1000

    def __init__(self, transaction_type, amount, description=""):
        Transaction.transaction_counter += 1

        self.transaction_id = (
            f"TXN{Transaction.transaction_counter}"
        )

        self.transaction_type = transaction_type
        self.amount = amount
        self.description = description

        self.timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

    def __str__(self):
        return (
            f"{self.transaction_id} | "
            f"{self.transaction_type:<10} | "
            f"₹{self.amount:>10.2f} | "
            f"{self.timestamp} | "
            f"{self.description}"
        )