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

    return round(total_debit, 2)

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
    print(monthly_withdrawals)
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


[
    {
        "Date": "Oct 2",
        "Description": "Electronic DepositFrom 36 TREAS 3109101036151 MISC PAY431833386360012REF=172750102657000N00",
        "Debit": null,
        "Credit": "7265.00",
        "Balance": null
    },
    {
        "Date": "Oct 2",
        "Description": "Debit Purchase - VISAOn 092917 MISSION KSPANERA BREAD #20REF #24427337272720040130721************8781",
        "Debit": "7.00",
        "Credit": null,
        "Balance": null
    }
]

null must be "0"
keys must be capitalized "Debit"
"""