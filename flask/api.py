from flask import Flask, jsonify, request 

app = Flask(__name__)

items = [
    {'id': 1, 'name': 'Item 1', 'price': 10.99},
    {'id': 2, 'name': 'Item 2', 'price': 12.99},
    {'id': 3, 'name': 'Item 3', 'price': 15.99}
]

@app.route('/')
def home():
    return "Welcome to the Item API!"

@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    else:
        return jsonify({'error': 'Item not found'}), 404
    
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json or 'price' not in request.json:
        return jsonify({'error': 'Bad Request'}), 400
    new_item = {
        'id': len(items) + 1,
        'name': request.json.get('name'),
        'price': request.json.get('price')
    }
    items.append(new_item)
    return jsonify(new_item), 201

@app.route('/items', methods=['PUT'])
def update_item():
    if not request.json or 'id' not in request.json:
        return jsonify({'error': 'Bad Request'}), 400
    item_id = request.json['id']
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({'error': 'Item not found'}), 404
    item['name'] = request.json.get('name', item['name'])
    item['price'] = request.json.get('price', item['price'])
    return jsonify(item)

@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({'result': True})

if __name__ == '__main__':
    app.run(debug=True)