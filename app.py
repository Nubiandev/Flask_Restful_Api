#Importing Flask libraries flask, jsonify for json, and request 

from flask import Flask, jsonify, request
app = Flask(__name__)

#in-memory storage for items 
items = []

#Home route 
@app.route('/')
def home(): 
    return "Welcome to the Simple Item API!"

#GET all items
@app.route('/items', methods=['GET'])
def get_items(): 
    return jsonify(items)

#POST new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()
    print(new_item) #added to debug
    items.append(new_item)
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True)
        

