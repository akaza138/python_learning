class order():
    def __init__(self, order_id, customer_name, product_name, price , discount):
        self.order_id = order_id
        self.customer_name = customer_name
        self.product_name = product_name
        self.price = price
        self.__discount = discount
        
    def __final_cal (self):
        return self.price - self.__discount

    def admin_view(self):
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "product_name": self.product_name,
            "price": self.price,
            "discount": self.__discount,
            "total": self.__final_cal()
        }
    def customer_view(self):
        return {
            "order_id": self.order_id,
            "customer_name": self.customer_name,
            "product_name": self.product_name,
            "price": self.price,
            "total": self.__final_cal()
        }

class admin():
    def show_order(self, order):
        print("Admin View:")
        print(order.admin_view())

class customer():
    def show_order(self, order):
        print("Customer View:")
        print(order.customer_view())

order1 = order(1, "John Doe", "Laptop", 1000, 100)
admin1 = admin()
customer1 = customer()
print(admin1.show_order(order1))
print(customer1.show_order(order1))
