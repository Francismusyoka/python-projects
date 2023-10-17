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
        if quantity > 0:
            self.quantity = quantity
        else:
            self.quantity = 0

    def get_price_per_item(self):
        return self.price_per_item

    def set_price_per_item(self, price_per_item):
        if price_per_item > 0:
            self.price_per_item = price_per_item
        else:
            self.price_per_item = 0

    def get_invoice_amount(self):
        return self.quantity * self.price_per_item

# Example usage
invoice = Invoice("12345", "Widget", 5, 10.99)
print(f"Part Number: {invoice.get_part_number()}")
print(f"Part Description: {invoice.get_part_description()}")
print(f"Quantity: {invoice.get_quantity()}")
print(f"Price per Item: ${invoice.get_price_per_item():.2f}")
print(f"Invoice Amount: ${invoice.get_invoice_amount():.2f}")

# Update quantity and price per item (with invalid values)
invoice.set_quantity(-2)
invoice.set_price_per_item(-5.99)

print(f"Updated Quantity: {invoice.get_quantity()}")
print(f"Updated Price per Item: ${invoice.get_price_per_item():.2f}")
print(f"Updated Invoice Amount: ${invoice.get_invoice_amount():.2f}")
