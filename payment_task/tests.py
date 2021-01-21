import unittest
from app import app

class PaymentProcessTests(unittest.TestCase):
    def setUp(self):
        '''
            set up function to make unit tests
        '''
        app.config['TESTING'] = True
        app.config['DEBUG'] = False

        self.app = app.test_client()

    #### Start Test With Empty Data ####

    def test_with_empty_credit_card_number(self):
        data = {
            'CreditCardNumber': '',
            'CardHolder': 'TEST TEST',
            'ExpirationDate': '10-2022',
            'Amount': 19.5
        }

        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'please add valid credit card number')

    def test_with_empty_card_holder(self):
        data = {
            'CreditCardNumber': '1234567891234567',
            'CardHolder': '',
            'ExpirationDate': '10-2022',
            'Amount': 19.5
        }

        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'please add valid card holder')

    def test_with_empty_expiration_date(self):
        data = {
            'CreditCardNumber': '1234567891234567',
            'CardHolder': 'TEST TEST',
            'ExpirationDate': '',
            'Amount': 19.5
        }

        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'please add valid expiration date')

    def test_with_empty_amount(self):
        data = {
            'CreditCardNumber': '1234567891234567',
            'CardHolder': 'TEST TEST',
            'ExpirationDate': '10-2022',
            'Amount': 0.0
        }

        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'please add valid amount')

    #### End Test With Empty Data #####



    ### Start Test With Invalid Data ###

    def test_with_invalid_credit_card_number(self):

        data = {
            'CreditCardNumber': '123456789',
            'CardHolder': 'TEST TEST',
            'ExpirationDate': '10-2022',
            'Amount': 19.5
        }

        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'please add valid credit card number')
    
    def test_with_invalid_expiration_date(self):
        data = {
            'CreditCardNumber': '1234567891234567',
            'CardHolder': 'TEST TEST',
            'ExpirationDate': '10-2019',
            'Amount': 19.5
        }

        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json['message'], 'please add valid expiration date')

    ### End Test With Invalid Data ###

    ### Start Test With Valid Data ###
    def test_cheap_payment_gateway_with_valid_data(self):
        data = {
            'CreditCardNumber': '1234567891234567',
            'CardHolder': 'TEST TEST',
            'ExpirationDate': '10-2022',
            'Amount': 19.5
        }

        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['payment_gateway'], 'CheapPaymentGateway')


    def test_expensive_payment_gatewat_with_valid_data(self):
        data = {
            'CreditCardNumber': '1234567891234567',
            'CardHolder': 'TEST TEST',
            'ExpirationDate': '10-2022',
            'Amount': 120.0
        }

        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['payment_gateway'], 'ExpensivePaymentGateway')

    def test_premium_payment_gatewat_with_valid_data(self):
        data = {
            'CreditCardNumber': '1234567891234567',
            'CardHolder': 'TEST TEST',
            'ExpirationDate': '10-2022',
            'Amount': 1000.0
        }

        response = self.app.post('/', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['payment_gateway'], 'PremiumPaymentGateway')

    ### End Test With Valid Data ###

if __name__ == "__main__":
    unittest.main()