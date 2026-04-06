class BankAccount:
    #uses the __init__ method to initiate
    def __init__(self, name, account_num, amount, interest_rate):
        #making storage for all my variables
        self.name = name
        self.acct_num = account_num
        self.amount = str(amount)
        self.interest_rate = str(interest_rate)

    def change_interest_rate(self, new_rate):
        #adds a way to alter the interest
        temp_rate = float(new_rate)
        self.interest_rate = str(temp_rate)

    def deposit(self, amount):
        #makes float values to get the math done and undoes it
        current_balance = float(self.amount)
        new_balance = current_balance + float(amount)
        self.amount = str(new_balance)

    def withdraw(self, amount):
        #checking if the requested withdraw is possible
        if float(self.amount) - float(amount) >= 0:
            self.amount = str(float(self.amount) - float(amount))
        else:
            print("balance is short bro")

    def get_balance(self):
        #gets the balance number
        return float(self.amount)

    def calculate_interest(self, days):
        #compounds the interest every day and returns it
        total_interest = 0
        daily_rate = (float(self.interest_rate) / 365)
        for i in range(int(days)):
            total_interest = total_interest + (float(self.amount) * daily_rate)
        return total_interest

    def __str__(self):
        #uses the __str__ method to display the stuff
        return f"Name: {self.name} Account: {self.acct_num} Balance: {self.get_balance()}"


def test_bank_stuff():
    #initiates account variable
    my_account = BankAccount("John Hodges", "1", 1000000, 0.03)
    print(my_account.__str__())

    #tests sending into the account
    deposit = float(input("How much would you like to deposit?"))
    my_account.deposit(deposit)
    print(f"Depositing ${deposit}")

    #tests taking from account
    withdraw = float(input("How much would you like to withdraw?"))
    my_account.withdraw(withdraw)
    print(f"Withdrawing {withdraw}")

    #calculates all the cash earned from the compounded interest rate
    interest = my_account.calculate_interest(365)
    print("Interest earned in a year: " + str(interest))

    #tests the method to change the interest rate
    interest = float(input("What do you wish your interest rate was?"))
    my_account.change_interest_rate(interest)
    print(f"New interest rate = {interest}")

    #calculates all the cash earned from the new compounded interest rate
    interest = my_account.calculate_interest(365)
    print("Interest earned in a year: " + str(interest))

    #prints the new balance name account number
    print(my_account.__str__())


test_bank_stuff()