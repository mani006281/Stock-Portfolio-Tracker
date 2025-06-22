# Predefined stock prices using a dictionary
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2800,
    "MSFT": 350,
    "AMZN": 3300
}

# Empty dictionary to store user input
portfolio = {}

# Input number of stocks
n = int(input("Enter the number of different stocks you own: "))

# Taking stock name and quantity from user
for _ in range(n):
    stock = input("Enter stock symbol (e.g., AAPL): ").upper()
    quantity = int(input(f"Enter quantity of {stock}: "))
    
    if stock in stock_prices:
        portfolio[stock] = quantity
    else:
        print(f"⚠️ Warning: {stock} is not in the stock price list. Skipping.")

# Calculate total investment
total_investment = 0
print("\n📊 Investment Breakdown:")
for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares x ${price} = ${value}")

print(f"\n💰 Total Investment Value: ${total_investment}")

# Save to file (optional)
save = input("Do you want to save the result to a file? (yes/no): ").lower()
if save == "yes":
    with open("portfolio_summary.txt", "w") as f:
        f.write("Stock Portfolio Summary\n")
        for stock, qty in portfolio.items():
            f.write(f"{stock}: {qty} shares x ${stock_prices[stock]} = ${stock_prices[stock] * qty}\n")
        f.write(f"\nTotal Investment Value: ${total_investment}")
    print("📁 Saved to 'portfolio_summary.txt'")
