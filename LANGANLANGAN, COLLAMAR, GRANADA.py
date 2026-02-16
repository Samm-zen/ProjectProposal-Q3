def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def add_expense(expenses, total_spent):
    print("\n--- Add an Expense ---")
    name = input("Expense name: ")
    category = input("Category (Food/Transport/School/Others): ")
    price = get_float_input("Price: ₱")

    expenses.append({
        "name": name,
        "category": category,
        "price": price
    })

    total_spent += price
    return total_spent


def show_summary(expenses, bank_balance, total_spent, savings_goal):
    remaining = bank_balance - total_spent

    print("\n============================")
    print("          SUMMARY")
    print("============================")

    for idx, expense in enumerate(expenses, start=1):
        print(f"{idx}. {expense['name']} "
              f"({expense['category']}) - ₱{expense['price']}")

    print("----------------------------")
    print(f"Total spent: ₱{total_spent}")
    print(f"Remaining balance: ₱{remaining}")
    print("----------------------------")

    if savings_goal:
        print(f"Savings Goal: ₱{savings_goal}")
        if remaining >= savings_goal:
            print("You reached your savings goal!")
        else:
            print("You have not yet reached your savings goal.")

    if remaining < 0:
        print("You are in debt. Reduce expenses.")
    elif remaining <= 100:
        print("Balance is very low.")
    else:
        print("Spending is manageable.")


def main():
    while True:
        expenses = []
        total_spent = 0

        print("\n====== Expense Tracker ======")
        bank_balance = get_float_input("Enter your total bank balance: ₱")
        savings_goal = get_float_input("Enter your savings goal (₱0 if none): ")

        while True:
            total_spent = add_expense(expenses, total_spent)

            if total_spent > bank_balance:
                print("WARNING: You exceeded your balance!")
                break

            add_more = input("Add another expense? (yes/no): ").lower()
            if add_more != "yes":
                break

        show_summary(expenses, bank_balance, total_spent, savings_goal)

        restart = input("\nRestart program? (yes/no): ").lower()
        if restart != "yes":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
