
## Install


```
pip install pesapal
```

## Example


```
import pesapal, urllib2

consumer_key ='consumer_key'
consumer_secret = 'consumer_secret'
testing = False

### make client
client = pesapal.PesaPal(consumer_key, consumer_secret, testing)

### post a direct order

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
request = client.postDirectOrder(post_params, request_data)
# get url to display as an iframe
print request.to_url()

### get order status

params = {
  'pesapal_merchant_reference': '000',
  'pesapal_transaction_tracking_id': '000'
}
request = client.queryPaymentStatus(params)
url = request.to_url()
print url
response = urllib2.urlopen(url)
print response.read()

### get order status by ref

params = {
  'pesapal_merchant_reference': '000'
}
request = client.queryPaymentStatusByMerchantRef(params)
print request.to_url()

### get detailed order status

params = {
  'pesapal_merchant_reference': '000',
  'pesapal_transaction_tracking_id': '000'
}
request = client.queryPaymentDetails(params)
print request.to_url()

```

## Api

### PesaPal(consumer_key, consumer_secret, testing)
  
  pass testing as true to use http://demo2.pesapal.com/api/ instead of https://www.pesapal.com/api/

### PesaPal#postDirectOrder(options)
  
  returns an oauth object

  options is a dictionary containing:

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

### PesaPal#queryPaymentStatus(options)

  returns an oauth object

  options is a dictionary containing:

  - pesapal_merchant_reference
  - pesapal_transaction_tracking_id

### PesaPal#queryPaymentStatusByMerchantRef(options)

  returns an oauth object

  options is a dictionary containing:
  
  - pesapal_merchant_reference

### PesaPal#queryPaymentDetails(options)

  returns an oauth object

  options is a dictionary containing:

  - pesapal_merchant_reference
  - pesapal_transaction_tracking_id

## Test

```
make
```

## License

MIT
