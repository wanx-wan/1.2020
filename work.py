class Shop:
    stores = "There is no store you are looking for."
    payment = "This type of payment is not supported."
    quantity = "You will receive a discount of at least 20%, up to 70% if you choose an available item."
    price = "You have not selected the item."

    def __init__(self, product, stores, quantity, price, payment):
        if product == "vegetable":
            self.product = "Lettuce"
            if stores == "mall" or "market" or "supermarket" or "shops":
                self.stores = "UBU vegetable shops."
            else:
                self.stores = stores
                if quantity >= 5:
                    self.quantity = "You get a 50% discount."
                    self.price = "Currently, you have to pay 50% of the full price."
                else:
                    self.quantity = "Please purchase additional items to receive a 50% discount."
                    self.price = "Currently, you have to pay 50% of the full price."
                    if payment == "Visa Card" or "Master Card" or "JCB" \
                            or "Internet Banking" \
                            or 'Online Direct ' \
                               'Debit' or "Bill " \
                                          "Payment" or "AirPay":
                        self.payment = "ThailandPost"
                    elif payment == "Cash on delivery":
                        self.payment = "Flash express"
                    else:
                        self.payment = payment

        elif product == "fruit":
            self.product = "Mango"
            if stores == "mall" or "market" or "supermarket" or "shops":
                self.stores = "UBU fruit shops."
            else:
                self.stores = stores
                if quantity >= 10:
                    self.quantity = "You get a 70% discount."
                    self.price = "Currently, you have to pay 30% of the full price."
                else:
                    self.quantity = "Please purchase additional items to receive a 70% discount."
                    self.price = price
                    if payment == "Visa Card" or "Master Card" or "JCB" or "Internet Banking" \
                            or "Online Direct Debit" \
                            or "Bill Payment" \
                            or "AirPay":
                        self.payment = "ThailandPost"
                    elif payment == "Cash on delivery":
                        self.payment = "Flash express"
                    else:
                        self.payment = payment

        elif product == "Select products for the whole shop":
            self.product = "You choose both types."
            if stores == "mall" or "market" or "supermarket" or "shops":
                self.stores = "UBU vegetable and fruit shops."
            else:
                self.stores = stores
                if quantity >= 20:
                    self.quantity = "You get a 20% discount."
                    self.price = "Currently, you have to pay 80% of the full price."
                else:
                    self.quantity = "Please purchase additional items to receive a 20% discount."
                    self.price = "Currently, you have to pay full price."
                    if payment == "Visa Card" or "Master Card" or "JCB" \
                            or "Internet Banking" \
                            or "Online Direct Debit" \
                            or "Bill Payment" \
                            or "AirPay":
                        self.payment = "ThailandPost"
                    elif payment == "Cash on delivery":
                        self.payment = "Flash express"
                    else:
                        self.payment = payment
        else:
            self.product = "The product you are currently selecting does not exist. If you want the product, " \
                           "please make a new one. "
            if stores == "mall" or "market" or "supermarket" or "shops":
                self.stores = "There are no participating stores."
            else:
                self.stores = stores
                if quantity >= 5:
                    self.quantity = quantity
                    self.price = price
                else:
                    self.quantity = quantity
                    self.price = price
                    if payment == "Visa Card" or "Master Card" or "JCB" \
                            or "Internet Banking" \
                            or "Online Direct Debit" \
                            or "Bill Payment" \
                            or "AirPay":
                        self.payment = "Please make a new product list."
                    elif payment == "Cash on delivery":
                        self.payment = "Please make a new product list."
                    else:
                        self.payment = "Please make a new product list."

    def displayData(self):
        print("Thank you for purchasing products through Shop application. ", "Product of your choice:", self.product,
              "Stores:", self.stores, "Quantity:", self.quantity, "You have to pay:", self.price,
              "Delivery", self.payment)
        print(Shop)


obj1 = Shop("fruit", "mall", 5, 250, "AirPay")
obj1.displayData()
