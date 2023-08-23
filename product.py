class Product:
    def __init__(self):
        self.name = ""
        self.price = 0.0
        self.quantity = 0

def display_menu():
    print("\n------ Product Management System ------")
    print("1. Add a product")
    print("2. Edit a product")
    print("3. Remove a product")
    print("4. Print receipt")
    print("5. Exit")
    print("---------------------------------------")

def add_product(products, num_products):
    if num_products >= 100:
        print("Cannot add more products. Maximum capacity reached.")
        return

    product = Product()
    product.name = input("Enter the name of the product: ")
    product.price = float(input("Enter the price of the product (in Naira): "))
    product.quantity = int(input("Enter the quantity of the product: "))

    products.append(product)
    num_products += 1

def edit_product(products):
    if not products:
        print("No products to edit.")
        return

    target_name = input("Enter the name of the product to edit: ")

    for product in products:
        if product.name == target_name:
            product.price = float(input("Enter the new price of the product (in Naira): "))
            product.quantity = int(input("Enter the new quantity of the product: "))
            print("Product updated successfully.")
            return

    print("Product not found.")

def remove_product(products):
    if not products:
        print("No products to remove.")
        return

    target_name = input("Enter the name of the product to remove: ")

    for product in products:
        if product.name == target_name:
            products.remove(product)
            print("Product removed successfully.")
            return

    print("Product not found.")

def calculate_total_cost(products):
    total_cost = 0.0
    for product in products:
        total_cost += product.price * product.quantity
    return total_cost

def print_receipt(products, total_cost):
    print("\n---- Receipt ----")
    for product in products:
        print(f"{product.name} x{product.quantity}: ₦{product.price * product.quantity:.2f}")
    print("-----------------")
    print(f"Subtotal: ₦{total_cost:.2f}")
    print("-----------------")

def main():
    products = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_product(products, len(products))
        elif choice == '2':
            edit_product(products)
        elif choice == '3':
            remove_product(products)
        elif choice == '4':
            total_cost = calculate_total_cost(products)
            print_receipt(products, total_cost)
        elif choice == '5':
            print("Thank you for using our system!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
