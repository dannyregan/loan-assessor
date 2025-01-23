from flask import Flask, request, jsonify
from flask_cors import CORS

from utils import sum_debits
from utils import sum_credits
from utils import check_balance
from utils import total_monthly_deposits
from utils import total_monthly_withdrawals

app = Flask(__name__)
CORS(app)

@app.route('/process_json', methods=['POST'])
def process_json():
    """Process JSON data and calculate total debit."""
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Print the incoming data for debugging
        print("Received data:")

        # Check if data is a list or dictionary
        if isinstance(data, list):
            # Calculate the total debit
            total_debit = sum_debits(data)
            total_credit = sum_credits(data)
            balance_check = check_balance(data)
            monthly_deposits = total_monthly_deposits(data)
            monthly_withdrawals = total_monthly_withdrawals(data)


            # Respond with the total debit
            return jsonify({"total_debit": total_debit, "total_credit": total_credit, "balance_check": balance_check, "Monthly Deposits": monthly_deposits, "Monthly Withdrawals": monthly_withdrawals}), 200
        else:
            return jsonify({"error": "Expected a list of transactions"}), 400

    except Exception as e:
        return jsonify({"error": f"Error processing the data: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)


"""
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
 """