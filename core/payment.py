import stripe

stripe.api_key = 'sk_test_51LhXWLAH1MlYWwwsLCU5zqtPe5jjGlXcS65BccGaxRP' \
                 'v0xPoF22QHYbqVRddBVBF9YAbk4JzAuDECIVY8KdlmjQk00DQIU90nN'


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
        success_url=f'http://127.0.0.1:8000/api/item/{pk}',
        cancel_url=f'http://127.0.0.1:8000/api/item/{pk}',
    )
    return session