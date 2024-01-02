#  Muhammd Muzamil - F2020266388
#  Scenerio 2 - Online Shopping System. 

#  I was high enough to comment how I applied OOP here, so please bear with me :)

#  OOP Concepts:
#  a) Inheritence (Done) - Product (Parent), Physical_Product (Child), Digital_Product (Child)
#  b) Polymorphism (Done) - print_details(), get_price(), total_price()
#  c) Abstraction (Done) - Quantity, Category
#  d) Encapsulation (Done) - Price, Quantity (Cannot Change the Price and Quantity from Main.)
#  e) Composition (Done) - Product_IDS class's object being used in Products class.


import os
import time


class Product_IDS():
    def __init__(self) -> None:
        self.id = 0

    def assign_id(self) -> int:
        self.id += 1
        return self.id

class Product:
    def __init__(self,name,price,quantity,product_id) -> None:
        self.name = name
        self.__price = price
        self.__quantity = quantity
        self.product_id = product_id.assign_id()

    def get_price(self):
        return self.__price

    def print_details(self):
        pass

    def total_price(self):
        pass

    def decrease_quantity(self):
        self.__quantity -= 1

    def increase_quantity(self):
        self.__quantity += 1

    def get_quantity(self) -> int:
        return self.__quantity

    def get_product_id(self) -> int:
        return self.product_id


class Physical_Product(Product):
    def __init__(self, name, price, storage, quantity, product_id) -> None:
        super().__init__(name, price, quantity, product_id)
        self.product_category = "physical"
        self.storage = storage

    def print_details(self):
        print(f"Product ID: {self.get_product_id()}\nName: {self.name}\nPrice: ${self.get_price()}\nStorage: {self.storage}\n")
    
    def total_price(self) -> int:
        total_price = 0
        total_price = 50 + self.get_price() # adding $50 shipping / handling fees.
        return total_price

class Digital_Product(Product):
    def __init__(self, name, price, plan, quantity, product_id) -> None:
        super().__init__(name, price, quantity, product_id)
        self.product_category = "digital"
        self.plan = plan

    def print_details(self):
        print(f"Product ID: {self.get_product_id()}\nName:{self.name}\nPrice: ${self.get_price()}\nPlan: {self.plan}\n")

    def total_price(self) -> int:
        return self.get_price()
    
class Shopping_Cart():
    def __init__(self) -> None:
        self.cart = []
        self.cart_product_ids = 0
    
    def count_product(self) -> int:
        return len(self.cart)
    
    def product_list_in_cart(self):
            for product in self.cart:
                print(f'{product.name} - ')
    
    def print_cart_products(self):
        if len(self.cart) == 0:
            print("\nYour cart is empty.")
        else:
            i = 1
            for product in self.cart:
                print(f'Product #{i}')
                product.print_details()
                i += 1
    
    def add_product(self, products, product_id) -> None:
        if products[product_id].get_quantity() > 0:
            self.cart.append(products[product_id])
            products[product_id].decrease_quantity()
            print(f"\n{products[product_id].name} has been added to the cart.")
            print("\nReturing to the menu.")
        else:
            print(f"We're sorry {products[product_id].name} is out of stock.")

    def remove_product(self, product_number, products ) -> None: # products = list of products in the main()
        product = self.cart[product_number -1]
        products[product.product_id - 1].increase_quantity()
        del self.cart[product_number - 1]
        print("\nItem has been removed from your cart.")
        print("\nReturing to the menu.")

    def check_out(self):
        self.print_cart_products()
        total_bill = 0
        for product in self.cart:
                total_bill += product.total_price()
        response = int(input(f"\nPhysical Products include $50 handling fee. \nTotal Bill:{total_bill}. \nDo you want to check out?\n 1 - Yes, 0 - No\nResponse: "))

        if response == 1:
            print("\nThank you for shopping!")
            print("\nReturing to the menu.")
            self.cart.clear()

        elif response == 0:
            pass

product_ids = Product_IDS() #  initializing product ids for assigning ids to products.
cart = Shopping_Cart() #  initializing shopping cart.

#  list of the products.
products = [
    Physical_Product("iPhone-15", 799, "256 GB", 10, product_ids), 
    Physical_Product("iPhone-15 Pro", 999, "512 GB", 10, product_ids),
    Physical_Product("MacBook Air M2", 1099, "1 TB GB", 5, product_ids),
    Physical_Product("Apple Watch Series 9", 399, " - ", 10, product_ids),
    Physical_Product("Apple AirPods", 179, " - ", 10, product_ids),
    Digital_Product("Apple Music",11,"1 Month",100, product_ids),
    Digital_Product("Apple TV",15,"1 Month",100, product_ids),
    Digital_Product("Apple Podcast",15,"1 Month",100, product_ids),
    Digital_Product("Apple Books",18,"1 Month",100, product_ids),
    Digital_Product("Apple Fitness",18,"1 Month",100, product_ids),
    ]

# Interactive Menu
while True:
    print("\n***** Apple Store *****\n")
    for product in products: # Display Product List
        product.print_details()

    print("******** Your Cart ********") # Display Cart Status
    print(f"Cart: {cart.count_product()}")
    cart.print_cart_products()
    print("***************************")

    try: #  taking valid input from user.
        user_response = int(input("\n1 - ADD, 2 - REMOVE, 3 - Check-out, 0 - Exit\nResponse: ")) # Display Actions and take user's input.
        
    except ValueError: #  incase user enters input other than int.
        print("\nPlease enter a valid reponse.")

    else: #  no exception raised.
        if user_response == 0: # Exit the shop :)
            break

        elif user_response == 1: #  add products to cart.   
            p_id = int(input("\nEnter Product ID to add it to the cart: "))
            if p_id <= len(products):    
                cart.add_product(products, p_id - 1)
                time.sleep(3)
                os.system('clear')
            else:
                print(f"\nNo product found with Product ID: {p_id}.")
                time.sleep(3)

        elif user_response == 2: #  remove product from cart.
            print("\n0 - Exit")
            p_number = int(input("\nEnter Product# to remove it from the cart: "))
            if p_number < cart.count_product():#  if cart has products.
                cart.remove_product(p_number,products)
                time.sleep(3)
                os.system('clear')
            elif p_number == 0:
                pass  
            else:#  else, return to menu.
                print("\nProduct# not found.")
                time.sleep(3)

        elif user_response == 3: #  check out from the shop.
            if cart.count_product() > 0: #  if cart has products, proceed to check-out.
                cart.check_out()  
                time.sleep(3)
                os.system('clear')
            else:#  else, return back to menu.
                print("\nNo products in the cart :(")
                time.sleep(3)
                os.system('clear')
        else:
            print("\nPlease enter a valid input.")