import json
import pandas as pd
from datetime import date


class Staff:
    def __init__(self):
        self.member = []

    def add_member(self, name):
        self.member.append(name)
        print("Add new member successful...!")

    def get_member(self):
        return self.member


class Stock:
    def __init__(self):
        self.stocks_details = []

    def add_stocks(self, product, price, quantity):
        stocks_detail = {'product': product, 'price': price, 'quantity': quantity}
        self.stocks_details.append(stocks_detail)

    def add_bulk_stock(self, filepath):
        try:
            df = pd.read_excel(filepath)
            for index, row in df.iterrows():
                b_product = row['Product']
                b_price = row['Price']
                b_quantity = row['Quantity']
                self.add_stocks(b_product, b_price, b_quantity)
            print("Bulk stock upload successful...!")
        except Exception as e:
            print(e)

    def get_stocks_details(self):
        return self.stocks_details


class Order:
    def __init__(self):
        self.order_details = []

    def add_single_order(self, product, sell_price, sold_quantity):
        order_detail = {'product': product, 'price': sell_price, 'quantity': sold_quantity}
        self.order_details.append(order_detail)

    def add_bulk_order(self, filepath):
        try:
            df = pd.read_excel(filepath)
            for index, row in df.iterrows():
                o_product = row['Product']
                o_price = row['Price']
                o_quantity = row['Quantity']
                self.add_single_order(o_product, o_price, o_quantity)
            print("Bulk order upload successful.")
        except Exception as e:
            print(e)

    def get_orders_details(self):
        return self.order_details


class Shop(Staff, Stock, Order):
    def __init__(self):
        super().__init__()
        self.member = []
        self.stocks_details = []
        self.order_details = []

    def display_stock(self):
        if len(self.stocks_details) == 0:
            print("No stock available")
        else:
            for i, j in enumerate(self.get_stocks_details()):
                print(f"{i + 1}, Product: {j['product']}, Price: {j['price']}, Quantity: {j['quantity']}")

    def display_order(self):
        today = date.today().strftime("%d-%m-%Y")
        total_profit = 0

        if len(self.order_details) == 0:
            print("No order available")
        else:
            for i, j in enumerate(self.get_orders_details()):
                print(f"{i + 1}, Product: {j['product']}, Price: {j['price']}, Quantity: {j['quantity']}")

        for order in self.order_details:
            for stock in self.stocks_details:
                if order['product'] == stock['product']:

                    profit = (order['price'] - stock['price']) * order['quantity']
                    total_profit += profit
                    stock['quantity'] -= order['quantity']
                    break

        df = pd.DataFrame(self.order_details)
        df['Date'] = today
        df['Daily profit'] = total_profit
        df.to_excel('Daily_seles_report.xlsx', sheet_name='Daily_sales')
        print(f"Daily sales report excel file download.")

    def remaining_stock(self):
        remaining_stock = []
        today = date.today().strftime("%d-%m-%Y")
        for stock in self.stocks_details:
            if stock['quantity'] > 0:
                remaining_stock.append(stock)

        print("Remaining stocks")
        for stock in self.stocks_details:
            print(f"Product: {stock['product']}, Price: {stock['price']}, Quantity: {stock['quantity']}")

        df = pd.DataFrame(self.stocks_details)
        df['Date'] = today
        df.to_excel('remaining_stock.xlsx', sheet_name='remaining_stock')
        print(f"Remaining stock report excel file download.")


if __name__ == "__main__":

    shop = Shop()

    while True:
        print("*-----* Shop Management *-----*")
        print("1. Add new staff member")
        print("2. Shop Owner add stocks details")
        print("3. Order table")
        print("4. Show Stock details")
        print("5. Show Order details")
        print("6. Live dashboard of remaining stocks")
        print("7. Exit")

        choice = input("Enter a number: ")

        if choice == '1':
            name = input("Enter a name you have to add: ").lower()
            shop.add_member(name)

        elif choice == '2':
            print("A. Single stock upload")
            print("B. Bulk stock upload through (excel file)")

            sub_choice = input("Enter a your option (A-B): ")
            if sub_choice == "A":
                product = input("Enter Product name: ")
                price = float(input("Enter price: "))
                quantity = int(input("Enter quantity: "))
                shop.add_stocks(product, price, quantity)
                print("Single stock upload successful.")

            elif sub_choice == "B":
                path = input("Enter excel file path: ")
                shop.add_bulk_stock(path)
            else:
                print("Invalid choice. Please try again")

        elif choice == "3":
            print("A. Shop owner add multiple order details(excel file)")
            print("B. Shop staff add single order detail")

            sub_choice = input("Enter a your option (A-B): ")

            if sub_choice == "A":
                path = input("Enter excel file path: ")
                shop.add_bulk_order(path)

            elif sub_choice == "B":
                staff_name = input("Enter a staff name: ").lower()
                if staff_name in shop.member:
                    product = input("Enter Product name: ")
                    price = float(input("Enter price: "))
                    quantity = int(input("Enter quantity: "))
                    shop.add_single_order(product, price, quantity)
                    print("Single order upload successful.")
                else:
                    print("No staff member sorry.. please add staff member")
            else:
                print("Invalid choice. Please try again")

        elif choice == "4":
            print("==== Stock details ====")
            shop.display_stock()

        elif choice == "5":
            print("==== Order details ====")
            shop.display_order()

        elif choice == "6":
            shop.remaining_stock()

        elif choice == "7":
            with open('staff.json', 'w') as staff_file:
                json.dump(shop.member, staff_file, indent=4)
            with open('stock.json', 'w') as stock_file:
                json.dump(shop.stocks_details, stock_file, indent=4)
            with open('order.json', 'w') as order_file:
                json.dump(shop.order_details, order_file, indent=4)
            print("Thank you for using Shop management system,,:)")
            break
        else:
            print("Invalid choice. Please try again")
