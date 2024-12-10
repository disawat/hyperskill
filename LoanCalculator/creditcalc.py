import argparse
import math

def cal_annu_payment(principal, periods, interest):
    i = interest / 12 / 100
    payment = math.ceil(principal * (i * (1 + i) ** periods) / ((1 + i) ** periods - 1))
    return payment

def cal_annu_principal(payment, periods, interest):
    i = interest / 12 / 100
    principal = payment / (i * (1 + i) ** periods / ((1 + i) ** periods - 1))
    return principal

def cal_annu_periods(principal, payment, interest):
    i = interest / 12 / 100
    periods = math.ceil(math.log(payment / (payment - i * principal), 1 + i))
    return periods

def calculate_diff_payments(principal, periods, interest):
    i = interest / 12 / 100
    payments = []
    for m in range(1, periods + 1):
        payment = math.ceil(principal / periods + i * (principal - (principal * (m - 1) / periods)))
        payments.append(payment)
    return payments

def periods_to_years_months(periods):
    years = periods // 12
    months = periods % 12
    if years > 0 and months > 0:
        return f"{years} years and {months} months"
    elif years > 0:
        return f"{years} year{'s' if years > 1 else ''}"
    else:
        return f"{months} month{'s' if months > 1 else ''}"

def validate_inputs(args):
    if args.type not in ["annuity", "diff"]:
        return False
    elif args.interest is None:
        return False
    elif args.principal is not None and args.principal < 0:
        return False
    elif args.payment is not None and args.payment < 0:
        return False
    elif args.periods is not None and args.periods < 0:
        return False
    elif args.interest is not None and args.interest < 0:
        return False
    elif args.type == "diff" and args.payment is not None:
        return False
    elif args.type == "diff" and sum(arg is not None for arg in [args.principal, args.periods, args.interest]) < 3:
        return False
    return True

parser = argparse.ArgumentParser(description="Loan Calculator")
parser.add_argument("--type", help="Type of payment: 'annuity' or 'differentiate'")
parser.add_argument("--payment", type=float, help="Monthly payment amount (for annuity only)")
parser.add_argument("--principal", type=float, help="Loan principal")
parser.add_argument("--periods", type=int, help="Number of months needed to repay the loan")
parser.add_argument("--interest", type=float, help="Annual interest rate (without % sign)")

args = parser.parse_args()

if not validate_inputs(args):
    print("Incorrect parameters")

elif args.type == "annuity":
    if args.principal and args.payment and args.interest:
        periods = cal_annu_periods(args.principal, args.payment, args.interest)
        time_string = periods_to_years_months(periods)
        overpayment = int(args.payment * periods - args.principal)
        print(f"It will take {time_string} to repay this loan!")
        print(f"Overpayment = {overpayment}")
    elif args.principal and args.periods and args.interest:
        payment = cal_annu_payment(args.principal, args.periods, args.interest)
        overpayment = int(payment * args.periods - args.principal)
        print(f"Your monthly payment = {payment}!")
        print(f"Overpayment = {overpayment}")
    elif args.payment and args.periods and args.interest:
        principal = math.floor(cal_annu_principal(args.payment, args.periods, args.interest))
        overpayment = int(args.payment * args.periods - principal)
        print(f"Your loan principal = {principal}!")
        print(f"Overpayment = {overpayment}")
elif args.type == "diff":
    payments = calculate_diff_payments(args.principal, args.periods, args.interest)
    for month, payment in enumerate(payments, 1):
        print(f"Month {month}: payment is {payment}")
    overpayment = int(sum(payments) - args.principal)
    print(f"Overpayment = {overpayment}")