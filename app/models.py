from app import validate_apis
from app.validate_apis import invalid_inputs,empty_field

users = []

orders = []

status = {
    "init": 0,
    "make_order": 1,
    "in_transit": 2,
    "canceled": 3,
    "delivered": 4
}


class User:
    def __init__(self, user_name, user_email, user_password, user_address, confirm_password):
        self.user_id = len(users) + 1
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.user_address = user_address
        self.confirm_password = confirm_password


class Order:
    def __init__(self, parcel_name, parcel_weight, parcel_description, parcel_price, pickup, destination, status):
        self.parcel_id = len(orders) + 1
        self.parcel_name = parcel_name
        self.parcel_weight = parcel_weight
        self.parcel_description = parcel_description
        self.parcel_price = parcel_price
        self.pickup = pickup
        self.destination = destination
        self.status = status

    def create_order(self):
        order = {
            "parcel_id": self.parcel_id,
            "parcel_name": self.parcel_name,
            "parcel_weight": self.parcel_weight,
            "parcel_description": self.parcel_description,
            "parcel_price": self.parcel_price,
            "pickup": self.pickup,
            "destination": self.destination,
            "status": self.status
        }

        orders.append(order)

        return order

    def get_all_orders(self):
        return orders

    def get_single_orders(self, parcel_id):
        for order in orders:
            if parcel_id == order['parcel_id']:
                return order
    