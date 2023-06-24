import json
import pandas as pd
from datetime import date


class Create_user:
    def __init__(self):
        self.shop_data = self.load_data()
        self.current_user = None
        self.current_user_id = None
        self.current_shop = None
        self.current_shop_id = None
        self.current_staff = None
        self.current_staff_id = None

    def load_data(self):
        try:
            with open('shop_data.json', 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return {
                'user': [],
                'shop_name': [],
                'staff': [],
                'stocks': [],
                'orders': [],
                'next_stock_id': 1,
                'next_order_id': 1,
            }

    def save_data(self):
        with open('shop_data.json', 'w') as file:
            json.dump(self.shop_data, file, indent=4)

    def create_user(self):
        id = int(input("Enter id: "))
        username = input("Enter username: ")
        for i in self.shop_data['user']:
            if i['id'] == id:
                print("This user id already registered.,")
                break
        else:
            user = {
                'id': id,
                'username': username,
            }
            self.shop_data['user'].append(user)
            self.save_data()

    def authenticate_user(self, id):
        for user in self.shop_data['user']:
            if user['id'] == id:
                self.current_user = user['username']
                self.current_user_id = user['id']
                return True
        return False

    def add_shop(self):
        print("Do you become a partner ? (Yes or No)(Y/N).")
        partner = input("Enter Y/N : ").lower()
        if partner == 'n':
            shop_id = int(input("Enter shop id: "))
            shop_name = input("Enter Shop name: ")
            for i in self.shop_data['shop_name']:
                if i['shop_id'] == shop_id:
                    print("This shop id already registered.,")
                    break
            else:
                shop = {
                    'shop_id': shop_id,
                    'shop_name': shop_name,
                    'owner_id': self.current_user_id,
                }
                self.shop_data['shop_name'].append(shop)
                self.save_data()
                print(f"Shop {shop_name} add successful..")

        elif partner == 'y':
            shop_id = int(input("Enter shop id: "))
            shop_name = input("Enter Shop name: ")

            partner_id = set()
            paetners_id = []
            while True:
                p_id = int(input("Enter partner id (0 to finish): "))
                if p_id == 0:
                    break
                partner_id.add(p_id)

            for i in self.shop_data['shop_name']:
                if i['shop_id'] == shop_id:
                    print("This shop id already registered.,")
                    break
            else:
                owner_id = 0
                for i in self.shop_data['user']:
                    if i['username'] == self.current_user and i['id'] in partner_id:
                        print("This is owner you can NOT to be partner..")
                        break

                    elif i['username'] == self.current_user:
                        owner_id = i['id']

                    elif partner_id is not None:
                        for j in partner_id:
                            if i['id'] == j:
                                paetners_id.append(j)

                if not paetners_id:
                    print("Partner Id NOT match.. ")

                else:
                    shop = {
                        'shop_id': shop_id,
                        'shop_name': shop_name,
                        'owner_id': owner_id,
                        'partner_id': paetners_id
                    }
                    self.shop_data['shop_name'].append(shop)
                    self.save_data()
                    print(f"Shop {shop_name} add successful and with {len(paetners_id)} partners")

    def get_shop(self):
        owner_id = self.current_user_id

        for j in self.shop_data['shop_name']:
            if "partner_id" in j and owner_id in j["partner_id"]:
                print(f"shop_id: {j['shop_id']}, shop_name: {j['shop_name']}")
            elif 'owner_id' in j and owner_id == j['owner_id']:
                print(f"shop_id: {j['shop_id']}, shop_name: {j['shop_name']}")

    def authenticate_shop(self, shop_id):
        owner_id = self.current_user_id

        for shop in self.shop_data['shop_name']:
            if "partner_id" in shop and owner_id in shop["partner_id"]:
                if shop['shop_id'] == shop_id:
                    self.current_shop = shop['shop_name']
                    self.current_shop_id = shop['shop_id']
                    return True

            elif 'owner_id' in shop and owner_id == shop['owner_id']:
                if shop['shop_id'] == shop_id:
                    self.current_shop = shop['shop_name']
                    self.current_shop_id = shop['shop_id']
                    return True
        return False

    def add_staff(self):
        id = int(input("Enter id: "))
        name = input("Enter Staff-name: ")
        staff_shopid = int(input("Enter shop Id: "))

        for i in self.shop_data['staff']:
            if i['id'] == id:
                print("This id already registered.,")
                break

        else:
            for shop in self.shop_data['shop_name']:
                if self.current_user_id == shop['owner_id'] and shop['shop_id'] == staff_shopid:
                    staff_name = {
                        'id': id,
                        'staff_name': name,
                        'owner_id': self.current_user_id,
                        'shop_id': staff_shopid,
                    }
                    self.shop_data['staff'].append(staff_name)
                    self.save_data()
                    print(f"Staff {name} member add successful")

    def authenticate_staff(self, staff_id):
        for staff in self.shop_data['staff']:
            if staff['id'] == staff_id:
                self.current_staff_id = staff['id']
                self.current_shop_id = staff['shop_id']
                self.current_staff = staff['staff_name']
                return True
        return False


class Stock(Create_user):
    def __init__(self):
        super().__init__()
        self.shop_data = self.load_data()

    def add_single_stock(self):
        today = date.today().strftime("%Y-%m-%d")
        product = input("Enter stock name: ")
        price = float(input("Enter stock price: "))
        quantity = int(input("Enter stock quantity: "))

        stock_id = self.shop_data['next_stock_id']
        self.shop_data['stocks'].append({
            'StockId': stock_id,
            'ShopId': self.current_shop_id,
            'OwnerId': self.current_user_id,
            'Date': today,
            'Product': product,
            'Price': price,
            'Quantity': quantity
        })
        self.shop_data['next_stock_id'] += 1

        self.save_data()
        print(f"Stock '{product}' added successfully.")

    def add_bulk_stock(self, filepath):
        try:
            df = pd.read_excel(filepath)
            for index, row in df.iterrows():
                b_date = row['Date']
                b_product = row['Product']
                b_price = row['Price']
                b_quantity = row['Quantity']

                stock_id = self.shop_data['next_stock_id']
                self.shop_data['stocks'].append({
                    'StockId': stock_id,
                    'ShopId': self.current_shop_id,
                    'OwnerId': self.current_user_id,
                    'Date': str(b_date).strip(" 00:00:00"),
                    'Product': b_product,
                    'Price': b_price,
                    'Quantity': b_quantity
                })
                self.shop_data['next_stock_id'] += 1

                self.save_data()
            print("Bulk stock upload successful...!")
        except Exception as e:
            print(e)


class Order(Stock):
    def __init__(self):
        super().__init__()
        self.shop_data = self.load_data()

    def add_single_order(self):
        today = date.today().strftime("%Y-%m-%d")
        product = input("Enter order name: ")
        price = float(input("Enter order price: "))
        quantity = int(input("Enter order quantity: "))

        order_id = self.shop_data['next_order_id']
        self.shop_data['orders'].append({
            'OrderId': order_id,
            'StaffId': self.current_staff_id,
            'StaffName': self.current_staff,
            'ShopId': self.current_shop_id,
            'Date': today,
            'Product': product,
            'Price': price,
            'Quantity': quantity,
            'from_stock': self.get_from_stock(self.current_shop_id, product, quantity)
        })
        self.shop_data['next_order_id'] += 1

        self.save_data()
        print(f"Order '{product}' added successfully.")

    def add_bulk_order(self, filepath):
        try:
            df = pd.read_excel(filepath)
            for index, row in df.iterrows():
                o_date = row['Date']
                o_product = row['Product']
                o_price = row['Price']
                o_quantity = row['Quantity']

                order_id = self.shop_data['next_order_id']
                self.shop_data['orders'].append({
                    'OrderId': order_id,
                    'ShopId': self.current_shop_id,
                    'OwnerId': self.current_user_id,
                    'Date': str(o_date).strip(" 00:00:00"),
                    'Product': o_product,
                    'Price': o_price,
                    'Quantity': o_quantity,
                    'from_stock': self.get_from_stock(self.current_shop_id, o_product, o_quantity)
                })
                self.shop_data['next_order_id'] += 1

                self.save_data()
            print("Bulk orders upload successful!")
        except Exception as e:
            print(e)

    def get_from_stock(self, shop_id, product_name, quantity):
        from_stock = []
        remaining_quantity = quantity
        for stock in self.shop_data['stocks']:
            if stock['ShopId'] == shop_id and stock['Product'] == product_name:
                from_stock_quantity = min(stock['Quantity'], remaining_quantity)
                if from_stock_quantity > 0:
                    from_stock_entry = {"stock_Id": stock['StockId'], 'quantity': from_stock_quantity}
                    from_stock.append(from_stock_entry)
                    stock['Quantity'] -= from_stock_quantity
                    remaining_quantity -= from_stock_quantity
                if remaining_quantity <= 0:
                    break
        return from_stock

    def remaining_stock(self):
        remaining_stock = []
        for stock in self.shop_data['stocks']:
            if self.current_shop_id == stock['ShopId']:
                stock['ShopName'] = self.current_shop
                stock['OwnerName'] = self.current_user

                remaining_stock.append(stock)
        try:
            df = pd.DataFrame(remaining_stock,)
            del df['ShopId']
            del df['OwnerId']

            df = df[['Date', 'ShopName', 'OwnerName', 'StockId', 'Product', 'Price', 'Quantity']]
            print(df)

            df.to_excel('remaining_stock.xlsx', sheet_name='remaining_stock')
            print(f"Remaining_stock report excel file download.")

        except Exception as e:
            print(e)

    def daily_sales_report(self):
        today = date.today().strftime("%Y-%m-%d")
        daily_sales = []
        for daily_order in self.shop_data['orders']:
            if self.current_shop_id == daily_order['ShopId'] and today == daily_order['Date']:
                price = daily_order['Price']
                quantity = daily_order['Quantity']
                total_cost = 0
                stock_dates = []
                stock_products = []
                stock_prices = []
                stock_quantities = []

                for stock in daily_order['from_stock']:
                    for i in self.shop_data['stocks']:
                        if i['StockId'] == stock['stock_Id']:
                            cost = i['Price']
                            total_cost += (cost * stock['quantity'])
                            stock_dates.append(i['Date'])
                            stock_products.append(i['Product'])
                            stock_prices.append(i['Price'])
                            stock_quantities.append(stock['quantity'])

                profit = (price * quantity) - total_cost
                daily_order['Profit'] = profit
                daily_order['stock-date'] = stock_dates
                daily_order['stock-Product'] = stock_products
                daily_order['stock-Price'] = stock_prices
                daily_order['stock-quantity'] = stock_quantities

                if daily_order.get('StaffId') is not None:
                    daily_order['ShopName'] = self.current_shop
                else:
                    daily_order['ShopName'] = self.current_shop
                    daily_order['OwnerName'] = self.current_user

                daily_sales.append(daily_order)
        try:
            if len(daily_sales) != 0:
                df = pd.DataFrame(daily_sales, )
                del df['ShopId']
                del df['from_stock']
                del df['StaffId']

                df = df.explode(['stock-date', 'stock-Product', 'stock-Price', 'stock-quantity'], ignore_index=True)

                if 'OwnerName' in df:
                    df = df[['Date', 'OwnerName', 'StaffName', 'ShopName', 'OrderId', 'Product', 'Price', 'Quantity',
                             'stock-date', 'stock-Product', 'stock-Price', 'stock-quantity', 'Profit']]
                else:
                    df = df[['Date', 'ShopName', 'StaffName', 'OrderId', 'Product', 'Price', 'Quantity',
                             'stock-date', 'stock-Product', 'stock-Price', 'stock-quantity', 'Profit']]
                print(df)

                df.to_excel('daily_sales_report.xlsx', sheet_name='daily_sales_report')
                print(f"daily_sales_report excel file download.")
            else:
                print("No today sales...")

        except Exception as e:
            print(e)

    def custom_sales_report(self):
        start_date = input("Enter start date(2023-05-31): ")
        end_date = input("Enter end date(2023-05-31): ")
        custom_sales = []
        for custom_order in self.shop_data['orders']:
            if self.current_shop_id == custom_order['ShopId'] and start_date <= custom_order['Date'] <= end_date:
                price = custom_order['Price']
                quantity = custom_order['Quantity']
                total_cost = 0
                total_cost = 0
                stock_dates = []
                stock_products = []
                stock_prices = []
                stock_quantities = []

                for stock in custom_order['from_stock']:
                    for i in self.shop_data['stocks']:
                        if i['StockId'] == stock['stock_Id']:
                            cost = i['Price']
                            total_cost += (cost * stock['quantity'])
                            stock_dates.append(i['Date'])
                            stock_products.append(i['Product'])
                            stock_prices.append(i['Price'])
                            stock_quantities.append(stock['quantity'])

                profit = (price * quantity) - total_cost
                custom_order['Profit'] = profit
                custom_order['stock-date'] = stock_dates
                custom_order['stock-Product'] = stock_products
                custom_order['stock-Price'] = stock_prices
                custom_order['stock-quantity'] = stock_quantities

                if custom_order.get('StaffId') is not None:
                    custom_order['ShopName'] = self.current_shop
                else:
                    custom_order['ShopName'] = self.current_shop
                    custom_order['OwnerName'] = self.current_user

                custom_sales.append(custom_order)
        try:
            if len(custom_sales) != 0:
                df = pd.DataFrame(custom_sales,)
                del df['ShopId']
                del df['OwnerId']
                del df['from_stock']

                df = df.explode(['stock-date', 'stock-Product', 'stock-Price', 'stock-quantity', ],
                                ignore_index=True)

                if 'StaffName' in df:
                    del df['StaffId']
                    df = df[['Date', 'OwnerName', 'StaffName', 'ShopName', 'OrderId', 'Product', 'Price', 'Quantity',
                             'stock-date', 'stock-Product', 'stock-Price', 'stock-quantity', 'Profit']]
                else:
                    df = df[['Date', 'OwnerName', 'ShopName', 'OrderId', 'Product', 'Price', 'Quantity',
                             'stock-date', 'stock-Product', 'stock-Price', 'stock-quantity', 'Profit']]
                print(df)

                df.to_excel('custom_sales_report.xlsx', sheet_name='custom_sales_report')
                print(f"custom_sales_report excel file download.")
            else:
                print(f"This date no sales record {start_date} to {end_date}.")

        except Exception as e:
            print(e)

    def all_sales_report(self):
        all_sales = []
        for all_order in self.shop_data['orders']:
            if self.current_shop_id == all_order['ShopId']:
                price = all_order['Price']
                quantity = all_order['Quantity']
                total_cost = 0
                stock_dates = []
                stock_products = []
                stock_prices = []
                stock_quantities = []

                for stock in all_order['from_stock']:
                    for i in self.shop_data['stocks']:
                        if i['StockId'] == stock['stock_Id']:
                            cost = i['Price']
                            total_cost += (cost * stock['quantity'])
                            stock_dates.append(i['Date'])
                            stock_products.append(i['Product'])
                            stock_prices.append(i['Price'])
                            stock_quantities.append(stock['quantity'])

                profit = (price * quantity) - total_cost
                all_order['Profit'] = profit
                all_order['stock-date'] = stock_dates
                all_order['stock-Product'] = stock_products
                all_order['stock-Price'] = stock_prices
                all_order['stock-quantity'] = stock_quantities

                if all_order.get('StaffId') is not None:
                    all_order['ShopName'] = self.current_shop
                else:
                    all_order['ShopName'] = self.current_shop
                    all_order['OwnerName'] = self.current_user

                all_sales.append(all_order)
        try:
            if len(all_sales) != 0:
                df = pd.DataFrame(all_sales, )
                del df['ShopId']
                del df['OwnerId']
                del df['from_stock']
                del df['StaffId']

                df = df.explode(['stock-date', 'stock-Product', 'stock-Price', 'stock-quantity', ],
                                ignore_index=True)

                if 'StaffName' in df:
                    df = df[['Date', 'OwnerName', 'StaffName', 'ShopName', 'OrderId', 'Product', 'Price', 'Quantity',
                             'stock-date', 'stock-Product', 'stock-Price', 'stock-quantity', 'Profit']]
                else:
                    df = df[['Date', 'OwnerName', 'ShopName', 'OrderId', 'Product', 'Price', 'Quantity',
                             'stock-date', 'stock-Product', 'stock-Price', 'stock-quantity', 'Profit']]
                print(df)
                df.to_excel('all_sales_report.xlsx', sheet_name='all_sales_report')
                print(f"all_sales_report excel file download.")
            else:
                print(f"This shop No {self.current_shop} sales")

        except Exception as e:
            print(e)


if __name__ == "__main__":
    shop = Order()

    def shop_manu():
        while True:
            print("\n=== Shop Management ===")
            print("1. Shop Owner add stocks details")
            print("2. Order table")
            print("3. Show sales report")
            print("4. remaining stock")
            print("5. Logout")

            choice = input("Enter a number: ")

            if choice == '1':
                print("A. Single stock upload")
                print("B. Bulk stock upload through (excel file)")

                sub_choice = input("Enter a your option (A-B): ").upper()
                if sub_choice == "A":
                    shop.add_single_stock()

                elif sub_choice == "B":
                    path = input("Enter excel file path: ")
                    shop.add_bulk_stock(path)
                else:
                    print("Invalid choice. Please try again")

            elif choice == "2":
                print("A. Shop owner add multiple order details(excel file)")

                sub_choice = input("Enter a your option (A-B): ").upper()

                if sub_choice == "A":
                    path = input("Enter excel file path: ")
                    shop.add_bulk_order(path)

                else:
                    print("Invalid choice. Please try again")

            elif choice == "3":
                print("1. Show daily sales report")
                print("2. Custom date report")
                print("3. All sales report")

                sub_choice = input("Enter a number: ")

                if sub_choice == '1':
                    shop.daily_sales_report()

                elif sub_choice == '2':
                    shop.custom_sales_report()

                elif sub_choice == '3':
                    shop.all_sales_report()

                else:
                    print("Invalid choice. Please try again")

            elif choice == "4":
                shop.remaining_stock()

            elif choice == "5":
                shop.current_shop = None
                shop.current_shop_id = None
                break
            else:
                print("Invalid choice. Please try again")

    def main():
        while True:
            print("\n=== Shop Management ===")
            print("1. Add new shop ")
            print("2. Add new staff member")
            print("3. Show Shop")
            print("4. Logout")

            choice = input("Enter a number: ")

            if choice == '1':
                shop.add_shop()

            elif choice == '2':
                shop.add_staff()

            elif choice == '3':
                shop.get_shop()
                id = int(input("Enter shop id into login shop: "))
                if shop.authenticate_shop(id):
                    print(f"Login shop id '{shop.current_shop_id}' shop name'{shop.current_shop}' successful.")
                    shop_manu()
                else:
                    print('Invalid shop id.')

            elif choice == "4":
                shop.current_user = None
                shop.current_user_id = None
                break
            else:
                print("Invalid choice. Please try again")

    def owner_manu():
        while True:
            print("\n=== Shop Management ===")
            print("1. Create user")
            print("2. Login")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                shop.create_user()

            elif choice == '2':
                id = int(input("Enter id: "))
                if shop.authenticate_user(id):
                    print(f"Login {shop.current_user} successful.")
                    main()
                else:
                    print('Invalid user.')

            elif choice == '0':
                break
            else:
                print('Invalid choice. Please try again')

    def staff_manu():
        while True:
            print("\n=== Shop Management ===")
            print("1. Login")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                staff_id = int(input("Enter staff-id: "))
                if shop.authenticate_staff(staff_id):
                    print(f"Login staff {shop.current_staff} successful.")
                    staff_submanu()
                else:
                    print('Invalid Staff Id...')

            elif choice == '0':
                break

            else:
                print("Invalid choice. Please try again")

    def staff_submanu():
        while True:
            print("\n=== Shop Management ===")
            print("1. Shop staff add single order detail")
            print("0. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                shop.add_single_order()

            elif choice == '0':
                shop.current_staff_id = None
                shop.current_shop_id = None
                break

            else:
                print("Invalid choice. Please try again")

    while True:
        print("\n=== Shop Management ===")
        print("1. Owner Manu")
        print("2. Staff Manu")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            owner_manu()

        elif choice == '2':
            staff_manu()

        elif choice == '0':
            break
        else:
            print('Invalid choice. Please try again')
