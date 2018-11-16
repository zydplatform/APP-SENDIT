

from unittest import TestCase
import json
from app import app, views


class AppTest(TestCase):
    """Testing all AppTest endpoints"""

    def setUp(self):
        self.client = app.test_client()
        self.order = {
            "parcel_name": "Bag",
            "parcel_weight": 33,
            "parcel_description": "big",
            "parcel_price": 3000,
            "pickup": "mengo",
            "destination": "mukono",
            "status": 1
        }
        self.user = {
            "user_name":"ivan",
            "user_email":"kigs@gmail.com",
            "user_password":"ieatalot",
            "confirm_password":"ieatalot"
        }

    def test_home(self):
        res = self.client.get('/')
        res = self.client.get('/api/v1')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"Welcome To Send It API.", res.data)

    def test_create_order(self):
        res = self.client.post('/api/v1/parcels',
                               data=json.dumps(self.order),
                               content_type='application/json'
                               )
        self.assertEqual(res.status_code, 201)
        self.assertIn(b"Order created", res.data)

    def test_create_user(self):
        res = self.client.post('/api/v1/users',data=json.dumps(self.user),
        content_type='application/json')
        self.assertEqual(res.status_code,201)
        self.assertIn(b"User created",res.data)

    def test_get_all_orders(self):
        res = self.client.get('/api/v1/parcels')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"All created orders", res.data)

    def test_get_all_users(self):
        res = self.client.get('/api/v1/users')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"All created users", res.data)


    def test_get_single_order(self):
        res = self.client.get('/api/v1/parcels/1')
        self.assertEqual(res.status_code, 200)

    def test_get_single_user(self):
        res = self.client.get('/api/v1/users/1')
        self.assertEqual(res.status_code, 200)

    def test_get_orders_by_user(self):
        res = self.client.get('/api/v1/users/1/parcels')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"get all orders of a specific user", res.data)

    def test_cancel_order(self):
        res = self.client.put('/api/v1/parcels/1/cancel')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b"cancel order", res.data)
