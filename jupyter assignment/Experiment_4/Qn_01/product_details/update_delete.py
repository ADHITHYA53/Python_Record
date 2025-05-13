from product_details.entry_display import product_list

def update_product():
    name=input("Enter the product to be updated : ")
    for product in product_list:
        if product['name'].lower() == name.lower():
            product['name'] = input("Enter the new name :")
            product['price'] =float(input("Enter the new price of the product : "))
            product['quantity'] = int(input("Enter the new quantity of the product : "))
            print(f"Product '{name}' updated successfully.")
            break
        if product not in product_list:
            print(f"Product '{name}' not found.")

def delete_product():
    name=input("Enter the product to delete : ")
    for product in product_list:
        if product['name'].lower() == name.lower():
            product_list.remove(product)
            print(f"Product '{name}' deleted successfully.")
            break
        if product not in product_list:
            print(f"Product '{name}' not found.")
    