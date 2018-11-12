from flask import Flask,request,jsonify

app = Flask(__name__)


from app.models import Order,User,orders,users

@app.route('/api/v1/order',methods=['POST'])
def create_orders():
    data = request.get_json()
    parcel_name = data.get('parcel_name')
    parcel_weight = data.get('parcel_weight')
    parcel_description =  data.get('parcel_description')
    parcel_price = data.get('parcel_price')
    pickup = data.get('pickup')
    destination = data.get('destination')
    status = data.get('status')

    order = Order(parcel_name,parcel_weight,parcel_description,parcel_price,pickup,destination,status)
    orders.append(order.put_dict)
    return jsonify({"message":"order created successfully"}),201
@app.route('/api/v1/order',methods=['GET'])    
def get_all_orders():
    if not orders:
        return jsonify({"message":"Sorry orders not availble."}),400
    return jsonify({"Orders":orders})
@app.route('/api/v1/order',methods=['GET'])
def get_single_order(order_id):
    if order_id == "":
        return jsonify({"message":"Invalid request !"}),400
    elif type(order_id) != int:
        return jsonify({"message":"order id should be a number"})
    else:
        return jsonify({"Orders":orders[order_id]})

@app.route('/api/v1/order')
def cancel_order(order_id):
    if order_id == orders[order_id]:
        if user_id == users[user_id]:

            return jsonify({"message":"order canceled"})







