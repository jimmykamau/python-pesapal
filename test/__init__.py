#!/usr/bin/env python
import unittest
from urllib2 import urlopen

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import pesapal

KEY = os.environ.get('PESAPAL_KEY', '')
SECRET = os.environ.get('PESAPAL_SECRET', '')

class TestURLS(unittest.TestCase):

    def setUp(self):
        self.client = pesapal.PesaPal(KEY, SECRET)

    def test_post_direct_order(self):

        client = self.client

        request_data = {
          'Amount': '1',
          'Description': '1',
          #'Type': '',
          'Reference': '1',
          'PhoneNumber': '254700111000'
        }

        post_params = {
          'oauth_callback': 'www.myorder.co.ke/oauth_callback'
        }

        request = client.postDirectOrder(post_params, request_data)
        print request.to_url()

    def test_query_payment_status(self):

        client = self.client

        params = {
          'pesapal_merchant_reference': '000',
          'pesapal_transaction_tracking_id': '000'
        }

        request = client.queryPaymentStatus(params)
        print request.to_url()

    def test_query_payment_status_by_merchant_ref(self):

        client = self.client

        params = {
          'pesapal_merchant_reference': '000'
        }

        request = client.queryPaymentStatusByMerchantRef(params)
        print request.to_url()

    def test_query_payment_details(self):

        client = self.client

        params = {
          'pesapal_merchant_reference': '000',
          'pesapal_transaction_tracking_id': '000'
        }

        request = client.queryPaymentDetails(params)
        print request.to_url()



if __name__ == '__main__':
    unittest.main()