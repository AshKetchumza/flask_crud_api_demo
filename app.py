from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

basedir = os.path.abspath(os.path.dirname(__file__))

# Init app
app = Flask(__name__)

# Database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init DB
db = SQLAlchemy(app)

# Init Marshmallow
ma = Marshmallow(app)

# Product Class/Model
class Product(db.Model):
    # Define parameters
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    # Init
    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# Product Schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

# Init Schemas
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create a product
@app.route('/product', methods=['POST'])
def add_product():
    try:
        # Create vars from request data
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        qty = request.json['qty']

        # Create object with vars
        new_product = Product(name, description, price, qty)

        # Add to DB and commit
        db.session.add(new_product)
        db.session.commit()

        # API response
        return product_schema.jsonify(new_product)
    except Exception as err:
        # Handle exception
        return jsonify({'msg': err.args, 'error': 'Exception'})

# Get all products
@app.route('/product', methods=['GET'])
def get_products():
    try:
        # Query DB for all objects
        all_products = Product.query.all()
        # Create object from data
        result = products_schema.dump(all_products)
        
        # API response
        return jsonify(result)
    except Exception as err:
        # Handle exception
        return jsonify({'msg': err.args, 'error': 'Exception'})

# Get single products
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
    try:
        # Create object equal to DB query for specific object
        product = Product.query.get(id)

        # API response
        return product_schema.jsonify(product)
    except Exception as err:
        # Handle exception
        return jsonify({'msg': err.args, 'error': 'Exception'})

# Update a product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
    try:
        # Create object equal to DB query for specific object
        product = Product.query.get(id)

        # Create vars from request data
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        qty = request.json['qty']

        # Update new object with vars
        product.name = name
        product.description = description
        product.price = price
        product.qty = qty

        # Commit to DB
        db.session.commit()

        # API response
        return product_schema.jsonify(product)
    except Exception as err:
        # Handle exception
        return jsonify({'msg': err.args, 'error': 'Exception'})

# Delete a product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
    try:
        # Create object equal to DB query for specific object
        product = Product.query.get(id)

        # Delete from DB and commit
        db.session.delete(product)
        db.session.commit()

        # API response
        return product_schema.jsonify(product)
    except Exception as err:
        # Handle exception
        return jsonify({'msg': err.args, 'error': 'Exception'})

# Delete all products
@app.route('/product', methods=['DELETE'])
def delete_all_products():
    try:
        # Delete all objects of class
        Product.query.delete()

        # Commit to DB
        db.session.commit()

        # API response
        return jsonify({ 'msg': 'All Products deleted'})
    except Exception as err:
         # Handle exception
        return jsonify({'msg': err.args, 'error': 'Exception'})

# Run server
if __name__ == '__main__':
    app.run()