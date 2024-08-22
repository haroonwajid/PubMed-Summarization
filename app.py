from flask import Flask, request, jsonify

app = Flask(__name__)

# Example conversion rates (you can replace these with real-time rates)
conversion_rates = {
    "USD": {"EUR": 0.85, "PKR": 282.25},
    "EUR": {"USD": 1.18, "PKR": 331.50},
    "PKR": {"USD": 0.0035, "EUR": 0.0030}
}

@app.route('/convert', methods=['POST'])
def convert_currency():
    data = request.json

    # Check if all required fields are present
    if not all(key in data for key in ('amount', 'from_currency', 'to_currency')):
        return jsonify({"error": "Missing required parameters"}), 400

    try:
        amount = float(data['amount'])
    except ValueError:
        return jsonify({"error": "Invalid amount"}), 400

    from_currency = data['from_currency'].upper()
    to_currency = data['to_currency'].upper()

    # Check if the currencies are supported
    if from_currency not in conversion_rates or to_currency not in conversion_rates[from_currency]:
        return jsonify({"error": "Unsupported currency"}), 400

    # Fetch conversion rate
    conversion_rate = conversion_rates[from_currency][to_currency]

    # Calculate converted amount
    converted_amount = round(amount * conversion_rate, 2)

    return jsonify({
        "amount": amount,
        "from_currency": from_currency,
        "to_currency": to_currency,
        "converted_amount": converted_amount
    })

if __name__ == '__main__':
    app.run(debug=True)
