class product_informations:
    def __inti__(self):
        self.product_name = input("enter the product name : ")
        self.product_class = input("enter the product class : ")
        self.product_amount_by_dozen = int(input("enter how many dozan you want add : "))
        self.product_dozan_price = float(input("enter price for dozan : "))
        self.product_dozan_price_sale = (0.2 * self.product_dozan_price + self.product_dozan_price)
        self.Expiry_date = input("Expiry date of product year-month-day : ")
        self._date_lst = self.Expiry_date.split("-")
        self.date = "-".join(self._date_lst)

    product_list = []
    def warehouse_add(self,product):
        self.product_list.append(product)

    def authentication(self,name):
        for i in range(len(self.product_list)):
            if name in self.product_list[i].product.values():
                print()
                print("Authentication successful!")
                return self.product_list[i]


class warehouse (product_informations):
    product = {}
    print("you are now in the warehouse ")
    def __init__(self):

        super().__inti__()
        self.product['name'] = self.product_name
        self.product['info'] = (self.product_class,self.product_amount_by_dozen
                                    ,self.product_dozan_price,self.date,self.product_dozan_price_sale)
    def check(self):
        print(f"""information of {self.product['name']} product class ,product amount by dozen,
product dozan price,product dozan price sale,Expiry date on the following order :\n {self.product['info']}""")


    def export(self):
        amount = int(input("enter how many dozan you want export : "))
        if amount <= self.product_amount_by_dozen:
            self.product_amount_by_dozen = self.product_amount_by_dozen-amount
        else:
            print("you have not enough dozan from this product :")



running = True
while running:
    print()
    print("""Choose an option:

    1. add new product
    2. export product
    3. check specific commodity information
    4. Exit
    """)

    choice = int(input("1, 2 or 3: "))
    if choice == 1:
        print()
        c1 = warehouse()
        print()
        print("done")
    elif choice == 2:
        name = input("enter your product name : ")
        current_product = c1.authentication(name)
        if current_product:
            com_in = True
            while com_in:
                c1.export()
        else:
            print("the product not found")
    elif choice == 3:
        name = input("enter your product name : ")
        current_product = c1.authentication(name)
        if current_product:
            com_in = True
            while com_in:
                print()
                c1.check()
        else:
            print("the product not found")

    elif choice == 4:
        print()
        print("Goodbye!")
        running = False

