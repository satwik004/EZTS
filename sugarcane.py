def calculate_profit(N, price_per_glass):
    total_income = N * price_per_glass
    
    sugarcane_cost = 0.20 * total_income
    salt_and_mint_cost = 0.20 * total_income
    rent_cost = 0.30 * total_income
    
    total_expenses = sugarcane_cost + salt_and_mint_cost + rent_cost
    
    profit = total_income - total_expenses
    return profit

# Input number of test cases
T = int(input("Enter the number of test cases: "))

# Iterate through each test case
for _ in range(T):
    # Input the number of glasses sold for each test case
    N = int(input())
    price_per_glass = 50  # Price per glass in coins
    profit = calculate_profit(N, price_per_glass)
print(profit)
