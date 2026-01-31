import numpy as np

sales = np.random.randint(300, 700, size=(7, 7))
print("Sales Data (7 Days × 7 Products):\n", sales)

print("\nTotal sales of each product:")
print(sales.sum(axis=0))

print("\nAverage sales per day:")
print(sales.mean(axis=1))

highest_product = sales.sum(axis=0).max()
print("\nHighest selling product total:", highest_product)

print("\nSales after 10% increase:")
print(sales * 1.10)

print("\nSales data of first 3 days:")
print(sales[0:3, :])

daily_sales = sales.sum(axis=1)
average_sales = daily_sales.mean()

print("\nDays with sales above average:")
for day, value in enumerate(daily_sales):
    if value > average_sales:
        print(f"Day {day+1}: {value}")

week2 = np.random.randint(300, 700, size=(7, 7))
combined_sales = np.vstack((sales, week2))

print("\nCombined Sales Data Shape:", combined_sales.shape)

week1, week2_split = np.split(combined_sales, 2)

threshold = 600
count = 0

for value in np.nditer(sales):
    if value > threshold:
        count += 1

print("\nValues above threshold:", count)

sales_int16 = sales.astype(np.int16)
print("\nChanged dtype:", sales_int16.dtype)