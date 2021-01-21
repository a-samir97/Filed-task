from flask import abort
from datetime import date, datetime

from utils import split_date

def validate_credit_card_number(credit_card_number):
    if len(credit_card_number) != 16:
        abort(400, 'please add valid credit card number')

def validate_expiration_date(expiration_date):
    if len(expiration_date) <= 1:
        abort(400, 'please add valid expiration date')

    month, year = split_date(expiration_date)
    input_date = date(year, month, 1)
    current_date = datetime.now().date()

    if current_date > input_date:
        abort(400, 'please add valid expiration date')

def validate_card_holder(card_holder):

    if len(card_holder) < 1:
        abort(400, 'please add valid card holder')

def validate_amount(amount):
    if amount <= 0:
        abort(400, 'please add valid amount')