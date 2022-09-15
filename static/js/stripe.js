let stripe = Stripe("pk_test_51LhXWLAH1MlYWwwsWkbOqbxDWLfd6NtVBp3mljg7IiRdEnfvG6raujB927oQO18XbIvlJ6Ibf1xvCsWhZLTNhwvy00FgimE1T2");
let buyButton = document.getElementById('buy-button');

buyButton.addEventListener('click', function() {
    fetch('https://rishatvb.herokuapp.com/api/buy/1')
    .then(response => response.json())
    .then(session => stripe.redirectToCheckout({ sessionId: session }))
});
