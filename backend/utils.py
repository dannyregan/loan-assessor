def sum_debits(data):
    total_debit = 0

    # Iterate through the list of transactions
    for transaction in data:
        # Get the value of 'Debit' field
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