from flask import Flask, request, jsonify
from flask_cors import CORS

from utils import sum_debits
from utils import sum_credits
from utils import check_balance
from utils import total_monthly_deposits

app = Flask(__name__)
CORS(app)

@app.route('/process_json', methods=['POST'])
def process_json():
    """Process JSON data and calculate total debit."""
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Print the incoming data for debugging
        print("Received data:", data)

        # Check if data is a list or dictionary
        if isinstance(data, list):
            # Calculate the total debit
            total_debit = sum_debits(data)
            total_credit = sum_credits(data)
            balance_check = check_balance(data)
            monthly_deposits = total_monthly_deposits(data)


            # Respond with the total debit
            return jsonify({"total_debit": total_debit, "total_credit": total_credit, "balance_check": balance_check, "monthly_deposits": monthly_deposits}), 200
        else:
            return jsonify({"error": "Expected a list of transactions"}), 400

    except Exception as e:
        return jsonify({"error": f"Error processing the data: {str(e)}"}), 400

if __name__ == '__main__':
    app.run(debug=True)
