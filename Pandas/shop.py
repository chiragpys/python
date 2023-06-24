import json

class ShopPayeeRecordsManager:
    def __init__(self):
        self.users_file = 'users_data.json'
        self.staff_file = 'staff_data.json'
        self.stocks_file = 'stocks_data.json'
        self.orders_file = 'orders_data.json'
        self.users_data = self.load_data(self.users_file)
        self.staff_data = self.load_data(self.staff_file)
        self.stocks_data = self.load_data(self.stocks_file)
        self.orders_data = self.load_data(self.orders_file)
        self.current_user = None

    def load_data(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
                return data
        except FileNotFoundError:
            return []

    def save_data(self, data, file_path):
        with open(file_path, 'w') as file:
            json.dump(data, file)

    def create_user(self, username, password, role):
        user = {
            'username': username,
            'password': password,
            'role': role
        }
        self.users_data.append(user)
        self.save_data(self.users_data, self.users_file)
        print("User created successfully.")

    def authenticate_user(self, username, password):
        for user in self.users_data:
            if user['username'] == username and user['password'] == password:
                self.current_user = user
                return True
        return False

    def add_staff_member(self):
        if self.current_user['role'] != 'owner':
            print("You don't have permission to perform this operation.")
            return

        staff_name = input("Enter staff member name: ")
        self.staff_data.append(staff_name)
        self.save_data(self.staff_data, self.staff_file)
        print(f"Staff member '{staff_name}' added successfully.")

    def add_stock_details(self):
        if self.current_user['role'] != 'owner':
            print("You don't have permission to perform this operation.")
            return

        stock_name = input("Enter stock name: ")
        stock_price = float(input("Enter stock price: "))
        stock_quantity = int(input("Enter stock quantity: "))
        stock = {
            'name': stock_name,
            'price': stock_price,
            'quantity': stock_quantity
        }
        self.stocks_data.append(stock)
        self.save_data(self.stocks_data, self.stocks_file)
        print(f"Stock '{stock_name}' added successfully.")

    def bulk_stock_upload(self, file_path):
        if self.current_user['role'] != 'owner':
            print("You don't have permission to perform this operation.")
            return

        # Code to process the Excel file and extract stock details
        for stock in extracted_stocks:
            self.stocks_data.append(stock)
        self.save_data(self.stocks_data, self.stocks_file)
        print("Bulk stock upload completed.")

    def add_order_details(self):
        order_name = input("Enter product name: ")
        order_price = float(input("Enter selling price: "))
        order_quantity = int(input("Enter sold quantity: "))
        order = {
            'name': order_name,
            'price': order_price,
            'quantity': order_quantity
        }
        self.orders_data.append(order)
        self.save_data(self.orders_data, self.orders_file)
        print("Order details added successfully.")

    def generate_daily_sales_report(self):
        if self.current_user['role'] != 'owner':
            print("You don't have permission to perform this operation.")
            return

        # Code to generate the sales report
        # Include daily profit and loss summary and remaining stock details
        report = generate_report(self.orders_data, self.stocks_data)
        with open('daily_sales_report.xls', 'w') as file:
            file.write(report)
        print("Daily sales report generated and downloaded.")

    def display_live_dashboard(self):
        # Code to display the live dashboard of remaining stocks
        dashboard = generate_dashboard(self.stocks_data)
        print(dashboard)

    def main(self):
        while True:
            print("\n=== Shop Payee Records Management ===")
            print("1. Create user")
            print("2. Login")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                role = input("Enter role (owner/staff): ")
                self.create_user(username, password, role)
            elif choice == '2':
                username = input("Enter username: ")
                password = input("Enter password: ")
                if self.authenticate_user(username, password):
                    print("Login successful.")
                    if self.current_user['role'] == 'owner':
                        self.owner_menu()
                    else:
                        self.staff_menu()
                else:
                    print("Invalid credentials.")
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")

    def owner_menu(self):
        while True:
            print("\n=== Owner Menu ===")
            print("1. Add new staff member")
            print("2. Add stock details")
            print("3. Bulk stock upload through Excel file")
            print("4. Generate and download daily sales report")
            print("0. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_staff_member()
            elif choice == '2':
                self.add_stock_details()
            elif choice == '3':
                file_path = input("Enter the path to the Excel file: ")
                self.bulk_stock_upload(file_path)
            elif choice == '4':
                self.generate_daily_sales_report()
            elif choice == '0':
                self.current_user = None
                break
            else:
                print("Invalid choice. Please try again.")

    def staff_menu(self):
        while True:
            print("\n=== Staff Menu ===")
            print("1. Add order details")
            print("2. Display live dashboard of remaining stocks")
            print("0. Logout")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.add_order_details()
            elif choice == '2':
                self.display_live_dashboard()
            elif choice == '0':
                self.current_user = None
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    manager = ShopPayeeRecordsManager()
    manager.main()
