from tabulate import tabulate
import csv
class Item:
    pay_rate = 1
    def __init__(self, name: str, price: float ,quantity: int,):
        assert price >= 0 and quantity >= 0
        self.name = name
        self.price = price
        self.quantity = quantity
    def total_price(self):
        return int(self.price * self.quantity)
    def total_paid(self):
        return int(self.total_price() * Item.pay_rate)
    def data(self):
        return [self.name, self.price, self.quantity, self.total_price(), self.total_paid()]
# ------------------------------------------------------------------------------------------------
headers = ["Name", "Price", "Quantity","Total Price","Total Paid(after discount)"]
count = int(input("How many items do you want? "))
items = []
for i in range(count):
    item_name = input("Enter item name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    item = Item(item_name, price, quantity)
    items.append(item)
discount = input("Do you want discount? [y/n]")
if discount.upper().strip() == "Y":
    rate = int(input("Enter rate of discount: "))
    Item.pay_rate = (1 - (rate / 100))
else:
    Item.pay_rate = 1
print(tabulate([item.data() for item in items], headers, tablefmt="fancy_grid"))
with open("inventory.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(headers)

    for item in items:
        writer.writerow(item.data())

