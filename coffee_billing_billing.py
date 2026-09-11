# Coffee Shop Billing Program

# Item prices
coffee_price = 120
pastry_price = 80

# quantties of item
coffee_qty= int(input("How many cofffee do you want"))
pastry_qty= int(input("How many pastries do you want"))           

#GST rate
gst_rate = 0.18

# Calculate amount before GST
amount_before_gst = (coffee_price * coffee_qty) + (pastry_price * pastry_qty)

# Calculate GST amount
gst_amount = amount_before_gst * gst_rate

# Calculate total amount after GST
total_amount = amount_before_gst + gst_amount

# Display the bill
print("------ Coffee Shop Bill ------")
print(f"Amount Before GST: ₹{amount_before_gst:.2f}")
print(f"GST @%: ₹{gst_amount:.2f}")
print(f"Total Amount: ₹{total_amount:.2f}")
