import os
import unittest
import json
 
from restful_api import app, db
 
basedir = os.path.abspath(os.path.dirname(__file__))
TEST_DB = 'testdb.sqlite'

# Request data
headers = {"content-type": "application/json"}          
data_json = json.dumps({
    "name":"Camera",
    "description":"This is a camera",
    "price":500.00,
    "qty":100
})
 
class BasicTests(unittest.TestCase):
 
############################
#### setup and teardown ####
############################
 
    # Executed prior to each test to setup DB
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
         
        self.assertEqual(app.debug, False)
 
    # Executed after each test
    def tearDown(self):
        pass 
 
###############
#### tests ####
###############


    ### Test POST
    # Test creating product
    def test_create_product(self):
        print("----".join((" ","Test creating a product"," ")))
        resp = self.app.post('/product', data=data_json, headers=headers)
        self.assertEqual(resp.status_code,200)

    # Test exception when a param is missing
    def test_create_product_exception(self):
        print("----".join((" ","Test exception when param is missing"," ")))
        data_json = json.dumps({}) 
        resp = self.app.post('/product', data=data_json, headers=headers)
        self.assertEqual(resp.status_code,400)   

    ### Test GET
    # Test getting all products
    def test_get_all(self):
        print("----".join((" ","Test getting all products"," ")))  
        # Get data into cache first
        resp = self.app.get('/product')
        self.assertEqual(resp.status_code,200)

    # Test getting specific products
    def test_get_specific(self):
        print("----".join((" ","Test getting specific products"," ")))  
        # Create product to get
        resp = self.app.post('/product', data=data_json, headers=headers)
        self.assertEqual(resp.status_code,200)
        # Now try get it
        resp = self.app.get('/product/1')
        self.assertEqual(resp.status_code,200)

    # Test exception getting specific products
    def test_get_specific_exception(self):
        print("----".join((" ","Test exception getting specific products"," ")))          
        # Now try get it
        resp = self.app.get('/product/1')
        self.assertEqual(resp.status_code,200)

    ### Test PUT
    # Test updating products
    def test_update(self):
        print("----".join((" ","Test updating products"," ")))  
        # Create product to update
        resp = self.app.post('/product', data=data_json, headers=headers)
        self.assertEqual(resp.status_code,200)
        # Now try get it
        data_json_update = json.dumps({
            "name":"Camera",
            "description":"This is a camera",
            "price":500.00,
            "qty":99
        })
        resp = self.app.put('/product/1', data=data_json_update, headers=headers)
        self.assertEqual(resp.status_code,200)

    # Test updating products exception
    def test_update_exception(self):
        print("----".join((" ","Test updating products exception"," ")))  
        # Create product to update
        resp = self.app.post('/product', data=data_json, headers=headers)
        self.assertEqual(resp.status_code,200)
        # Now try get it
        data_json_update = json.dumps({
            "name":"Camera",
            "description":"This is a camera",
            "price":500.00,
            "qty":99
        })
        resp = self.app.put('/product/2', data=data_json_update, headers=headers)
        self.assertEqual(resp.status_code,200)

    ### Test DELETE
    # Test deleting specific
    def test_delete_specific(self):
        print("----".join((" ","Test deleting products"," "))) 
        # Create product to update
        resp = self.app.post('/product', data=data_json, headers=headers)
        self.assertEqual(resp.status_code,200)        
        # Then delete 1
        resp = self.app.delete('/product/1')
        self.assertEqual(resp.status_code, 200)

    # Test deleting specific exception
    def test_delete_specific_exception(self):
        print("----".join((" ","Test deleting products exception"," "))) 
        # Create product to update
        resp = self.app.post('/product', data=data_json, headers=headers)
        self.assertEqual(resp.status_code,200)        
        # Then delete 1
        resp = self.app.delete('/product/a')
        self.assertEqual(resp.status_code, 200)

    # Test deleting all
    def test_delete_all(self):
        print("----".join((" ","Test deleting products"," "))) 
        # Create product to update
        resp = self.app.post('/product', data=data_json, headers=headers)
        self.assertEqual(resp.status_code,200)        
        # Then delete all
        resp = self.app.delete('/product')
        self.assertEqual(resp.status_code, 200)
 
if __name__ == "__main__":
    unittest.main()
