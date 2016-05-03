#!/usr/bin/env python3
import unittest
import requests

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import python3_pesapal

python3_pesapal.consumer_key = os.environ.get('PESAPAL_KEY', None)
python3_pesapal.consumer_secret = os.environ.get('PESAPAL_SECRET', None)
python3_pesapal.testing = True

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

        print (python3_pesapal.postDirectOrder(post_params, request_data))

    def test_query_payment_status(self):

        params = {
          'pesapal_merchant_reference': '000',
          'pesapal_transaction_tracking_id': '000'
        }

        print (python3_pesapal.queryPaymentStatus(params))

    def test_query_payment_status_by_merchant_ref(self):

        params = {
          'pesapal_merchant_reference': '000'
        }

        print (python3_pesapal.queryPaymentStatusByMerchantRef(params))

    def test_query_payment_details(self):

        params = {
          'pesapal_merchant_reference': '000',
          'pesapal_transaction_tracking_id': '000'
        }

        print (python3_pesapal.queryPaymentDetails(params))


if __name__ == '__main__':
    unittest.main()