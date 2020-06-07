from flask import Flask, jsonify, request, render_template
# packages -> lowercase, #classes -> uppercase

app = Flask(__name__)

stores = [
    {
        'name': 'My Wonderful Store',
        'items': [
            {
            'name': 'My Item',
            'price': 15.99
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html')

# @app.route('/') # 'http://www.google.com/', just forward slash for home
# def home():
#     return "Hello, world!"

# from server perspective:
# POST - used to receive data
# GET - used to send data back only, however from browser perspective this is opposite.


# POST /store data: {name:}, will create a new store with a given name.
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
    'name': request_data['name'],
    'item': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# GET /store/<string:name>, this one is going to get a store for a given name and it's gonna return some data about it.
@app.route('/store/<string:name>')   # 'http://127.0.0.1:5000/store/some name'
def get_store(name):
    # Iterate over stores
    for store in stores:
        # if the store name matches, return it
        if store['name'] == name:
            return jsonify(store)
    # if none match, return an error message
    return jsonify({'message': 'store not found!'})


# GET /store, this one is going to return list of all stores.
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})   # this is going to convert the 'stores' variable to JSON


# POST /store/<string:name>/item, this one is going to create an item inside a specific store with a given name.
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})


# GET /store/<string:name>/item, this one is gonna get all the items in a specific store.
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
        return jsonify({'message': 'store not found'})



app.run(port=5000)
