bank_balance = float(input("Enter your total bank balance: ₱"))

expenses = []
total_spent = 0

while True:
    print("\n--- Add an Expense ---")
    name = input("Expense name: ")
    price = float(input("Price: ₱"))

    expenses.append((name, price))
    total_spent += price

    print(f"Added: {name} - ₱{price}")
    print(f"Current total spent: ₱{total_spent}")
    print(f"Remaining balance: ₱{bank_balance - total_spent}")

    # Check if total exceeds balance
    if total_spent > bank_balance:
        print("\n⚠ WARNING: You have exceeded your bank balance!")
        break

    # Ask if add more expenses
    add_more = input("\nAdd another expense? (yes/no): ").lower()
    if add_more != "yes":
        break

# Final remaining balance
remaining = bank_balance - total_spent

print("\n============================")
print("       SUMMARY")
print("============================")
for idx, (name, price) in enumerate(expenses, start=1):
    print(f"{idx}. {name} - ₱{price}")

print("----------------------------")
print(f"Total spent: ₱{total_spent}")
print(f"Remaining balance: ₱{remaining}")
print("----------------------------")

# Advice
if total_spent > bank_balance:
    print("⚠ You spent more than what you have. Be careful next time!")

elif 0 <= remaining <= 100:
    print("💡 Advice: Your balance is very low. Try to avoid spending for now.")

elif remaining < 0:
    print("⚠ You are in debt now. You need to reduce expenses.")

else:
    print("👍 Your spending looks manageable.")

# Next choice
print("\nWhat would you like to do next?")
print("[1] Restart")
print("[2] Exit")

choice = input("Choose: ")

if choice == "1":
    print("\n🔄 Restart the program to begin again.")
else:
    print("\nGoodbye!")
