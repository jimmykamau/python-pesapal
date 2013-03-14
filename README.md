
Install
---

```
pip install git+https://github.com/kelonye/python_pesapal.git
```

Example
---

```

consumer_key ='consumer_key'
consumer_secret = 'consumer_secret'

import pesapal, urllib2

# make client
client = pesapal.PesaPal(consumer_key, consumer_secret)

request_data = {
  'Amount': '',
  'Description': '',
  'Type': '',
  'Reference': '',
  'PhoneNumber': ''
}

post_params = {
  'oauth_callback': 'www.example.com/post_payment_page'
}

# post a direct order
request = client.postDirectOrder(post_params, request_data)
print request.to_url()

params = {
  'pesapal_merchant_reference': '000',
  'pesapal_transaction_tracking_id': '000'
}

# get order status
request = client.queryPaymentStatus(params)
url = request.to_url()
print url
response = urllib2.urlopen(url)
print response.read()

params = {
  'pesapal_merchant_reference': '000'
}

# get order status by ref
request = client.queryPaymentStatusByMerchantRef(params)
print request.to_url()

params = {
  'pesapal_merchant_reference': '000',
  'pesapal_transaction_tracking_id': '000'
}

# get detailed order status
request = client.queryPaymentDetails(params)
print request.to_url()

```

Api
---

- PesaPal
    - options
        - consumer_key
        - consumer_secret

  - methods: return oauth.OAuthRequest objects
      - postDirectOrder
          - options: hash containing:
              - Amount
              - Description
              - Type
              - Reference
              - Email
              - PhoneNumber
              ( optional )
              - Currency
              - FirstName
              - LastName
              - LineItems

      - queryPaymentStatus
          - options: hash containing:
              - pesapal_merchant_reference
              - pesapal_transaction_tracking_id

      - queryPaymentStatusByMerchantRef
          - options: hash containing:
              - pesapal_merchant_reference

      - queryPaymentDetails
          - options: hash containing:
              - pesapal_merchant_reference
              - pesapal_transaction_tracking_id

Testing
---

```
make
```

License
---

MIT