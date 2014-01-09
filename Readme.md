
## Install

    $ pip install pesapal


## Example

```python

import urllib2
import pesapal


pesapal.consumer_key = 'consumer_key'
pesapal.consumer_secret = 'consumer_secret'
pesapal.testing = False


### post a direct order

post_params = {
  'oauth_callback': 'https://www.example.com/post_payment_page/'
}
request_data = {
  'Amount': '100',
  'Description': 'E-book purchase',
  'Type': 'MERCHANT',
  'Reference': '12erwe',
  'PhoneNumber': '0700111000'
}
# build url to redirect user to confirm payment
url = pesapal.postDirectOrder(post_params, request_data)


### get order status

post_params = {
  'pesapal_merchant_reference': '000',
  'pesapal_transaction_tracking_id': '000'
}
url = pesapal.queryPaymentStatus(post_params)
response = urllib2.urlopen(url)
print response.read()


### get order status by ref

post_params = {
  'pesapal_merchant_reference': '000'
}
url = pesapal.queryPaymentStatusByMerchantRef(post_params)
response = urllib2.urlopen(url)
print response.read()


### get detailed order status

post_params = {
  'pesapal_merchant_reference': '000',
  'pesapal_transaction_tracking_id': '000'
}
url = pesapal.queryPaymentDetails(post_params)
response = urllib2.urlopen(url)
print response.read()

```

## Api

### consumer_key

  configurable consumer key

### consumer_secret

  configurable consumer secret

### testing
  
  variable that sets the base api url as http://demo.pesapal.com/api/ or https://www.pesapal.com/api/

### postDirectOrder(post_params, request_data)
  
  returns url

  post_params is a dictionary containing:

  - Amount
  - Description
  - Type
  - Reference
  - Email or/and PhoneNumber
  - Currency ( optional )
  - FirstName ( optional )
  - LastName ( optional )
  - LineItems ( optional )

  request_data is a dictionary containing:
  
  - oauth_callback


### queryPaymentStatus(options)

  returns url

  options is a dictionary containing:

  - pesapal_merchant_reference
  - pesapal_transaction_tracking_id

### queryPaymentStatusByMerchantRef(options)

  returns url

  options is a dictionary containing:
  
  - pesapal_merchant_reference

### queryPaymentDetails(options)

  returns url

  options is a dictionary containing:

  - pesapal_merchant_reference
  - pesapal_transaction_tracking_id

## Test

    $ make deps test

## License

MIT
