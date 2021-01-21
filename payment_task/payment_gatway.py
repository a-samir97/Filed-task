PremiumPaymentGateway = {
    'id': 1,
    'status_code': 200,
    'payment_gateway': 'PremiumPaymentGateway'
}

ExpensivePaymentGateway = {
    'id': 2,
    'status_code': 200,
    'payment_gateway': 'ExpensivePaymentGateway'
}

CheapPaymentGateway = {
    'id': 3,
    'status_code': 200,
    'payment_gateway': 'CheapPaymentGateway'
}

def process_by_cheap_payment_gatway(amount):
    '''
        assume it will return message, status code
        If the amount to be paid is less than £20, use CheapPaymentGateway.
    '''
    if CheapPaymentGateway['status_code'] == 200:
        return {
            'status_code': CheapPaymentGateway['status_code'],
            'payment_gateway':CheapPaymentGateway['payment_gateway']
        }

    return {
        'status_code': 400
    }

def process_by_expensive_gateway(amount):
    '''
        assume it will return message, status code
        
        If the amount to be paid is £21-500, use ExpensivePaymentGateway if available.
        Otherwise, retry only once with CheapPaymentGateway.
    '''
    if ExpensivePaymentGateway['status_code'] == 200:
        return {
            'status_code': ExpensivePaymentGateway['status_code'],
            'payment_gateway':ExpensivePaymentGateway['payment_gateway']
        }
    else:
        if CheapPaymentGateway['status_code'] == 200:
            return {
                'status_code': CheapPaymentGateway['status_code'],
                'payment_gateway':CheapPaymentGateway['payment_gateway']
            }

        return {
            'status_code': 400
        }

def process_by_premium_gateway(amount):
    '''
        assume it will return message, status code
        If the amount is > £500, try only PremiumPaymentGateway and retry up to 3 times
        in case payment does not get processed.
    '''
    if PremiumPaymentGateway['status_code'] == 200:
         return {
            'status_code': PremiumPaymentGateway['status_code'],
            'payment_gateway':PremiumPaymentGateway['payment_gateway']
        }   
    else:
        for i in range(0,3):
            if PremiumPaymentGateway['status_code'] == 200:
                return {
            'status_code': PremiumPaymentGateway['status_code'],
            'payment_gateway':PremiumPaymentGateway['payment_gateway']
        }
    
    return {
        'status_code': 400
    }

def process_payment(amount):
    if amount <= 20:
        response = process_by_cheap_payment_gatway(amount)

    elif amount > 20 and amount <= 500:
        response = process_by_expensive_gateway(amount)
    
    else:
        response = process_by_premium_gateway(amount)

    return response