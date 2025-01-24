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
    return monthly_withdrawals

def check_balance(data):

    running_balance = data[0].get("Balance")

    for transaction in data:
        income = transaction.get("Credit")
        spendings = transaction.get("Debit")
        running_balance += (income - spendings)
        if running_balance < 500:
            return f"This user is not a good loan recipient. Their balanced dropped to {running_balance}."
        elif running_balance < 1000:
            return f"This user may not be a good loan recipient. Their balanced dropped to {running_balance}."
        else:
            return "This user may be a good loan recipient."
        
    # Iterate through the list of transactions
    # for transaction in data:
    #     # Get the value of 'credit' field
    #     income = transaction.get("Credit")
    #     spendings = transaction.get("Debit")
        
    #     if balance is not None:
    #         try:
    #             # Remove commas and convert the credit value to float
    #             balance_value = float(balance.replace(",", ""))  # Remove commas
    #             if balance_value < 500:
    #                 return f"This user is not a good loan recipient. Their balanced dropped to {balance_value}."
    #             if balance_value < 1500:
    #                 return f"This user may not be a good loan recipient. Their balanced dropped to {balance_value}."
    #         except ValueError:
    #             # If the credit cannot be converted to a number, skip it
    #             continue
    print(running_balance)
    return True

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
            


"""
return a "Starting Balance"
ensure theres no "\" in the description

[
    {
        "Date": "Oct 2",
        "Description": "Electronic DepositFrom 36 TREAS 3109101036151 MISC PAY431833386360012REF=172750102657000N00",
        "Debit": "0",
        "Credit": "7265.00",
        "Balance": "0"
    },
    {
        "Date": "Oct 2",
        "Description": "Debit Purchase - VISAOn 092917 MISSION KSPANERA BREAD #20REF #24427337272720040130721************8781",
        "Debit": "7.00",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 2",
        "Description": "Customer Withdrawal",
        "Debit": "500.00",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 2",
        "Description": "Check 4670",
        "Debit": "1146.08",
        "Credit": "0",
        "Balance": "16522.58"
    },
    {
        "Date": "Oct 2",
        "Description": "Check 4672",
        "Debit": "70.00",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 3",
        "Description": "Electronic DepositFrom 36 TREAS 3109101036151 MISC PAY431833386360012REF 172760027363140N00",
        "Debit": "0",
        "Credit": "6400.00",
        "Balance": "22922.58"
    },
    {
        "Date": "Oct 4",
        "Description": "Electronic DepositFrom CGS ADMINISTATORREF=172720058223180Y006202552297HCCLAIMPMT267605",
        "Debit": "0",
        "Credit": "11911.98",
        "Balance": "0"
    },
    {
        "Date": "Oct 4",
        "Description": "Debit Purchase - VISAOn 100317 WWW.SOS.MO.G MOMO SEC OF STATEREF #24540457277235570575040************8781",
        "Debit": "51.25",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 4",
        "Description": "Check 4683",
        "Debit": "3000.00",
        "Credit": "0",
        "Balance": "31783.31"
    },
    {
        "Date": "Oct 6",
        "Description": "Debit Purchase - VISAOn 100517 800-5563012 KSFREDPRYOR CAREERREF # 24906417278045224965328************8781",
        "Debit": "149.00",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 6",
        "Description": "Electronic WithdrawalTo BlueKc Com Stimt4431257251WEB PYMNT 38589255REF=172780089093620N00",
        "Debit": "195.34",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 6",
        "Description": "Check 4678",
        "Debit": "228.00",
        "Credit": "0",
        "Balance": "28906.37"
    },
    {
        "Date": "Oct 6",
        "Description": "Check 4682",
        "Debit": "1804.60",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 10",
        "Description": "Debit Purchase - VISAOn 100617816-7638200 ΜΟREF #24183107279900014900051THE PLUMBING PRO************8781",
        "Debit": "372.00",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 10",
        "Description": "Check 4671",
        "Debit": "1146.08",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 10",
        "Description": "Check 4685",
        "Debit": "379.26",
        "Credit": "0",
        "Balance": "27009.03"
    },
    {
        "Date": "Oct 11",
        "Description": "Electronic DepositFrom CGS ADMINISTATORREF=172780042278970Y006202552297HCCLAIMPMT267605",
        "Debit": "0",
        "Credit": "4972.84",
        "Balance": "0"
    },
    {
        "Date": "Oct 11",
        "Description": "Check 4675",
        "Debit": "200.00",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 11",
        "Description": "Check 4676",
        "Debit": "2500.00",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 11",
        "Description": "Check 4679",
        "Debit": "754.99",
        "Credit": "0",
        "Balance": "28526.88"
    },
    {
        "Date": "Oct 12",
        "Description": "Electronic DepositFrom 36 TREAS 310REF=172850024413210N009101036151 MISC PAY431833386360012",
        "Debit": "0",
        "Credit": "4510.00",
        "Balance": "0"
    },
    {
        "Date": "Oct 12",
        "Description": "Electronic DepositFrom CGS ADMINISTATOR6202552297HCCLAIMPMT267605REF=172790122999750Y00",
        "Debit": "0",
        "Credit": "5597.43",
        "Balance": "0"
    },
    {
        "Date": "Oct 12",
        "Description": "Branch Account TransferTo Account 145574108240",
        "Debit": "8000.00",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 12",
        "Description": "Branch Account TransferTo Account 145570459670",
        "Debit": "12000.00",
        "Credit": "0",
        "Balance": "18634.31"
    },
    {
        "Date": "Oct 13",
        "Description": "Check 4699",
        "Debit": "450.00",
        "Credit": "0",
        "Balance": "18184.31"
    },
    {
        "Date": "Oct 16",
        "Description": "Electronic DepositFrom 36 TREAS 3109101036151 MISC PAY431833386360012REF=172890066691320N00",
        "Debit": "0",
        "Credit": "2641.08",
        "Balance": "0"
    },
    {
        "Date": "Oct 16",
        "Description": "Electronic WithdrawalFrom PHILA INS COREF=172890065018750N002316092819INS IN 80092172",
        "Debit": "5.00",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 16",
        "Description": "Analysis Service Charge",
        "Debit": "24.95",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 16",
        "Description": "Electronic WithdrawalFrom PHILA INS COREF=172890065018740N002316092819INS IN 80092172",
        "Debit": "7514.68",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 16",
        "Description": "Check 4667",
        "Debit": "3777.34",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 16",
        "Description": "Check 4680",
        "Debit": "33.23",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 16",
        "Description": "Check 4695",
        "Debit": "3341.36",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 16",
        "Description": "Check 4696",
        "Debit": "118.50",
        "Credit": "0",
        "Balance": "5815.27"
    },
    {
        "Date": "Oct 17",
        "Description": "Electronic DepositFrom CGS ADMINISTATORREF=172850047281610Y006202552297HCCLAIMPMT267605",
        "Debit": "0",
        "Credit": "3036.78",
        "Balance": "0"
    },
    {
        "Date": "Oct 17",
        "Description": "Check 4677",
        "Debit": "320.00",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 17",
        "Description": "Check 4692",
        "Debit": "726.37",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 17",
        "Description": "Check 4693",
        "Debit": "110.00",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 17",
        "Description": "Check 4697",
        "Debit": "78.65",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 17",
        "Description": "Check 4701",
        "Debit": "320.00",
        "Credit": "0",
        "Balance": "7297.03"
    },
    {
        "Date": "Oct 19",
        "Description": "Check 4690",
        "Debit": "995.00",
        "Credit": "0",
        "Balance": "0"
    },
    {
        "Date": "Oct 19",
        "Description": "Check 4691",
        "Debit": "34.55",
        "Credit": "0",
        "Balance": "6267.48"
    },
    {
        "Date": "Oct 20",
        "Description": "Electronic DepositFrom 36 TREAS 3109101036151 MISC PAY431833386360012REF=172920112272070N00",
        "Debit": "0",
        "Credit": "760.00",
        "Balance": "0"
    },
    {
        "Date": "Oct 20",
        "Description": "Electronic DepositFrom CGS ADMINISTATORREF=172900111651190Y006202552297HCCLAIMPMT267605",
        "Debit": "0",
        "Credit": "11414.48",
        "Balance": "0"
    },
    {
        "Date": "Oct 20",
        "Description": "Check 4687",
        "Debit": "287.66",
        "Credit": "0",
        "Balance": "18154.30"
    },
    {
        "Date": "Oct 23",
        "Description": "Electronic DepositFrom 36 TREAS 310REF=172960092179570N009101036151 MISC PAY431833386360012",
        "Debit": "0",
        "Credit": "3150.00",
        "Balance": "21304.30"
    },
    {
        "Date": "Oct 24",
        "Description": "Electronic DepositFrom CGS ADMINISTATORREF=172920071406510Y006202552297HCCLAIMPMT267605",
        "Debit": "0",
        "Credit": "305.71",
        "Balance": "0"
    },
    {
        "Date": "Oct 24",
        "Description": "Electronic DepositFrom 36 TREAS 3109101036151MISC PAY431833386360012EF=172960187647050N00",
        "Debit": "0",
        "Credit": "660.00",
        "Balance": "22270.01"
    },
    {
        "Date": "Oct 25",
        "Description": "Electronic DepositFrom CGS ADMINISTATORREF 172930041655740Y006202552297HCCLAIMPMT267605",
        "Debit": "0",
        "Credit": "11572.01",
        "Balance": "0"
    },
    {
        "Date": "Oct 25",
        "Description": "Electronic WithdrawalFrom ATTREF 172970047495440N009864031006Payment 401469002EPAYQ",
        "Debit": "308.48",
        "Credit": "0",
        "Balance": "0"
    }]
    """