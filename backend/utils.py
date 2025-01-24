def sum_debits(data):
    total_debit = 0

    for transaction in data:
        debit = transaction.get("Debit")
        
        if debit is not None:
            try:
                debit_value = float(debit.replace(",", ""))  
                total_debit += debit_value
            except ValueError:
                continue

    return round(total_debit, 2)

def sum_credits(data):
    total_credit = 0

    for transaction in data:
        credit = transaction.get("Credit")
        
        if credit is not None:
            try:
                credit_value = float(credit.replace(",", ""))
                total_credit += credit_value
            except ValueError:
                continue

    return round(total_credit, 2)

def total_monthly_deposits(data):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthly_deposits = {}
    
    for transaction in data:
        date = transaction.get("Date")
        deposit = float(transaction.get("Credit"))
        if date and deposit:
            date = date.split(" ")
            for item in date:
                if item in months:
                    monthly_deposits[item] = round(monthly_deposits.get(item, 0) + deposit, 2)
    return monthly_deposits

def total_monthly_withdrawals(data):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthly_withdrawals = {}
    
    for transaction in data:
        date = transaction.get("Date")
        withdrawal = round(float(transaction.get("Debit")), 2)
        if date and withdrawal:
            date = date.split(" ")
            for item in date:
                if item in months:
                    monthly_withdrawals[item] = round(monthly_withdrawals.get(item, 0) + withdrawal, 2)
    return monthly_withdrawals

def check_balance(data):

    running_balance = float(data[0].get("Balance"))

    for transaction in data:
        income = float(transaction.get("Credit"))
        spendings = float(transaction.get("Debit"))
        running_balance += (income - spendings)
        if running_balance < 500:
            return f"Unlikely. Very low balance"
        elif running_balance < 1000:
            return f"Maybe. Low balance"
        else:
            return "Likely."

def monthly_cashflow(data):
    deposits = total_monthly_deposits(data)
    withdrawals = total_monthly_withdrawals(data)

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthly_cashflows = {}

    for month in months:
        if month in deposits and month in withdrawals:
            monthly_cashflows[month] = round(deposits[month] - withdrawals[month], 2)
        elif month in deposits:
            monthly_cashflows[month] = deposits[month]
            print(deposits[month], "monthly deposit")
        elif month in withdrawals:
            monthly_cashflows[month] = round(0 - withdrawals[month], 2)
    return monthly_cashflows