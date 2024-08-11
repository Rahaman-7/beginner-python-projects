# 1. Create a function to calculate finances
def calculate_finances(monthly_income: float,expenses: float, tax_rate: float, currency: str) -> None:
    # 2. Do the math for each field
    yearly_salary: float = (monthly_income - expenses)  * 12
    monthly_tax: float = monthly_income * (tax_rate / 100)
    yearly_tax: float = monthly_tax * 12
    monthly_net_income: float = (monthly_income - expenses) - monthly_tax
    yearly_net_income: float = yearly_salary - yearly_tax

    # 3. Format the information nicely for the user
    print('--------------------------------')
    print(f'Monthly income: {currency}{monthly_income:,.2f}')
    print(f'Tax rate: {tax_rate:,.0f}%')
    print(f'Monthly tax: {currency}{monthly_tax:,.2f}')
    print(f'Monthly net income: {currency}{monthly_net_income:,.2f}')
    print(f'Yearly salary: {currency}{yearly_salary:,.2f}')
    print(f'Yearly tax paid: {currency}{yearly_tax:,.2f}')
    print(f'Yearly net income: {currency}{yearly_net_income:,.2f}')
    print('--------------------------------')


# 4. Create a main entry point for the program
def main() -> None:
    # 5. Gather user input
    while True:
        try:
            monthly_income = float(input('Enter your monthly income: '))
            expenses = float(input('Enter your monthly Expenses like (Rent,Food,GYM memebershipetc..): '))
            tax_rate = float(input('Enter your tax rate (%): '))
            currency = input("Enter the currency(ex, USD,KR,YEN..): ")
            break # Exit the loop if the conversion is successful
        except ValueError:
            print('Invalid input, Please input a valid monthly income,tax rate and currency')

    # 6. Call the function
    calculate_finances(monthly_income,expenses, tax_rate, currency)


# 7. Run the script
if __name__ == "__main__":
    main()
