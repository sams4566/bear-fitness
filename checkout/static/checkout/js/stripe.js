// Create payment input
var stripePublicKey = $('#var_stripe_public_key').text().slice(1, -1)
var stripe = Stripe(stripePublicKey);
var elements = stripe.elements();
var card = elements.create('card', {
    style: {
        base: {
            iconColor: '#000000',
            color: '#000000',
            fontWeight: '500',
            fontFamily: 'Roboto, Open Sans, Segoe UI, sans-serif',
            fontSize: '16px',
            fontSmoothing: 'antialiased',
            ':-webkit-autofill': {
                color: '#000000',
            },
            '::placeholder': {
                color: '#000000'
            }
        },
        invalid: {
            iconColor: '#000000',
            color: '#000000',
        }
    },
});
card.mount('#card-element')

// Create payment submission
var form = document.getElementById('payment-form');

form.addEventListener('submit', function(event) {
    event.preventDefault();
    $('#payment-form').fadeToggle(110);
    $('#loading-background').fadeToggle(110);

    var clientSecret = $('#var_client_secret').text().slice(1, -1);

    var csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    var data = {
        'client_secret': clientSecret,
        'csrfmiddlewaretoken': csrfToken,
    }
    var data_view = '/checkout/save_checkout_info/';

    $.post(data_view, data).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.full_name.value),
                    phone: $.trim(form.telephone.value),
                    email: $.trim(form.email.value),
                    address:{
                        line1: $.trim(form.address_line1.value),
                        line2: $.trim(form.address_line2.value),
                        city: $.trim(form.city.value),
                        state: $.trim(form.county.value),
                        country: $.trim(form.country.value),
                        postal_code: $.trim(form.postcode.value),
                    }
                }
            }
        }).then(function(result) {
            if (result.error) {
                console.log(result.error.message);
                $('#payment-form').fadeToggle(110);
                $('#loading-background').fadeToggle(110);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        }).fail(function () {
            location.reload();
        })
    });
});