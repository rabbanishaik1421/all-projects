#Pivot table 
import pandas as pd

df = pd.DataFrame({
    'Region': ['East', 'East', 'West', 'West', 'North', 'North', 'South', 'South'],
    'Product': ['Laptop', 'Mobile', 'Laptop', 'Mobile', 'Laptop', 'Mobile', 'Laptop', 'Mobile'],
    'Salesperson': ['John', 'John', 'Mary', 'Mary', 'David', 'David', 'John', 'Mary'],
    'Sales': [50000, 30000, 45000, 25000, 60000, 35000, 55000, 40000],
    'Profit': [10000, 5000, 9000, 4000, 12000, 7000, 11000, 8000]
})

# 1. Find the total sales for each region
total_sales = pd.pivot_table(
    df,
    index='Region',
    values='Sales',
    aggfunc='sum'
)
print(total_sales)

#2. Find the average profit for each region.
avg_sales = pd.pivot_table(
    df,
    index='Region',
    values='Profit',
    aggfunc='mean'
)
print(avg_sales)

#3. Count the number of sales records in each region
sales_count = pd.pivot_table(
    df,
    index='Region',
    values='Sales',
    aggfunc='count'
)
print(sales_count)

#4. Find the maximum sales in each region.
max_sales = pd.pivot_table(
    df,
    index='Region',
    values='Sales',
    aggfunc='max'
) 
print(max_sales)

#5. Find the minimum profit in each region
min_profit = pd.pivot_table(
    df,
    index='Region',
    values='Profit',
    aggfunc='min'
) 
print("Min Profit")
print(min_profit)

#6. Create a pivot table showing
pivotTable = pd.pivot_table(
    df,
    index='Region',
    columns='Product',
    values='Sales',
    aggfunc='sum'
)
print("Pivot Table")
print(pivotTable)

#7. Create a pivot table showing the average sales by region and product
average_sales = pd.pivot_table(
    df,
    index='Region',
    columns='Product',
    values='Sales',
    aggfunc='mean'
) 
print("Average sales by Region and Product")
print(average_sales)

#8. Show the total profit by salesperson.
totalProfitBySalesPerson = pd.pivot_table(
    df,
    index='Salesperson',
    values='Profit',
    aggfunc='sum'    
)
print(totalProfitBySalesPerson)

#9. Display sales by salesperson and product
displaySalesperson = pd.pivot_table(
    df,
    index='Salesperson',
    columns='Product',
    values='Sales',
    aggfunc='sum'
)
print("#9. Display sales by salesperson and product")
print(displaySalesperson)

'''
10. Create a pivot table with:
Rows → Region
Columns → Product
Values → Profit
Fill missing values with 0
'''
fillMissingValues = pd.pivot_table(
    df,
    index='Region',
    columns='Product',
    values='Profit',
    fill_value=0
)
print(fillMissingValues)

#11. Display both Sales and Profit in the same pivot table.
displaySalesProfit = pd.pivot_table(
    df,
    index='Region',
    # columns='["Sales", "Profit"]',
    values=["Sales", "Profit"],
    aggfunc='sum'
) 
print('#11. Display both Sales and Profit in the same pivot table.')
print(displaySalesProfit)

# 12. Apply multiple aggregation functions (sum, mean, count) on the Sales column.
multipleSales = pd.pivot_table(
    df,
    index='Region',
    columns='Product',
    values='Sales',
    aggfunc=['sum', 'mean', 'count']
)
print(multipleSales)

# 13. Create a pivot table with:
'''Rows → Region, Salesperson
Columns → Product
Values → Sales'''
pivotTable4 = pd.pivot_table(
    df,
    index=['Region', 'Salesperson'],
    columns='Product',
    values='Sales'
)
print(pivotTable4)

# 14. Add row and column totals using the margins parameter.
result = pd.pivot_table(
    df,
    index="Region",
    columns="Product",
    values="Sales",
    aggfunc="sum",
    margins=True,
    margins_name="Total"
)
print(result)

# 15. Use a custom aggregation function to calculate the range of sales (max - min) for each region.
customAggregation = pd.pivot_table(
    df,
    index='Region',
    values='Sales',
    aggfunc=lambda x:x.max() - x.min()
)
print(customAggregation)

# 16. Create a pivot table showing:
'''Rows → Salesperson
Columns → Region
Values → Sales
Aggregation → Sum
'''
pivotTable5 = pd.pivot_table(
    df,
    index='Salesperson',
    columns='Region',
    values='Sales',
    aggfunc='sum'
)
print(pivotTable5)

# 17. Show the average profit by product and salesperson.
averageProfitByProdcutSalesperson = pd.pivot_table(
    df,
    index='Product',
    columns='Salesperson',
    values='Profit',
    aggfunc='mean'
)
print(averageProfitByProdcutSalesperson)

# 18. Create a pivot table using two value columns (Sales and Profit) with sum as the aggregation function.
pivotTable6 = pd.pivot_table(
    df,
    index="Region",
    values=["Sales","Profit"],
    aggfunc="sum"
)
print('#18 Create a pivot table using two value columns (Sales and Profit) with sum as the aggregation function.')
# print(pivotTable6)

# 19. Create a pivot table with:
'''Rows → Region
Columns → Product
Values → Sales
Aggregation → ['sum', 'mean', 'max']'''

pivotTable7 = pd.pivot_table(
    df,
    index='Region',
    columns='Product',
    values='Sales',
    aggfunc=['sum', 'mean', 'max']
)
print(pivotTable7)

# 20. Compare the output of:
df1 = df.groupby('Region')['Sales'].sum()

df2 = pd.pivot_table(
    df,
    values='Sales',
    index='Region',
    aggfunc='sum'
)

print(df1, df2)

print("="*50)
print("# dropna example")
print("="*50)
dropna_ex = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum",
    dropna=False
)
print(dropna_ex)

print("="*50)
print("# sort example")
print("="*50)
sort_ex = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum",
    sort=False
)
print(sort_ex)

print("="*50)
print("# observed example")
print("="*50)
sort_ex = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum",
    sort=False
)
print(sort_ex)

# observed = True
df["Product"] = pd.Categorical(
    df["Product"],
    categories=["Laptop", "Tablet"]
)

observed_ex = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Product",
    aggfunc="sum",
    observed=True,
)

print(observed_ex)