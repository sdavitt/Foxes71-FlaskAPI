from flask import Blueprint, jsonify, request
import stripe
import os

payment = Blueprint('payment', __name__)

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')

@payment.route('/pay', methods=['POST'])
def pay():
    """
    Receives payment amount from react app (client)
    creates paymentIntent by communicating with stripe
    returns the required client secret
    """
    try:
        data = request.get_json()
        print(data)
        intent = stripe.PaymentIntent.create(
            amount=data['amount'],
            currency='usd'
        )
        print(intent)
        return jsonify(client_secret=intent.client_secret)
    except Exception as e:
        return jsonify(error=str(e)), 403
