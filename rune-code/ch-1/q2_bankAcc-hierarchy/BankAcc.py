"""
Construct a class hierarchy for bank accounts.

Now the way I thought about it:
1. Actors: Customer/Borrower, Bank/Lender

2. What does each actor need? : 
    This one really stumped because I couldn't find by what name to unify these two actors I proposed. Originally I thought a parent called "User" could be inherited by the two, but that felt too generic.
    - What attributes might a lender have? (I was stumped here as well)
    In the interest of keeping it quick, the idea was to come up with the simplest hierarchy.

    Borrower attributes: account_num, name, dob, email
    Lender attributes: location, branch_code, offers/features

3. What behaviours might each actor have? 
    i. Borrower : check_balance, deposit, withdraw
    ii. Lender : charge_fee, lend_money/disburse/loan
"""

from abc import ABC, abstractmethod
from datetime import date
from typing import List

# ─── Actors ────────────────────────────────────────────────────────────────────

class Participant(ABC):
    def __init__(self, name: str, participant_id: str):
        self.name = name
        self.id = participant_id

class Customer(Participant):
    def __init__(self,
                 name: str,
                 customer_id: str,
                 dob: date,
                 email: str):
        super().__init__(name, customer_id)
        self.dob = dob
        self.email = email
        self.accounts: List[BankAccount] = []

    def open_account(self, account: "BankAccount"):
        self.accounts.append(account)

    def get_total_balance(self) -> float:
        return sum(ac.balance for ac in self.accounts)

class BankBranch(Participant):
    def __init__(self,
                 name: str,
                 branch_code: str,
                 location: str,
                 services_offered: List[str]):
        super().__init__(name, branch_code)
        self.location = location
        self.services = services_offered

    def approve_loan(self, loan_account: "LoanAccount"):
        # some eligibility logic…
        loan_account.status = "Approved"

    def charge_fee(self, account: "BankAccount", amount: float):
        account.withdraw(amount)

# ─── Accounts ─────────────────────────────────────────────────────────────────

class BankAccount(ABC):
    def __init__(self, account_number: str, owner: Customer):
        self.account_number = account_number
        self.owner = owner
        self.balance = 0.0

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    @abstractmethod
    def account_type(self) -> str:
        ...

class CheckingAccount(BankAccount):
    def __init__(self,
                 account_number: str,
                 owner: Customer,
                 overdraft_limit: float,
                 monthly_fee: float):
        super().__init__(account_number, owner)
        self.overdraft_limit = overdraft_limit
        self.monthly_fee = monthly_fee

    def account_type(self) -> str:
        return "Checking"

class SavingsAccount(BankAccount):
    def __init__(self,
                 account_number: str,
                 owner: Customer,
                 interest_rate: float):
        super().__init__(account_number, owner)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self.balance *= 1 + self.interest_rate

    def account_type(self) -> str:
        return "Savings"

class LoanAccount(BankAccount):
    def __init__(self,
                 account_number: str,
                 owner: Customer,
                 principal: float,
                 interest_rate: float,
                 term_years: int):
        super().__init__(account_number, owner)
        self.principal = principal
        self.interest_rate = interest_rate
        self.term_years = term_years
        self.status = "Pending"

    def make_payment(self, amount: float):
        self.withdraw(amount)
        self.principal -= amount

    def account_type(self) -> str:
        return "Loan"
