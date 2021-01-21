from flask_restful import Resource

from parsers import payment_request_parser
from validators import (
    validate_credit_card_number, 
    validate_expiration_date,
    validate_card_holder,
    validate_amount
)

from payment_gatway import process_payment

class ProcessPayment(Resource):
    '''
    - CreditCardNumber (mandatory, string, it should be a valid credit card number)
    - CardHolder: (mandatory, string)
    - ExpirationDate (mandatory, DateTime, it cannot be in the past)
    - SecurityCode (optional, string, 3 digits)
    - Amount (mandatoy decimal, positive amount)    
    '''

    def __init__(self):
        self.args = payment_request_parser()

    def post(self):
        args = self.args.parse_args()

        # validation 
        validate_credit_card_number(args['CreditCardNumber'])
        validate_expiration_date(args['ExpirationDate'])
        validate_card_holder(args['CardHolder'])
        validate_amount(args['Amount'])

        # processing payment gateway
        response = process_payment(args['Amount'])
        return response