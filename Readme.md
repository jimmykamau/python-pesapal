
## Install


    $ pip install pesapal


## Example

```python
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

### Using requests

Install requests with pip

    $ pip install requests

```python

client = pesapal.PesaPal(consumer_key, consumer_secret)
request = client.queryPaymentStatus(params)
url = request.to_url()
response = requests.get(url)
if response.status_code == 200:
  print response.text

```

### Using urllib3

    $ pip install urllib3

```python
client = pesapal.PesaPal(consumer_key, consumer_secret)
request = client.queryPaymentStatus(params)
url = request.to_url()

import urllib3
http = urllib3.PoolManager()

response = http.request('GET', url)
if response.status == 200:
  print response.data

```

### Using Google App Engine's urlfetch

```python
from google.appengine.api import urlfetch

client = pesapal.PesaPal(consumer_key, consumer_secret)
request = client.queryPaymentStatus(params)
url = request.to_url()
response = urlfetch.fetch(url)
if response.status_code == 200:
    print response.content

```


## Api

### PesaPal(consumer_key, consumer_secret, testing)
  
  pass testing as true to use http://demo2.pesapal.com/api/ instead of https://www.pesapal.com/api/

### PesaPal#postDirectOrder(options)
  
  returns an oauth object ( get url with `.to_url()` method )

  options is a dictionary containing:

  - Amount
  - Description
  - Type
  - Reference
  - Email or/and PhoneNumber
  - Currency ( optional )
  - FirstName ( optional )
  - LastName ( optional )
  - LineItems ( optional )

### PesaPal#queryPaymentStatus(options)

  returns an oauth object ( get url with `.to_url()` method )

  options is a dictionary containing:

  - pesapal_merchant_reference
  - pesapal_transaction_tracking_id

### PesaPal#queryPaymentStatusByMerchantRef(options)

  returns an oauth object ( get url with `.to_url()` method )

  options is a dictionary containing:
  
  - pesapal_merchant_reference

### PesaPal#queryPaymentDetails(options)

  returns an oauth object ( get url with `.to_url()` method )

  options is a dictionary containing:

  - pesapal_merchant_reference
  - pesapal_transaction_tracking_id

## Test

    $ make deps test

## License

MIT
