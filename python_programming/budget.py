class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # 30-character title line centered with '*'
        title = self.name.center(30, "*")
        lines = [title]

        # Ledger entries
        for item in self.ledger:
            desc = item["description"][:23].ljust(23)
            amt = f"{item['amount']:.2f}".rjust(7)
            lines.append(f"{desc}{amt}")

        # Total line
        total = f"Total: {self.get_balance():.2f}"
        lines.append(total)

        return "\n".join(lines)


def create_spend_chart(categories):
    # Calculate spending (withdrawals only) for each category
    spent_per_category = []
    for cat in categories:
        spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0)
        spent_per_category.append(spent)

    total_spent = sum(spent_per_category)

    # Calculate percentages rounded down to nearest 10
    if total_spent == 0:
        percentages = [0] * len(categories)
    else:
        percentages = [int((spent / total_spent) * 100) // 10 * 10 for spent in spent_per_category]

    chart = "Percentage spent by category\n"

    # Y-axis rows from 100 down to 0
    for level in range(100, -1, -10):
        row = f"{level:>3}| "
        for pct in percentages:
            row += "o  " if pct >= level else "   "
        chart += row + "\n"

    # Horizontal line below the bars
    dashes = "-" * (len(categories) * 3 + 1)
    chart += "    " + dashes + "\n"

    # Vertical category names
    max_len = max(len(cat.name) for cat in categories)
    name_rows = []

    for i in range(max_len):
        row = "     "
        for cat in categories:
            char = cat.name[i] if i < len(cat.name) else " "
            row += f"{char}  "
        name_rows.append(row)

    chart += "\n".join(name_rows)

    return chart