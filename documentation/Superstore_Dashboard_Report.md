# Superstore Sales & Profit Dashboard – Power BI Report

## 1. Introduction

This report documents the **Power BI dashboard** built on the *Sample Superstore* dataset. The dashboard provides an interactive view of sales, profit, discounts, and product performance across different regions, customer segments, and product categories. It is intended for business users who need to quickly identify profit drivers and problem areas.

---

## 2. Dataset Overview

The dataset (`SampleSuperstore.csv`) contains **9,994 rows** of simulated sales transactions from a global office supply retailer. Key columns include:

| Column Name | Description |
|-------------|-------------|
| `Ship Mode` | Shipping class (First Class, Second Class, Standard Class, Same Day) |
| `Segment` | Customer segment (Consumer, Corporate, Home Office) |
| `Country`, `State`, `City`, `Postal Code` | Geographic details |
| `Region` | Four US regions: Central, East, South, West |
| `Category` | Product category (Furniture, Office Supplies, Technology) |
| `Sub‑Category` | Detailed product type (e.g., Chairs, Phones, Tables) |
| `Sales` | Total sales amount (USD) |
| `Quantity` | Number of units sold |
| `Discount` | Discount applied (0 to 0.8) |
| `Profit` | Profit (positive or negative) |

**Calculated measures** added in Power BI:
- `Profit Ratio` = `Profit / Sales`
- `Discount Band` = groups discount levels (No Discount, Low, Medium, High)

---

## 3. Dashboard Pages & KPIs

The dashboard consists of **four pages**, each focusing on a different analytical angle.

### Page 1: Executive Overview
- **KPIs** (cards): Total Sales, Total Profit, Total Quantity, Average Discount, Profit Ratio
- **Map**: Profit by State (red for loss, green for profit)
- **Bar chart**: Sales and Profit by Region
- **Scatter plot**: Sales vs. Profit by Sub‑Category (highlights “Copiers” as high‑profit, “Tables” as high‑loss)

### Page 2: Regional & Segment Analysis
- **Matrix**: Profit by Region and Segment
- **Donut chart**: Profit share by Category
- **Bar chart**: Bottom 5 Sub‑Categories by Profit (loss leaders)
- **Slicers**: Region, Segment, Category

### Page 3: Product Performance & Discount Impact
- **Column & line chart**: Sales (columns) and Profit Ratio (line) by Sub‑Category
- **Scatter plot**: Average Discount vs. Profit Ratio (shows that discounts above 40% destroy profit)
- **Table**: Top 10 most unprofitable orders (Sales, Discount, Profit)

### Page 4: Discount Deep Dive (Drill‑through)
- **Box plot**: Profit distribution per Discount Band
- **Line chart**: Profit vs. Discount (binned)
- **Details** of any selected product/state (drill‑through from other pages)

---

## 4. Key Insights (Examples)

From the dashboard you will observe:

- **Technology** is the most profitable category (Copiers and Phones drive high margins).
- **Tables** and **Bookcases** are consistently loss‑making, especially when discounts exceed 30%.
- **West region** has the highest sales, but **South** shows the lowest profit due to deep discounts on Furniture.
- **Consumer segment** orders more frequently, but **Corporate** orders have better profit ratios.
- **Discounts above 50%** lead to negative profit in 95% of transactions.

---

## 5. Screenshots of the Dashboard

Below are the actual screenshots taken from the Power BI report.  
*(Replace the file paths with your own image locations.)*

### 5.1 Executive Overview Page
![Executive Overview](images/executive_overview.jpeg)

### 5.2 Regional & Segment Analysis
![Regional Segment](images/regional_&_segment_analysis.jpeg)

### 5.3 Product Performance
![Product Discount](images/product_performance.jpeg)


**How to take screenshots in Power BI Desktop:**
1. Open each dashboard page.
2. Use `Ctrl + Shift + S` (or go to *File > Export > Screenshot*).
3. Save as PNG in the `images/` folder relative to this report.
4. Adjust the markdown image paths accordingly.

---

## 6. Power BI File (.pbix) Technical Details

| Property | Value |
|----------|-------|
| File Name | `Sample_Superstore_Dashboard.pbix` |
| Power BI Version | May 2025 or later |
| Data Source | CSV (local file) |
| Data Refresh | Manual (or scheduled via OneDrive if uploaded) |
| Row Count | 9,994 |
| Measures created | 5 (Total Sales, Total Profit, Total Quantity, Avg Discount, Profit Ratio) |
| Calculated columns | 2 (Profit Ratio, Discount Band) |
| Pages | 4 |

---

## 7. How to Use This Report

1. Open the `.pbix` file in Power BI Desktop.
2. Interact with slicers and visuals to explore different regions, segments, and discount levels.
3. Use the drill‑through page by right‑clicking on a state or sub‑category → *Drill through > Discount Deep Dive*.
4. Export any visual as an image or PDF for presentations.

---

## 8. Conclusion

The Superstore Sales & Profit Dashboard enables quick identification of profitable products and regions, while highlighting the negative impact of excessive discounts. It serves as a practical tool for inventory and pricing decisions.

---

*Report generated on: May 26, 2026*
*Report generated by: Suman Krishna*
*Dashboard created using Power BI Desktop*