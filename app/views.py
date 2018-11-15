from flask import jsonify, request
from app import app
from app.models import Order,orders

@app.errorhandler(404)
def error404(error):
    return jsonify({"error":" Page not found !"}),404

@app.errorhandler(500)
def error500(error):
    return jsonify({"error":"Invalid request"}),500

@app.errorhandler(405)
def error405(error):
    return jsonify({"error":"Method not allowed"}),405

@app.route('/', methods=['POST', 'GET'])
@app.route('/api/v1', methods=['POST', 'GET'])
def index():
    
    return jsonify({"message": "Welcome To Send It API."}), 200

@app.route('/api/v1/parcels', methods=['POST', 'GET'])
def create_and_get_orders():
    if request.method == 'POST':

        data = request.json

        parcel_name = data['parcel_name']
        parcel_weight = data['parcel_weight']
        parcel_description = data['parcel_description']
        parcel_price = data['parcel_price']
        pickup = data['pickup']
        destination = data['destination']
        status = data['status']
        order_class = Order(parcel_name, parcel_weight, parcel_description, parcel_price, pickup, destination, status)
        order = order_class.create_order()
        return jsonify({"message": "Order created", "order": order}), 201

    if request.method == 'GET':
        if not orders:
            return jsonify({"message": "Sorry orders not availble."}), 400
        return jsonify({"message": "All created orders", "Orders": orders}), 200


@app.route('/api/v1/parcels/<string:parcel_id>', methods=['GET'])
def get_single_order(parcel_id):
    order_class = Order(
        parcel_name='',
        parcel_weight='',
        parcel_description='',
        parcel_price='',
        pickup='',
        destination='',
        status=''
    )
    order = order_class.get_single_orders(parcel_id)
    return jsonify({"Order": order}), 200


@app.route('/api/v1/users/<int:user_id>/parcels', methods=['GET'])
def get_orders_by_user(user_id):
    
    return jsonify({"message": "get all orders of a specific user"}), 200


@app.route('/api/v1/parcels/<int:parcel_id>/cancel', methods=['PUT'])
def cancel_order(parcel_id):
    return jsonify({"message": "cancel order."}), 200
