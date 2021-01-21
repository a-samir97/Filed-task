from flask_restful import reqparse

def payment_request_parser():
    
    '''
    payment parser to parse request data
    '''

    parser =reqparse.RequestParser(bundle_errors=True)
    parser.add_argument('CreditCardNumber', type=str, required=True)
    parser.add_argument('CardHolder', type=str, required=True)
    parser.add_argument('ExpirationDate', type=str, required=True)
    parser.add_argument('SecurityCode', type=str, required=False)
    parser.add_argument('Amount', type=float, required=True)

    return parser
