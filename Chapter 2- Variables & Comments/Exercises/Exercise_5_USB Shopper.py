## Solutions for Chapter 2: Variables & Comments

# Exercise 5: USB Shopper
# Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.

budget = 50
usb_stick = 6
print("\nBudget: £50\nCost for each USB stick: £6\n------------")

total_usb = 50 // 6
msg1 = f"\nShe can buy {total_usb} USB sticks with £50.\n"
print(msg1)

total_amount = total_usb * 6
msg2 = f"Total amount to be paid: £{total_amount}.\n"
print(msg2)

change = 50 - total_amount
msg3 = f"She will have £{change} left.\n"
print(msg3)