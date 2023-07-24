# python creditcalc.py --type=diff --payment=1000000 --periods=10
# --interest=10
import argparse
import math
import sys
from argparse import Namespace


def calculate_annuity(loan_principal=None, monthly_payment=None, number_of_periods=None, loan_interest=None):

    #Do the calculations according to the selection:
    interest = float(loan_interest)/(12*100.)

    if number_of_periods is not None: #if selection != 'n':
        np = int(number_of_periods)
        temp1 = math.pow(1+interest, np)
        temp2 = interest * temp1 / (temp1 - 1)

        if loan_principal is None: # selection == 'p': #calculate loan_principal
            mp = float(monthly_payment)
            lp = math.floor(mp / temp2)
            print('Your loan principal = ' + str(lp) + '!')
        elif monthly_payment is None: #selection == 'a': #calculate monthly_payment
            lp = float(loan_principal)
            mp = math.ceil(lp * temp2)
            print('Your monthly payment = ' + str(mp) + '!')
    elif number_of_periods is None: #selection == 'n': #calculate number_of_periods
        mp = float(monthly_payment)
        lp = float(loan_principal)
        temp = mp/(mp - interest * lp)
        print(str(temp) + '  ' + str(interest))
        np = math.ceil(math.log(temp, 1+interest))
        years = math.floor(np/12)
        years_part = ''
        months_part = ''
        if years == 1:
            years_part = '1 year'
        elif years > 1:
            years_part = str(years) + ' years'
        if np != 0:
            if years_part != '':
                months_part += ' and '
            months_part += str (np%12) + (' month' if np == 1 else ' months')
        print ('It will take ' + years_part + months_part + ' to repay this loan!')
    return mp * np - lp

parser = argparse.ArgumentParser('Arguments: --type=diff --payment=1000000 --periods=10 \
 --interest=10')
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--periods")
parser.add_argument("--interest")
parser.add_argument("--principal")

args: Namespace = parser.parse_args()
args_error = 0
nargs = 0

if args.type == None:
    print('Incorrect parameters')
    sys.exit(0)
else:
    type = str(args.type)

if (type == 'annuity'):
    if args.principal is not None:
        nargs += 1
        if float(args.principal) < 0:
            args_error += 1
    if args.interest is not None:
        nargs += 1
        if float(args.interest) < 0:
            args_error += 1
    if args.periods is not None:
        nargs += 1
        if int(args.periods) < 0:
            args_error += 1
    if args.payment is not None:
        nargs += 1
        if float(args.payment) < 0:
            args_error += 1
    if nargs < 3 or args_error > 0:
        print('Incorrect parameters')
        sys.exit(0)

    ovp = calculate_annuity(args.principal, args.payment, args.periods, args.interest)
    print('Overpayment = ', str(math.ceil(ovp)))

elif (args.type == 'diff') and \
    (args.principal is not None) and \
    (args.periods is not None) and \
    (args.interest is not None):

    p = float(args.principal)
    n = int(args.periods)
    i = float(args.interest) / (12 * 100.)
    if p < 0 or n < 0 or i < 0:
        print('Incorrect parameters')
        sys.exit(0)

    # calculate monthly payments for each month
    total_payment = 0
    for m in range(1, n+1):
        diff_payment = math.ceil(p/n + i * (p - p * (m - 1) / n))
        total_payment += diff_payment
        print('Month ' + str(m) + ': payment is ' + str(diff_payment))

    print('Overpayment = ', str(math.ceil(total_payment - p)))

else:
    print('Incorrect parameters')






