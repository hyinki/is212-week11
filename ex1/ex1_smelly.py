# class OrderProcessor:
#     def process_order(self, order):
#         # Step 1: Validate order details
#         if not order.get("customer_id"):
#             raise ValueError("Customer ID is required.")
#         if not order.get("items"):
#             raise ValueError("Order must contain items.")

#         # Step 2: Calculate total price
#         total_price = 0
#         for item in order["items"]:
#             total_price += item["price"] * item["quantity"]

#         # Step 3: Apply discounts if applicable
#         if order.get("discount_code") == "SUMMER20":
#             total_price *= 0.8  # 20% discount
#         elif order.get("discount_code") == "WELCOME10":
#             total_price *= 0.9  # 10% discount

#         # Step 4: Update inventory
#         for item in order["items"]:
#             item_id = item["id"]
#             quantity = item["quantity"]
#             # Code to update inventory for each item
#             # (for simplicity, let's assume a simple print statement here)
#             print(f"Updating inventory for item {item_id}, reducing stock by {quantity}.")

#         # Step 5: Generate receipt
#         receipt = f"Customer ID: {order['customer_id']}\n"
#         receipt += "Items:\n"
#         for item in order["items"]:
#             receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
#         receipt += f"Total: ${total_price:.2f}\n"

#         # Step 6: Send confirmation email
#         print(f"Sending email to customer {order['customer_id']} with receipt:\n{receipt}")

#         return receipt

class OrderProcessor:
    def process_order(self, order):
        self._validate_order(order)
        total_price = self._calculate_total_price(order)
        total_price = self._apply_discount(order, total_price)
        self._update_inventory(order)
        receipt = self._generate_receipt(order, total_price)
        self._send_confirmation_email(order["customer_id"], receipt)
        return receipt

    def _validate_order(self, order):
        if not order.get("customer_id"):
            raise ValueError("Customer ID is required.")
        if not order.get("items"):
            raise ValueError("Order must contain items.")

    def _calculate_total_price(self, order):
        total_price = 0
        for item in order["items"]:
            total_price += item["price"] * item["quantity"]
        return total_price

    def _apply_discount(self, order, total_price):
        if order.get("discount_code") == "SUMMER20":
            total_price *= 0.8  # 20% discount
        elif order.get("discount_code") == "WELCOME10":
            total_price *= 0.9  # 10% discount
        return total_price

    def _update_inventory(self, order):
        for item in order["items"]:
            item_id = item["id"]
            quantity = item["quantity"]
            # Simulate inventory update with print statement
            print(f"Updating inventory for item {item_id}, reducing stock by {quantity}.")

    def _generate_receipt(self, order, total_price):
        receipt = f"Customer ID: {order['customer_id']}\n"
        receipt += "Items:\n"
        for item in order["items"]:
            receipt += f"- {item['name']}: {item['quantity']} x ${item['price']}\n"
        receipt += f"Total: ${total_price:.2f}\n"
        return receipt

    def _send_confirmation_email(self, customer_id, receipt):
        print(f"Sending email to customer {customer_id} with receipt:\n{receipt}")
