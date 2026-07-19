# 6. E-commerce Discount and Shipping Engine
# Input:
# •	cart value
# •	customer type
# •	coupon code
# •	membership status
# Rules:
# •	Premium members get free shipping
# •	Cart above ₹5000 gets 20% discount
# •	Cart above ₹2000 gets 10% discount
# •	Coupon applies only if valid
# •	Final payable amount should be displayed

cart_value = float(input("Enter Cart Value (₹): "))
customer_type = input("Enter Customer Type (Regular/Premium): ").lower()
coupon = input("Enter Coupon Code: ").upper()
membership = input("Enter Membership Status (yes/no): ").lower()

# Discount Calculation
if cart_value > 5000:
    discount = cart_value * 0.20
elif cart_value > 2000:
    discount = cart_value * 0.10
else:
    discount = 0

# Coupon Discount
if coupon == "SAVE100":
    coupon_discount = 100
elif coupon == "SAVE200":
    coupon_discount = 200
else:
    coupon_discount = 0

# Shipping Charges
if membership == "yes" or customer_type == "premium":
    shipping = 0
else:
    shipping = 100

# Final Amount
final_amount = cart_value - discount - coupon_discount + shipping

if final_amount < 0:
    final_amount = 0

print("\n----- Bill Summary -----")
print("Cart Value          : ₹", cart_value)
print("Discount            : ₹", discount)
print("Coupon Discount     : ₹", coupon_discount)
print("Shipping Charges    : ₹", shipping)
print("-------------------------------")
print("Final Payable Amount: ₹", final_amount)