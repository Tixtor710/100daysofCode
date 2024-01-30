def main():
    print("This is monthly payment Loan Calculator")
    print("")

    principal= float(input("Input the Loan Amount: "))
    apr = float(input("Enter The annual interest Rate: "))
    years = float(input("Enter Number of years: "))


    monthly_interest_rate= apr / 1200
    amount_of_months= years*12
    monthly_payment= principal * monthly_interest_rate/ (1-(1+monthly_interest_rate)**(-amount_of_months))    
    print("The Monthly payment for your loan is : "+str(monthly_payment))

main()