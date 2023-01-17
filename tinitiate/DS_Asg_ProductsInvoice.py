# Products
#   *Price
# Define Product
# Define price

# Invoice
# Create Cart
# Add / edit Cart
# * Apply Discount (% or $value)
# * Calc Total

class ProductsSuppliers():

    product_details = []
    shopping_cart = {}

    def display_products(self):
        print(self.product_details)

    def add_products(self, prod_name, price):
        product_detail = {}
        product_detail["prod_name"]=prod_name
        product_detail["price"]=price
        self.product_details.append(product_detail)

    def create_cust_cart(self,cust_id,cust_name):
        cust_details={}
        cust_details["cust_id"]=cust_id
        cust_details["cust_name"]=cust_name
        self.shopping_cart["cust_details"]=cust_details

    def add_product(self,prod_name,qty):
        line_item={}
        line_item["prod_name"]=prod_name
        line_item["qty"]=qty
        self.shopping_cart["prod_details"].append(line_item)

    def show_cust_cart(self):
        print(self.shopping_cart)

# Create Object
a = ProductsSuppliers()

# Define Products
# ###################################
a.add_products("Apple", 1)
a.add_products("Peanuts", 2)
a.add_products("Cooking Oil", 5)
a.add_products("Juice", 2)
#
a.display_products()

# Shopping Cart
# ####################################
a.create_cust_cart(1, "a")
a.add_product("Apple",3)
a.add_product("Peanuts",5)
a.show_cust_cart()

# Calculate Totals
# ####################################
#
# Total "function calls"
#
# a.show_cust_cart()

"""
{'cust_details': {'cust_id': 1, 'cust_name': 'a'}, 
 'prod_details': [ {'prod_name': 'Apple', 'qty': 3}    # INVOICE LINE ITEM 1
                  ,{'prod_name': 'Peanuts', 'qty': 5}  # INVOICE LINE ITEM 2
                 ]
 
 }
"""