from functools import reduce

#make my function to loop inputs and throw it into the list every time
def get_expenses():
    #make the list
    expenses = []
    #info for user
    print("Type your expenses this month. To end, type end. ")
    #inputting/list appending loop
    while True:
        #inputting part
        name = input("Input the type of expense: ").strip()
        if name.lower() == 'end':
            break

        amount = float(input(f"Enter amount for {name}: "))

        #appending the list part
        expenses.append({'name': name, 'amount': amount})

    return expenses


def analyze_expenses(expenses):

    #get the total with lambda
    total = reduce(lambda acc, x: acc + x['amount'], expenses, 0)

    #get the highest with lamda
    highest = reduce(lambda a, b: a if a['amount'] > b['amount'] else b, expenses)

    #lambda for the lowest as well.
    lowest = reduce(lambda a, b: a if a['amount'] < b['amount'] else b, expenses)

    #output results
    print(f"Your lowest expense was {lowest['name']} ${lowest['amount']}")
    print(f"Your highest expense was {highest['name']} ${highest['amount']})")
    print(f"Total expenses ${total}")

user_expenses = get_expenses()
analyze_expenses(user_expenses)