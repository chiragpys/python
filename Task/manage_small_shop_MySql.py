import pandas as pd
from datetime import date
from models import *


class Create_user:
    def __init__(self):
        self.engine = engine
        self.session = session
        self.current_user = None
        self.current_user_id = None
        self.current_shop = None
        self.current_shop_id = None
        self.current_staff = None
        self.current_staff_id = None

    def create_user(self):
        id = int(input("Enter id: "))
        username = input("Enter username: ")

        user = self.session.query(User).filter_by(id=id).first()
        if user:
            print("This user id already registered.")
        else:
            new_user = User(id=id, name=username)
            self.session.add(new_user)
            self.session.commit()
            print("User created successfully.")
        self.session.close()

    def authenticate_user(self):
        id = int(input("Enter id to Login: "))
        user = self.session.query(User).filter_by(id=id).first()
        if user:
            self.current_user = user.name
            self.current_user_id = user.id
            self.session.close()
            return True
        self.session.close()
        return False

    def add_shop(self):
        print("Do you want to become a partner? (Yes or No)")
        partner = input("Enter Y/N: ").lower()

        if partner == 'n':
            shop_id = int(input("Enter shop id: "))
            shop_name = input("Enter Shop name: ")

            shop = self.session.query(Shop).filter_by(id=shop_id).first()
            if shop:
                print("This shop id already registered.")
            else:
                new_shop = Shop(id=shop_id, shop_name=shop_name, owner_id=self.current_user_id)
                self.session.add(new_shop)
                self.session.commit()
                print(f"Shop {shop_name} added successfully.")
            self.session.close()

        elif partner == 'y':
            # shop_id = int(input("Enter shop id: "))
            shop_name = input("Enter Shop name: ")

            partner_ids = set()
            while True:
                p_id = int(input("Enter partner id (0 to finish): "))
                if p_id == 0:
                    break
                partner_ids.add(p_id)

            for pid in partner_ids:
                if pid == self.current_user_id:
                    print("Shop owner can't as partner..")
                    break
                else:
                    user = self.session.query(User).filter_by(id=pid).first()
                    if user:
                        shop = self.session.query(Shop).filter_by(shop_name=shop_name).first()
                        if not shop:
                            new_shop = Shop(shop_name=shop_name, owner_id=self.current_user_id)
                            user.partner_shops.append(new_shop)
                            self.session.add(new_shop)
                        else:
                            user.partner_shops.append(shop)
                    else:
                        print(f"User with ID {pid} does not exist.")
                        continue

            self.session.commit()
            self.session.close()
            print(f"Shop {shop_name} added successfully with {len(partner_ids)} partners.")

    def get_shop(self):
        owner_id = self.current_user_id
        shops = self.session.query(Shop).filter_by(owner_id=owner_id).all()

        for shop in shops:
            if owner_id == shop.owner_id:
                print(f"shop_id: {shop.id}, shop_name: {shop.shop_name}")

        partner_shops = self.session.query(User).filter_by(id=owner_id).first().partner_shops.order_by('id')
        for shop in partner_shops:
            print(f"shop_id: {shop.id}, shop_name: {shop.shop_name}")
        self.session.close()

    def authenticate_shop(self, shop_id):
        shop = self.session.query(Shop).filter_by(id=shop_id).first()
        if shop:
            self.current_shop = shop.shop_name
            self.current_shop_id = shop.id
            self.session.close()
            return True
        self.session.close()
        return False

    def add_staff(self):
        id = int(input("Enter id: "))
        name = input("Enter Staff-name: ")
        staff_shopid = int(input("Enter shop Id: "))

        staff = self.session.query(User).filter_by(id=id).first()
        if staff:
            print("This id already registered.")

        shop = self.session.query(Shop).filter_by(owner_id=self.current_user_id, id=staff_shopid).first()
        if shop:
            new_staff = User(id=id, name=name, role='staff', owner_id=self.current_user_id, shop_id=staff_shopid)
            self.session.add(new_staff)
            self.session.commit()
            print(f"Staff member {name} added successfully.")
        else:
            print("Shop ID not found or you don't have permission to add staff to that shop.")
        self.session.close()

    def authenticate_staff(self, staff_id):
        staff = self.session.query(User).filter_by(id=staff_id).first()
        if staff:
            self.current_staff_id = staff.id
            self.current_shop_id = staff.shop_id
            self.current_staff = staff.name
            self.session.close()
            return True
        self.session.close()
        return False


class Record(Create_user):
    def __init__(self):
        super().__init__()

    def remaining_stock(self):
        remaining_stock = []

        shop_name = self.session.query(Shop).filter_by(id=self.current_shop_id).first()
        owner_name = self.session.query(User).filter_by(id=self.current_user_id).first()

        stocks = (
            self.session.query(Stock)
            .join(Product)
            .filter(Stock.shop_id == self.current_shop_id, )
            .order_by(Stock.date)
        )

        for stock in stocks:
            values = {
                'Date': stock.date,
                'ShopName': shop_name.shop_name,
                'OwnerName': owner_name.name,
                'StockId': stock.id,
                'Product': stock.product.product,
                'Price': stock.price,
                'Quantity': stock.quantity
            }
            remaining_stock.append(values)
        try:
            df = pd.DataFrame(remaining_stock, )
            if df.empty:
                print("No Stock this shop..! ")
            else:
                # df = df[['Date', 'ShopName', 'OwnerName', 'StockId', 'Product', 'Price', 'Quantity']]
                print(df)

                df.to_excel('remaining_stock_MySql.xlsx', sheet_name='remaining_stock')
                print(f"Remaining_stock_MySql report excel file download.")

        except Exception as e:
            print(e)

    def daily_sales_report(self):
        today = date.today()
        daily_sales = []

        shop = self.session.query(Shop).filter_by(id=self.current_shop_id).first()
        owner = self.session.query(User).filter_by(id=self.current_user_id).first()

        orders = (
            self.session.query(Order)
            .join(Product)
            .join(order_stock_table)
            .filter(Order.shop_id == self.current_shop_id, )
            .order_by(Order.date)
            .all()
        )

        for order in orders:
            if order.date == today:
                staff = self.session.query(User).filter_by(id=order.staff_id).first()
                order_stock = self.session.query(order_stock_table).filter_by(order_id=order.id).all()
                stock_quantities = [stock.quantity_sold for stock in order_stock]
                stock_dates = [stock.date for stock in order.stocks]
                stock_products = [stock.product.product for stock in order.stocks]
                stock_prices = [stock.price for stock in order.stocks]

                total_cost = sum(stock_prices[i] * stock_quantities[i] for i in range(len(stock_prices)))
                # for i in range(len(stock_prices)):
                #     total_cost += stock_prices[i] * stock_quantities[i]

                profit = order.sell_price * order.sold_quantity - total_cost

                owner_name = None
                staff_name = None

                if staff is None:
                    owner_name = owner.name
                    staff_name = None

                elif staff.name:
                    owner_name = None
                    staff_name = staff.name

                values = {
                    'Date': order.date,
                    'OwnerName': owner_name,
                    'StaffName': staff_name,
                    'ShopName': shop.shop_name,
                    'OrderId': order.id,
                    'Product': order.product.product,
                    'SellPrice': order.sell_price,
                    'SoldQuantity': order.sold_quantity,
                    'stock-date': stock_dates,
                    'stock-Product': stock_products,
                    'stock-Price': stock_prices,
                    'stock-quantity': stock_quantities,
                    'Profit': profit,
                }
                daily_sales.append(values)

        try:
            if len(daily_sales) != 0:
                df = pd.DataFrame(daily_sales)

                df = df.explode(['stock-date', 'stock-Product', 'stock-Price', 'stock-quantity'], ignore_index=True)

                if 'OwnerName' in df:
                    df = df[['Date', 'OwnerName', 'StaffName', 'ShopName', 'OrderId', 'Product', 'SellPrice',
                             'SoldQuantity',
                             'stock-date', 'stock-Product', 'stock-Price', 'stock-quantity', 'Profit']]
                else:
                    df = df[['Date', 'ShopName', 'OrderId', 'Product', 'SellPrice', 'SoldQuantity',
                             'stock-date', 'stock-Product', 'stock-Price', 'stock-quantity', 'Profit']]
                print(df)

                df.to_excel('daily_sales_report_MySql.xlsx', sheet_name='daily_sales_report')
                print(f"daily_sales_report excel file download.")
            else:
                print("No today sales...")

        except Exception as e:
            print(e)

    def custom_sales_report(self):
        start_date = input("Enter start date(2023-05-31): ")
        end_date = input("Enter end date(2023-05-31): ")
        custom_sales = []

        shop = self.session.query(Shop).filter_by(id=self.current_shop_id).first()
        owner = self.session.query(User).filter_by(id=self.current_user_id).first()

        orders = (
            self.session.query(Order)
            .join(Product)
            .join(order_stock_table)
            .filter(Order.shop_id == self.current_shop_id, )
            .order_by(Order.date)
            .all()
        )

        for order in orders:
            if start_date <= str(order.date) <= end_date:
                staff = self.session.query(User).filter_by(id=order.staff_id).first()
                order_stock = self.session.query(order_stock_table).filter_by(order_id=order.id).all()
                stock_quantities = [stock.quantity_sold for stock in order_stock]
                stock_dates = [stock.date for stock in order.stocks]
                stock_products = [stock.product.product for stock in order.stocks]
                stock_prices = [stock.price for stock in order.stocks]

                total_cost = sum(stock_prices[i] * stock_quantities[i] for i in range(len(stock_prices)))
                # for i in range(len(stock_prices)):
                #     total_cost += stock_prices[i] * stock_quantities[i]

                profit = order.sell_price * order.sold_quantity - total_cost
                owner_name = None
                staff_name = None

                if staff is None:
                    owner_name = owner.name
                    staff_name = None

                elif staff.name:
                    owner_name = None
                    staff_name = staff.name

                values = {
                    'Date': order.date,
                    'OwnerName': owner_name,
                    'StaffName': staff_name,
                    'ShopName': shop.shop_name,
                    'OrderId': order.id,
                    'Product': order.product.product,
                    'SellPrice': order.sell_price,
                    'SoldQuantity': order.sold_quantity,
                    'stock-date': stock_dates,
                    'stock-Product': stock_products,
                    'stock-Price': stock_prices,
                    'stock-quantity': stock_quantities,
                    'Profit': profit,
                }
                custom_sales.append(values)
        try:
            if len(custom_sales) != 0:
                df = pd.DataFrame(custom_sales)

                df = df.explode(['stock-date', 'stock-Product', 'stock-Price', 'stock-quantity'], ignore_index=True)

                if 'StaffName' in df:
                    df = df[['Date', 'OwnerName', 'StaffName', 'ShopName', 'OrderId', 'Product', 'SellPrice',
                             'SoldQuantity',
                             'stock-date', 'stock-Product', 'stock-Price', 'stock-quantity', 'Profit']]
                else:
                    df = df[['Date', 'OwnerName', 'ShopName', 'OrderId', 'Product', 'SellPrice', 'SoldQuantity',
                             'stock-date', 'stock-Product', 'stock-Price', 'stock-quantity', 'Profit']]
                print(df)
                df.to_excel('custom_sales_report_MySql.xlsx', sheet_name='custom_sales_report')
                print(f"custom_sales_report excel file download.")
            else:
                print(f"This date no sales record {start_date} to {end_date}.")

        except Exception as e:
            print(e)

    def all_sales_report(self):
        all_sales = []

        shop = self.session.query(Shop).filter_by(id=self.current_shop_id).first()
        owner = self.session.query(User).filter_by(id=self.current_user_id).first()

        orders = (
            self.session.query(Order)
            .join(Product)
            .join(order_stock_table)
            .filter(Order.shop_id == self.current_shop_id, )
            .order_by(Order.date)
            .all()
        )

        for order in orders:
            staff = self.session.query(User).filter_by(id=order.staff_id).first()
            order_stock = self.session.query(order_stock_table).filter_by(order_id=order.id).all()
            stock_quantities = [stock.quantity_sold for stock in order_stock]
            stock_dates = [stock.date for stock in order.stocks]
            stock_products = [stock.product.product for stock in order.stocks]
            stock_prices = [stock.price for stock in order.stocks]

            total_cost = sum(stock_prices[i] * stock_quantities[i] for i in range(len(stock_prices)))
            # for i in range(len(stock_prices)):
            #     total_cost += stock_prices[i] * stock_quantities[i]

            profit = order.sell_price * order.sold_quantity - total_cost
            owner_name = None
            staff_name = None

            if staff is None:
                owner_name = owner.name
                staff_name = None

            elif staff.name:
                owner_name = None
                staff_name = staff.name

            values = {
                'Date': order.date,
                'OwnerName': owner_name,
                'StaffName': staff_name,
                'ShopName': shop.shop_name,
                'OrderId': order.id,
                'Product': order.product.product,
                'SellPrice': order.sell_price,
                'SoldQuantity': order.sold_quantity,
                'stock-date': stock_dates,
                'stock-Product': stock_products,
                'stock-Price': stock_prices,
                'stock-quantity': stock_quantities,
                'Profit': profit,
            }
            all_sales.append(values)

        try:
            if len(all_sales) != 0:
                df = pd.DataFrame(all_sales)

                df = df.explode(['stock-date', 'stock-Product', 'stock-Price', 'stock-quantity'], ignore_index=True)

                if 'StaffName' in df:
                    df = df[['Date', 'OwnerName', 'StaffName', 'ShopName', 'OrderId', 'Product', 'SellPrice',
                             'SoldQuantity',
                             'stock-date', 'stock-Product', 'stock-Price', 'stock-quantity', 'Profit']]
                else:
                    df = df[['Date', 'OwnerName', 'ShopName', 'OrderId', 'Product', 'SellPrice', 'SoldQuantity',
                             'stock-date', 'stock-Product', 'stock-Price', 'stock-quantity', 'Profit']]
                print(df)
                df.to_excel('all_sales_report_MySql.xlsx', sheet_name='all_sales_report')
                print("all_sales_report excel file download.")
            else:
                print(f"This shop No {self.current_shop} sales")

        except Exception as e:
            print(e)


class Stock_shop(Record):
    def __init__(self):
        super().__init__()

    def add_single_stock(self):
        product = input("Enter stock name: ").title()
        price = float(input("Enter stock price: "))
        quantity = int(input("Enter stock quantity: "))

        get_product = self.session.query(Product).filter_by(product=product, ).first()
        if not get_product:
            new_stock = Product(product=product)
            self.session.add(new_stock)
            self.session.commit()
            get_product = new_stock

        if get_product:
            new_details = Stock(product_id=get_product.product_id, price=price, quantity=quantity,
                                shop_id=self.current_shop_id)
            self.session.add(new_details)
            self.session.commit()
        else:
            print(f"Product '{product}' not found.")
        self.session.close()
        print(f"Stock '{product}' added successfully.")

    def add_bulk_stock(self, filepath):
        try:
            df = pd.read_excel(filepath)

            for index, row in df.iterrows():
                b_date = row['Date']
                b_product = row['Product']
                b_price = row['Price']
                b_quantity = row['Quantity']

                get_product = self.session.query(Product).filter_by(product=b_product, ).first()

                if not get_product:
                    new_stock = Product(product=b_product)
                    self.session.add(new_stock)
                    self.session.commit()
                    get_product = new_stock

                if get_product:
                    new_details = Stock(product_id=get_product.product_id, date=b_date, price=b_price,
                                        quantity=b_quantity,
                                        shop_id=self.current_shop_id)
                    self.session.add(new_details)
                    self.session.commit()
                else:
                    print(f"Product '{b_product}' not found.")

            self.session.close()
            print("Bulk stock upload successful!")
        except Exception as e:
            print(e)


class Order_shop(Stock_shop):
    def __init__(self):
        super().__init__()

    def add_single_order(self):
        product = input("Enter order Product name: ").title()
        sell_price = float(input("Enter order sell price: "))
        sold_quantity = int(input("Enter order sold quantity: "))

        get_product = self.session.query(Product).filter_by(product=product).first()

        new_details = Order(product_id=get_product.product_id, sell_price=sell_price,
                            sold_quantity=sold_quantity, shop_id=self.current_shop_id,
                            owner_id=self.current_user_id, staff_id=self.current_staff_id)
        self.session.add(new_details)
        self.session.commit()

        stocks = (
            self.session.query(Stock)
            .join(Product)
            .filter(Product.product == product, Stock.shop_id == self.current_shop_id, Stock.quantity > 0)
            .order_by(Stock.date)
        )

        remaining_quantity = sold_quantity
        for stock in stocks:
            if remaining_quantity <= stock.quantity:
                order_stock_values = {
                    'order_id': new_details.id,
                    'stock_id': stock.id,
                    'quantity_sold': remaining_quantity
                }
                self.session.execute(insert(order_stock_table).values(order_stock_values))
                stock.quantity -= remaining_quantity
                self.session.commit()
                break
            else:
                order_stock_values = {
                    'order_id': new_details.id,
                    'stock_id': stock.id,
                    'quantity': stock.quantity
                }
                self.session.execute(insert(order_stock_table).values(order_stock_values))
                remaining_quantity -= stock.quantity
                stock.quantity = 0
                self.session.commit()

        self.session.close()
        print(f"Order'{product}' added successfully.")

    def add_bulk_order(self, filepath):
        try:
            df = pd.read_excel(filepath)

            for index, row in df.iterrows():
                o_date = row['Date']
                o_product = row['Product']
                o_price = row['Price']
                o_quantity = row['Quantity']

                get_product = self.session.query(Product).filter_by(product=o_product).first()

                # if not get_product:
                #     new_order = OrderItems(product=o_product)
                #     self.session.add(new_order)
                #     self.session.commit()

                new_details = Order(product_id=get_product.product_id, date=o_date, sell_price=o_price,
                                    sold_quantity=o_quantity, shop_id=self.current_shop_id,
                                    owner_id=self.current_user_id, staff_id=self.current_staff_id)
                self.session.add(new_details)
                self.session.commit()

                stocks = (
                    self.session.query(Stock)
                    .join(Product)
                    .filter(Product.product == o_product, Stock.shop_id == self.current_shop_id, Stock.quantity > 0)
                    .order_by(Stock.date)
                )

                remaining_quantity = o_quantity
                for stock in stocks:
                    if remaining_quantity <= stock.quantity:
                        order_stock_values = {
                            'order_id': new_details.id,
                            'stock_id': stock.id,
                            'quantity_sold': remaining_quantity
                        }
                        self.session.execute(insert(order_stock_table).values(order_stock_values))
                        stock.quantity -= remaining_quantity
                        self.session.commit()
                        break
                    else:
                        order_stock_values = {
                            'order_id': new_details.id,
                            'stock_id': stock.id,
                            'quantity_sold': stock.quantity
                        }
                        self.session.execute(insert(order_stock_table).values(order_stock_values))
                        remaining_quantity -= stock.quantity
                        stock.quantity = 0
                        self.session.commit()

            self.session.close()
            print("Bulk stock upload successful!")
        except Exception as e:
            print(e)


if __name__ == "__main__":
    shop = Order_shop()


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
                # id = int(input("Enter id: "))
                if shop.authenticate_user():
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
