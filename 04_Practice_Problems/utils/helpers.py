def get_amount():

    while True:

        try:

            amount = float(
                input("Enter amount: ₹")
            )

            if amount <= 0:
                print(
                    "Amount must be greater than zero."
                )
                continue

            return amount

        except ValueError:

            print(
                "Please enter a valid number."
            )


def pause():

    input(
        "\nPress Enter to continue..."
    )