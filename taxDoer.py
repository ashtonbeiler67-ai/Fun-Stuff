#Calculates simple finance examples with taxes - not meant for legitimate use.

STATE_TAX_RATE = 0.05
COUNTY_TAX_RATE = 0.06
account_balance = 0
state_tax = 0.05
county_tax = 0.06
def calculate_tax(total_amt, state_tax=STATE_TAX_RATE, county_tax=COUNTY_TAX_RATE):
    calculated_state_tax = total_amt * state_tax
    calculated_county_tax = total_amt * county_tax
    calculated_total_tax = calculated_state_tax + calculated_county_tax
    print("total tax:$" + str(calculated_total_tax))
    return calculated_total_tax
def enter_expense():
    global account_balance
    item_name = input("enter expense item name: ")
    item_cost = float(input("enter expense item cost: "))
    item_amt = int(input("enter expense item amount: "))
    total_expense = item_cost * item_amt
    account_balance -= total_expense
    print("Total account balance:$" + str(account_balance))
    print("total expense:$" + str(total_expense))
    print(account_balance)
    
    display()
    return (
        item_name,
        item_cost,
        item_amt,
    
    )
def enter_income():
    global account_balance
    income_name = input("enter income source name: ")
    income_amt = float(input("enter income amount: "))
    print("name of income source:" + income_name)
    print("income amount:$" + str(income_amt))
    diff_county = input("Are you in a different county? (y/n): ")
    if diff_county == "y":
        county_tax = float(input("enter your county tax rate as a decimal: "))
    else:
        county_tax = COUNTY_TAX_RATE
    tax_owed = calculate_tax(income_amt, county_tax=county_tax)
    net_income = income_amt - tax_owed
    account_balance += net_income
    print("account balance:$" + str(account_balance))
    print("state tax:$" + str(income_amt * state_tax))
    print("county tax:$" + str(income_amt * county_tax))
    display()
    return income_name, income_amt
def show_balance():
    print("account balance:$" + str(account_balance))
    display()
def display():
    print("""1. enter an expense \n2. enter an income \n3. show current balance \n4. exit the program""")
    choice = input("enter your choice: ")
    if choice == "1":
        enter_expense()
    elif choice == "2":
        enter_income()
    elif choice == "3":
        show_balance()
    elif choice == "4":
        print("exiting the program.")
    else:
        print("invalid choice")
        display()

def main():
    display()
main()
