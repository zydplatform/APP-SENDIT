from uuid import uuid4
users = []

orders = []

status = {
    1:"make_order",
    2:"in_transit",
    3:"canceled",
    4:"delivered"
}


class User:
    def __init__(self, user_name, user_email, user_password,confirm_password):
        self.user_id = uuid4().hex
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
        self.confirm_password = confirm_password
    
    def create_user(self):
        user = {
                "user_id":self.user_id,
                "user_name":self.user_name,
                "user_email":self.user_email,
                "user_password":self.user_password,
                "confirm_password":self.confirm_password
               }
        users.append(user)
        return user
    def get_all_users(self):
        return users
    def get_single_user(self,user_id):
        for user in users:
            if user_id == user['user_id']:
                return user


class Order:
    def __init__(self, parcel_name, parcel_weight, parcel_description, parcel_price, pickup, destination, status):
        self.parcel_id = uuid4().hex
        self.user_id = uuid4().hex
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
            "status": self.status,
            "user_id":self.user_id
        }

        orders.append(order)

        return order

    def get_all_orders(self):
        return orders

    def get_single_order(self, parcel_id):
        for order in orders:
            if parcel_id == order['parcel_id']:
                return order
    

