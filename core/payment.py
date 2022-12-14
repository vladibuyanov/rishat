import os
import stripe

""" Связь с сервисом оплаты """

stripe.api_key = os.environ.get('stripe')


def create_checkout_session(name, price, pk):
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                'currency': 'usd',
                'product_data': {
                    'name': name,
                },
                'unit_amount': price,
            },
            'quantity': 1,
        }],
        mode='payment',
        success_url=f'https://rishatvb.herokuapp.com/api/item/{pk}',
        cancel_url=f'https://rishatvb.herokuapp.com/api/item/{pk}',
    )
    return session
