```python
import json
# some JSON:
bill_json =  """{ "BillNumber":1245
                 ,"BillTotal":3000
                 ,"StoreLocation":"New York"
                 ,"BillDetails":[ { "Product":"Soda"
                                   ,"Quantity":10
                                   ,"UnitPrice":2
                                   ,"LineItemPrice": 20}
                                 ,{ "Product":"Chips"
                                   ,"Quantity":5
                                   ,"UnitPrice":3
                                   ,"LineItemPrice":15 }
                                 ,{ "Product":"cookies"
                                   ,"Quantity":4
                                   ,"UnitPrice":5
                                   ,"LineItemPrice":20 } ]
                 }"""

# Parse JSON using "loads" Method
data = json.loads(bill_json)
print(data["BillDetails"])

# OUTPUT: [{'Product': 'Soda', 'Quantity': 10, 'UnitPrice': 2, 'LineItemPrice': 20}, {'Product': 'Chips', 'Quantity': 5, 'UnitPrice': 3, 'LineItemPrice': 15}, {'Product': 'cookies', 'Quantity': 4, 'UnitPrice': 5, 'LineItemPrice': 20}]
```

```python
# JSON Nested value, Get First Product
import json
# some JSON:
bill_json =  """{ "BillNumber":1245
                 ,"BillTotal":3000
                 ,"StoreLocation":"New York"
                 ,"BillDetails":[ { "Product":"Soda"
                                   ,"Quantity":10
                                   ,"UnitPrice":2
                                   ,"LineItemPrice": 20}
                                 ,{ "Product":"Chips"
                                   ,"Quantity":5
                                   ,"UnitPrice":3
                                   ,"LineItemPrice":15 }
                                 ,{ "Product":"cookies"
                                   ,"Quantity":4
                                   ,"UnitPrice":5
                                   ,"LineItemPrice":20 } ]
                 }"""

# Parse JSON using "loads" Method
data = json.loads(bill_json)
print(data["BillDetails"][0]["Product"])

# OUTPUT: Soda
```

```python
# JSON Get All Products
import json
# some JSON:
bill_json =  """{ "BillNumber":1245
                 ,"BillTotal":3000
                 ,"StoreLocation":"New York"
                 ,"BillDetails":[ { "Product":"Soda"
                                   ,"Quantity":10
                                   ,"UnitPrice":2
                                   ,"LineItemPrice": 20}
                                 ,{ "Product":"Chips"
                                   ,"Quantity":5
                                   ,"UnitPrice":3
                                   ,"LineItemPrice":15 }
                                 ,{ "Product":"cookies"
                                   ,"Quantity":4
                                   ,"UnitPrice":5
                                   ,"LineItemPrice":20 } ]
                 }"""

# Parse JSON using "loads" Method
data = json.loads(bill_json)
for restaurant in data["BillDetails"]:
    print(restaurant["Product"])

# OUTPUT: Soda
#Chips
#cookies
```

```python
import json
# some JSON:
bill_json =  """{ "BillNumber":1245
                 ,"BillTotal":3000
                 ,"StoreLocation":"New York"
                 ,"BillDetails":[ { "Product":"Soda"
                                   ,"Quantity":10
                                   ,"UnitPrice":2
                                   ,"LineItemPrice": 20}
                                 ,{ "Product":"Chips"
                                   ,"Quantity":5
                                   ,"UnitPrice":3
                                   ,"LineItemPrice":15 }
                                 ,{ "Product":"cookies"
                                   ,"Quantity":4
                                   ,"UnitPrice":5
                                   ,"LineItemPrice":20 } ]
                 }"""

# Parse JSON using "loads" Method
data = json.loads(bill_json)
# json object to json string
for restaurant in data["BillDetails"]:
    # print(data)
    del restaurant["Product"]
    data_new =json.dumps(data)
    print(data_new)

  # OUTPUT: {"BillNumber": 1245, "BillTotal": 3000, "StoreLocation": "New York", "BillDetails": [{"Quantity": 10, "UnitPrice": 2, "LineItemPrice": 20}, {"Product": "Chips", "Quantity": 5, "UnitPrice": 3, "LineItemPrice": 15}, {"Product": "cookies", "Quantity": 4, "UnitPrice": 5, "LineItemPrice": 20}]}
#{"BillNumber": 1245, "BillTotal": 3000, "StoreLocation": "New York", "BillDetails": [{"Quantity": 10, "UnitPrice": 2, "LineItemPrice": 20}, {"Quantity": 5, "UnitPrice": 3, "LineItemPrice": 15}, {"Product": "cookies", "Quantity": 4, "UnitPrice": 5, "LineItemPrice": 20}]}
#{"BillNumber": 1245, "BillTotal": 3000, "StoreLocation": "New York", "BillDetails": [{"Quantity": 10, "UnitPrice": 2, "LineItemPrice": 20}, {"Quantity": 5, "UnitPrice": 3, "LineItemPrice": 15}, {"Quantity": 4, "UnitPrice": 5, "LineItemPrice": 20}]}
```
```python
# writing json string to json file.


import json
# some JSON:
bill_json =  """{ "BillNumber":1245
                 ,"BillTotal":3000
                 ,"StoreLocation":"New York"
                 ,"BillDetails":[ { "Product":"Soda"
                                   ,"Quantity":10
                                   ,"UnitPrice":2
                                   ,"LineItemPrice": 20}
                                 ,{ "Product":"Chips"
                                   ,"Quantity":5
                                   ,"UnitPrice":3
                                   ,"LineItemPrice":15 }
                                 ,{ "Product":"cookies"
                                   ,"Quantity":4
                                   ,"UnitPrice":5
                                   ,"LineItemPrice":20 } ]
                 }"""
data = json.loads(bill_json)
data_new =json.dumps(data)
print(data_new)
data_new =json.dumps(data)
print(data_new)
with open('Bills_new.json', 'w') as f:
  json.dump(data_new, f, indent=2)

# OUTPUT: {"BillNumber": 1245, "BillTotal": 3000, "StoreLocation": "New York", "BillDetails": [{"Product": "Soda", "Quantity": 10, "UnitPrice": 2, "LineItemPrice": 20}, {"Product": "Chips", "Quantity": 5, "UnitPrice": 3, "LineItemPrice": 15}, {"Product": "cookies", "Quantity": 4, "UnitPrice": 5, "LineItemPrice": 20}]}
#{"BillNumber": 1245, "BillTotal": 3000, "StoreLocation": "New York", "BillDetails": [{"Product": "Soda", "Quantity": 10, "UnitPrice": 2, "LineItemPrice": 20}, {"Product": "Chips", "Quantity": 5, "UnitPrice": 3, "LineItemPrice": 15}, {"Product": "cookies", "Quantity": 4, "UnitPrice": 5, "LineItemPrice": 20}]}

"""
# json object to JSON string with identation
# for restaurant in data["BillDetails"]:
      # del restaurant["Product"]
      # data_new = json.dumps(data, indent=2)
      # print(data_new)

# dumps object to JSON string with identation and sort
for restaurant in data["BillDetails"]:
    del restaurant["Product"]
    data_new = json.dumps(data, indent=2,sort_keys=True)
    print(data_new)
"""