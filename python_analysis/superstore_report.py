# superstore_report.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Set style for plots
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# -------------------------------
# 1. Load and inspect data
# -------------------------------
df = pd.read_csv('/Users/sumankrishna/Desktop/Suman Krishna/EduTech Solutions/Superstore_Dashboard/data/SampleSuperstore.csv')
print("=== SAMPLE SUPERSTORE REPORT ===\n")
print(f"Dataset shape: {df.shape}")
print(f"Columns: {list(df.columns)}\n")
print("First 5 rows:")
print(df.head(), "\n")

# -------------------------------
# 2. Basic statistics and KPIs
# -------------------------------
total_sales = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_quantity = df['Quantity'].sum()
avg_discount = df['Discount'].mean()
profit_margin = (total_profit / total_sales) * 100

print("=== KEY PERFORMANCE INDICATORS ===")
print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Profit: ${total_profit:,.2f}")
print(f"Profit Margin: {profit_margin:.2f}%")
print(f"Total Quantity Sold: {total_quantity:,}")
print(f"Average Discount: {avg_discount:.2%}\n")

# -------------------------------
# 3. Profit by Region
# -------------------------------
region_profit = df.groupby('Region')['Profit'].sum().sort_values(ascending=False)
print("=== PROFIT BY REGION ===")
print(region_profit.to_string())

plt.figure()
region_profit.plot(kind='bar', color=['green' if x>0 else 'red' for x in region_profit])
plt.title('Total Profit by Region')
plt.ylabel('Profit ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('profit_by_region.png')
plt.close()
print("Saved: profit_by_region.png\n")

# -------------------------------
# 4. Profit by Category and Sub-Category
# -------------------------------
cat_profit = df.groupby('Category')['Profit'].sum().sort_values(ascending=False)
print("=== PROFIT BY CATEGORY ===")
print(cat_profit.to_string())

subcat_profit = df.groupby('Sub-Category')['Profit'].sum().sort_values(ascending=False)
print("\n=== PROFIT BY SUB-CATEGORY (Top 5 & Bottom 5) ===")
print(subcat_profit.head(5))
print(subcat_profit.tail(5))

# Top 5 sub-categories
plt.figure()
subcat_profit.head(10).plot(kind='bar', color='skyblue')
plt.title('Top 10 Sub-Categories by Profit')
plt.ylabel('Profit ($)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('profit_by_subcategory_top10.png')
plt.close()

# Bottom 5 sub-categories (loss makers)
plt.figure()
subcat_profit.tail(5).plot(kind='bar', color='salmon')
plt.title('Bottom 5 Sub-Categories by Profit (Losses)')
plt.ylabel('Profit ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('loss_makers_subcategory.png')
plt.close()

# -------------------------------
# 5. Impact of Discount on Profit
# -------------------------------
# Create discount bins
df['Discount_Bin'] = pd.cut(df['Discount'], bins=[-0.001, 0, 0.2, 0.4, 0.6, 1.0], 
                             labels=['0%', '1-20%', '21-40%', '41-60%', '61-100%'])
discount_effect = df.groupby('Discount_Bin')['Profit'].mean()
print("\n=== AVERAGE PROFIT BY DISCOUNT LEVEL ===")
print(discount_effect.to_string())

plt.figure()
discount_effect.plot(kind='bar', color='teal')
plt.title('Average Order Profit vs Discount Level')
plt.xlabel('Discount Range')
plt.ylabel('Average Profit ($)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('profit_vs_discount.png')
plt.close()

# Scatter plot: Discount vs Profit (zoom to typical range)
plt.figure()
sns.scatterplot(data=df, x='Discount', y='Profit', alpha=0.3, color='purple')
plt.axhline(y=0, color='red', linestyle='--')
plt.title('Discount vs Profit per Order')
plt.xlabel('Discount')
plt.ylabel('Profit ($)')
plt.tight_layout()
plt.savefig('discount_profit_scatter.png')
plt.close()

# -------------------------------
# 6. Worst performing products (lowest profit)
# -------------------------------
# Group by Sub-Category and Region to find problem areas
worst_combos = df.groupby(['Region', 'Sub-Category'])['Profit'].sum().reset_index()
worst_combos = worst_combos[worst_combos['Profit'] < 0].sort_values('Profit').head(10)
print("\n=== TOP 10 LOSS-MAKING (REGION, SUB-CATEGORY) COMBINATIONS ===")
print(worst_combos.to_string(index=False))

# -------------------------------
# 7. Segment analysis
# -------------------------------
segment_profit = df.groupby('Segment')['Profit'].sum().sort_values(ascending=False)
print("\n=== PROFIT BY CUSTOMER SEGMENT ===")
print(segment_profit.to_string())

# -------------------------------
# 8. Export summary tables to CSV
# -------------------------------
summary = {
    'Metric': ['Total Sales', 'Total Profit', 'Profit Margin (%)', 'Total Quantity', 'Avg Discount'],
    'Value': [total_sales, total_profit, profit_margin, total_quantity, avg_discount]
}
summary_df = pd.DataFrame(summary)
summary_df.to_csv('kpi_summary.csv', index=False)

region_profit.to_csv('profit_by_region.csv', header=True)
subcat_profit.to_csv('profit_by_subcategory.csv', header=True)

print("\n=== REPORT GENERATION COMPLETE ===")
print("Files created:")
print(" - profit_by_region.png")
print(" - profit_by_subcategory_top10.png")
print(" - loss_makers_subcategory.png")
print(" - profit_vs_discount.png")
print(" - discount_profit_scatter.png")
print(" - kpi_summary.csv")
print(" - profit_by_region.csv")
print(" - profit_by_subcategory.csv")