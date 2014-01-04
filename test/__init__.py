#!/usr/bin/env python
import unittest
from urllib2 import urlopen

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import lib as pesapal

pesapal.consumer_key = os.environ.get('PESAPAL_KEY', 'H7jjIYLsuYGWZEJnuO8mIEMMPa4K15O6')
pesapal.consumer_secret = os.environ.get('PESAPAL_SECRET', 'C0hFRtwKY+rKfol3usK8ejhgL+s=')
pesapal.testing = True

class TestURLS(unittest.TestCase):

    def test_post_direct_order(self):

        post_params = {
          'oauth_callback': 'www.myorder.co.ke/oauth_callback'
        }
        request_data = {
          'Amount': '1',
          'Description': '1',
          #'Type': '',
          'Reference': '1',
          'PhoneNumber': '254700111000'
        }

        print pesapal.postDirectOrder(post_params, request_data)

    def test_query_payment_status(self):

        params = {
          'pesapal_merchant_reference': '000',
          'pesapal_transaction_tracking_id': '000'
        }

        print pesapal.queryPaymentStatus(params)

    def test_query_payment_status_by_merchant_ref(self):

        params = {
          'pesapal_merchant_reference': '000'
        }

        print pesapal.queryPaymentStatusByMerchantRef(params)

    def test_query_payment_details(self):

        params = {
          'pesapal_merchant_reference': '000',
          'pesapal_transaction_tracking_id': '000'
        }

        print pesapal.queryPaymentDetails(params)


if __name__ == '__main__':
    unittest.main()