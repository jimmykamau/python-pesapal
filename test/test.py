#!/usr/bin/env python3
import unittest
import requests

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import lib as pesapal

pesapal.consumer_key = 'SSr2MkbtF+/4wQIDESbP9muXMOfQ4Vof'
pesapal.consumer_secret = 'Lk/zjnsyjoM283g5+Tr0K5e8Jgo='
#pesapal.consumer_key = os.environ.get('PESAPAL_KEY', None)
#pesapal.consumer_secret = os.environ.get('PESAPAL_SECRET', None)
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
          'PhoneNumber': '254700111000',
          'LineItems': [
            {
              'uniqueid': '1',
              'particulars': 'PS4',
              'quantity': '1',
              'unitcost': '50000',
              'subTotal': '50000',
            }, {
              'uniqueId': '2',
              'particulars': 'Driveclub',
              'quantity': '1',
              'unitcost': '3000',
              'subTotal': '3000',
            }
          ]
        }

        print (pesapal.postDirectOrder(post_params, request_data))

    def test_query_payment_status(self):

        params = {
          'pesapal_merchant_reference': '000',
          'pesapal_transaction_tracking_id': '000'
        }

        print (pesapal.queryPaymentStatus(params))

    def test_query_payment_status_by_merchant_ref(self):

        params = {
          'pesapal_merchant_reference': '000'
        }

        print (pesapal.queryPaymentStatusByMerchantRef(params))

    def test_query_payment_details(self):

        params = {
          'pesapal_merchant_reference': '000',
          'pesapal_transaction_tracking_id': '000'
        }

        print (pesapal.queryPaymentDetails(params))


if __name__ == '__main__':
    unittest.main()