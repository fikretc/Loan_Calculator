# interested in four values:
# the number of monthly payments required to repay the loan,
# the monthly payment amount,
# the loan principal,
# and the loan interest.
import math

def calculate_annuity(loan_principal=None, monthly_payment=None, number_of_periods=None, loan_interest=None):
    #Do the calculations according to the selection:
    interest = loan_interest/(12*100.)

    if number_of_periods != None: #if selection != 'n':
        temp1 = math.pow(1+interest,number_of_periods)
        temp2 = interest * temp1 / (temp1 - 1)

        if loan_principal == None: # selection == 'p': #calculate loan_principal
            loan_principal = math.floor(monthly_payment / temp2)
            print ('Your loan principal = ' + str(loan_principal) + '!')
        elif monthly_payment == None: #selection == 'a': #calculate monthly_payment
            monthly_payment = math.ceil(loan_principal * temp2)
            print ('Your monthly payment = ' + str(monthly_payment) + '!')
    elif number_of_periods ==None: #selection == 'n': #calculate number_of_periods
        temp = monthly_payment/(monthly_payment - interest * loan_principal)
        print(str(temp) + '  ' + str(interest))
        number_of_periods = math.ceil(math.log(temp, 1+interest))
        years = math.floor(number_of_periods/12)
        years_part = ''
        months_part = ''
        if years == 1:
            years_part = '1 year'
        else:
            years_part = str(years) + ' years'
        if number_of_periods != 0:
            if years_part != '':
                months_part += ' and '
            months_part += str (number_of_periods%12) + (' month' if number_of_periods == 1 else ' months')
        print ('It will take ' + years_part + months_part + ' to repay this loan!')
    return monthly_payment * number_of_periods - loan_principal



selection = 'False'
while selection not in ['n', 'a', 'p']:
    selection = input('What do you want to calculate?' +
        '\ntype "n" for number of monthly payments,' +
        '\ntype "a" for annuity monthly payment amount,' +
        '\ntype "p" for loan principal:\n')

loan_principal = monthly_payment = number_of_periods = loan_interest = None

if selection != 'p':
    loan_principal = float(input('Enter the loan principal:\n'))
if selection != 'a':
    monthly_payment = float (input('Enter the monthly payment:\n'))
if selection != 'n':
    number_of_periods = int (input('Enter the number of periods:\n'))
loan_interest = float (input('Enter the loan interest:\n'))

calculate_annuity(loan_principal, monthly_payment, number_of_periods, loan_interest)





