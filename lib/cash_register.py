#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.items.extend([title] * quantity)
        self.total += price * quantity
        self.last_transaction = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            self.total = round(self.total, 2)

            total_display = f"{self.total:.2f}"
            if total_display.endswith(".00"):
                total_display = total_display[:-3]

            print(f"After the discount, the total comes to ${total_display}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction > 0:
            self.total -= self.last_transaction
            self.last_transaction = 0
            if self.items:
                for _ in range(self.items.count(self.items[-1])):
                    self.items.pop()
        else:
            print("No transaction to void.")
