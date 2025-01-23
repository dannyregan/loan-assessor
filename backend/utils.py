def sum_debits(data):
    total_debit = 0

    # Iterate through the list of transactions
    for transaction in data:
        # Get the value of 'debit' field
        debit = transaction.get("Debit")
        
        if debit is not None:
            try:
                # Remove commas and convert the debit value to float
                debit_value = float(debit.replace(",", ""))  # Remove commas
                total_debit += debit_value
            except ValueError:
                # If the debit cannot be converted to a number, skip it
                continue

    return total_debit

def sum_credits(data):
    total_credit = 0

    # Iterate through the list of transactions
    for transaction in data:
        # Get the value of 'credit' field
        credit = transaction.get("Credit")
        
        if credit is not None:
            try:
                # Remove commas and convert the credit value to float
                credit_value = float(credit.replace(",", ""))  # Remove commas
                total_credit += credit_value
            except ValueError:
                # If the credit cannot be converted to a number, skip it
                continue

    return total_credit

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
                    monthly_deposits[item] = monthly_deposits.get(item, 0) + deposit
    return monthly_deposits

def total_monthly_withdrawals(data):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    monthly_withdrawals = {}
    
    for transaction in data:
        date = transaction.get("Date")
        withdrawal = float(transaction.get("Debit"))
        if date and withdrawal:
            date = date.split(" ")
            for item in date:
                if item in months:
                    monthly_withdrawals[item] = monthly_withdrawals.get(item, 0) + withdrawal
    return monthly_withdrawals

def check_balance(data):
    # Iterate through the list of transactions
    for transaction in data:
        # Get the value of 'credit' field
        balance = transaction.get("Balance")
        
        if balance is not None:
            try:
                # Remove commas and convert the credit value to float
                balance_value = float(balance.replace(",", ""))  # Remove commas
                if balance_value < 500:
                    return f"This user is not a good loan recipient. Their balanced dropped to {balance_value}."
                if balance_value < 1500:
                    return f"This user may not be a good loan recipient. Their balanced dropped to {balance_value}."
            except ValueError:
                # If the credit cannot be converted to a number, skip it
                continue

    return True



"""
[ 
    {
        "Date": "Oct 25",
        "Description": "Electronic WithdrawalFrom ATTREF 172970047495440N009864031006Payment 401469002EPAYQ",
        "Debit": "308.48",
        "Credit": "100",
        "Balance": null
    },
    {
        "Date": "Oct 25",
        "Description": "Branch Account TransferTo Account 145574108240",
        "Debit": "7700.00",
        "Credit": "50",
        "Balance": null
    }
]
"""