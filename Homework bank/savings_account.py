"""Imports the Account class from the Account.py file."""
from Account import Account

def create_savings_account(balance, interest_rate, months):
    """Creates a savings account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial savings account balance.
        interest_rate (float): The APR interest rate for the savings account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated savings account balance after adding the interest earned.
        float: The interest earned.
    """
    # Create an instance of the `Account` class
    savings_account = Account(balance, 0)

    # Calculate interest earned
    interest_earned = balance * (interest_rate / 100) * (months / 12)

    # Update the savings account balance
    updated_balance = balance + interest_earned

    # Set the updated balance and interest
    savings_account.set_balance(updated_balance)
    savings_account.set_interest(interest_earned)

    # Return the updated balance and interest earned
    return updated_balance, interest_earned
