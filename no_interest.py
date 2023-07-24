import math
loan_principal=int(input("Enter the loan principal:"))
selection = 'False'
while not (selection == "m" or selection == "p"):
    selection = input ( 'What do you want to calculate?' +
    '\ntype "m" - for number of monthly payments,' +
    '\ntype "p" - for the monthly payment:')

if selection == 'm':
    monthly_payment = int(input('Enter the monthly payment:'))
    number_of_monthly_payments = math.ceil(loan_principal/monthly_payment)
    print ('It will take ' + str (number_of_monthly_payments) +
           (' month' if number_of_monthly_payments == 1  else ' months') +
            ' to repay the loan')
elif selection == 'p':
    number_of_months = int (input ('Enter the number of months:'))
    monthly_payment = math.ceil (loan_principal/(number_of_months))
    last_payment = loan_principal - (number_of_months-1) * monthly_payment
    print ('Your monthly payment = ' + str(monthly_payment) +
           (' and the last payment = ' + str (last_payment) + '.' if
           monthly_payment != last_payment else ''))







