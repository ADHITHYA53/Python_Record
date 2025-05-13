product_list=[]  # empty list to store the data

def add_product():
    name = input("Enter the name of the product :")
    price = float(input("Enter the price of the product : ₹ "))
    quantity = int(input("Enter product quantity :"))
    product_list.append({"name" : name , "price" : price, "quantity" : quantity })
    print(f"{name} added successfully")

def display_products():
    print("Available Products")
    for product in product_list:
        print(f"Product:{product['name']} \t Price:₹{product['price']} \t Quantity:{product['quantity']}")