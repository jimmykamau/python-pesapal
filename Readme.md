
## Install

    $ pip install python3_pesapal


## Example

```python

import requests
import python_pesapal as pesapal


pesapal.consumer_key = 'consumer-key'
pesapal.consumer_secret = 'consumer-secret'
### change to false in production environment
pesapal.testing = True


### post a direct order

post_params = {
  'oauth_callback': 'https://website.example.com/callback/'
}
request_data = {
  'Amount': '10',
  'Description': 'E-book purchase 2',
  'Type': 'MERCHANT',
  'Reference': '000',
  'Email': 'john@test.com',
  'Currency': 'USD',
}
# build url to redirect user to confirm payment
url = pesapal.postDirectOrder(post_params, request_data)
print(url)

### get order status

post_params = {
  'pesapal_merchant_reference': '000',
  'pesapal_transaction_tracking_id': 'f4a878c5-2cad-4dd8-8378-6c2e308db123'
}
url = pesapal.queryPaymentStatus(post_params)
response = requests.get(url)
print(response.text)


### get order status by ref

post_params = {
  'pesapal_merchant_reference': '000'
}
url = pesapal.queryPaymentStatusByMerchantRef(post_params)
response = requests.get(url)
print(response.text)


### get detailed order status

post_params = {
  'pesapal_merchant_reference': '000',
  'pesapal_transaction_tracking_id': 'f4a878c5-2cad-4dd8-8378-6c2e308db123'
}
url = pesapal.queryPaymentDetails(post_params)
response = requests.get(url)
print(response.text)

```

## Django, GAE

For a more opionated solution, checkout [gae-pesapal](https://github.com/kelonye/gae-pesapal) or [django-pesapal](https://github.com/kelonye/django-pesapal)(WIP).

## Api

### consumer_key

configurable consumer key

### consumer_secret

configurable consumer secret

### testing
  
variable that sets the base api url as http://demo.pesapal.com/api/ or https://www.pesapal.com/api/

### postDirectOrder(post_params, request_data)
  
returns order url

`post_params` is a dictionary containing:

  - Amount
  - Description
  - Type
  - Reference
  - Email or/and PhoneNumber
  - Currency ( optional )
  - FirstName ( optional )
  - LastName ( optional )
  - LineItems ( optional )

#### Line Items

This is an array of the products contained in the order:

```js

{
  LineItems: [
    {
      'uniqueid': '',
      'particulars': '',
      'quantity': '',
      'unitCost': '',
      'subTotal': ''
    }
  ]
}

`request_data` is a dictionary containing:
  
  - oauth_callback

### queryPaymentStatus(options)

returns url to retrive payment status

`options` is a dictionary containing:

  - pesapal_merchant_reference
  - pesapal_transaction_tracking_id

### queryPaymentStatusByMerchantRef(options)

returns url to retrive payment status

`options` is a dictionary containing:
  
  - pesapal_merchant_reference

### queryPaymentDetails(options)

returns url to retrive a detailed status of a payment

`options` is a dictionary containing:

  - pesapal_merchant_reference
  - pesapal_transaction_tracking_id

## Test

    $ python3 test/test.py

## License

MIT
