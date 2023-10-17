class Invoice:
    def __init__(self, part_number, part_description, quantity, price_per_item):
        self.part_number = part_number
        self.part_description = part_description
        self.quantity = quantity
        self.price_per_item = price_per_item

    def get_part_number(self):
        return self.part_number

    def set_part_number(self, part_number):
        self.part_number = part_number

    def get_part_description(self):
        return self.part_description

    def set_part_description(self, part_description):
        self.part_description = part_description

    def get_quantity(self):
        return self.quantity

    def set_quantity(self, quantity):
        if quantity < 0:
            self.quantity = 0
        else:
            self.quantity = quantity

    def get_price_per_item(self):
        return self.price_per_item

    def set_price_per_item(self, price_per_item):
        if price_per_item < 0:
            self.price_per_item = 0
        else:
            self.price_per_item = price_per_item

    def get_invoice_amount(self):
        return self.quantity * self.price_per_item

# Example usage:
invoice = Invoice("123456", "Hammer", 2, 19.40)

# Print the invoice amount
print(invoice.get_invoice_amount())

# Output:
# 38.80
