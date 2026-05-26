<div align="center">

# 📊 Superstore Sales & Profit Dashboard

**End‑to‑End Business Intelligence | Power BI + Python**

[![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-4c72b0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](LICENSE)

**Interactive dashboard + automated statistical analysis**  
*Uncover profit drivers, discount pitfalls, and regional performance*

</div>

---

## 📸 Dashboard Preview

| Executive Overview | Regional & Segment Analysis | Product Performance |
|:---:|:---:|:---:|
| <img src="documentation/images/executive_overview.jpeg" width="300"/> | <img src="documentation/images/regional_&_segment_analysis.jpeg" width="300"/> | <img src="documentation/images/product_performance.jpeg" width="300"/> |

*Three of four dashboard pages – see full interactive experience in Power BI.*

---

## 🎯 Key Features

- ✅ **Interactive Power BI Dashboard** – 4 connected pages with drill‑through and filters
- ✅ **Automated Python EDA** – One‑click script generates summary stats, charts, and CSVs
- ✅ **Profit & Discount Deep Dive** – Identifies loss‑making products and optimal discount thresholds
- ✅ **Regional Profitability Matrix** – Visual heatmap of sales vs. profit by region
- ✅ **Actionable Insights** – Direct business recommendations (e.g., stop discounting Tables over 30%)

---

## 📂 Project Structure
Superstore_Dashboard/
├── data/
│ └── SampleSuperstore.csv # Raw dataset (999 rows, 21 columns)
├── powerbi/
│ └── Sample_Superstore_Dashboard.pbix # Main Power BI file
├── python_analysis/
│ ├── superstore_report.py # Full EDA script
│ ├── requirements.txt # Dependencies (pandas, matplotlib, seaborn)
│ └── outputs/ # Auto‑generated charts & CSVs
│ ├── profit_by_region.png
│ ├── profit_by_subcategory.png
│ ├── discount_vs_profit.png
│ └── ... (plus CSV exports)
├── documentation/
│ ├── Superstore_Dashboard_Report.md # Detailed business report
│ └── images/ # Screenshots for README
├── .gitignore
└── README.md

---

## 🚀 Getting Started

### Prerequisites

| Tool | Version | Download |
|------|---------|----------|
| Power BI Desktop | Free | [Download](https://powerbi.microsoft.com/en-us/desktop/) |
| Python | 3.8+ | [python.org](https://python.org) |
| Git | optional | [git-scm.com](https://git-scm.com/) |

### 1️⃣ Clone the repository

- ```bash
git clone https://github.com/krishnaaidev/superstore-powerbi-dashboard.git
cd superstore-powerbi-dashboard

### 2️⃣ Explore the Power BI dashboard

Open powerbi/Sample_Superstore_Dashboard.pbix in Power BI Desktop.

<details> <summary>📄 Dashboard pages (click to expand)</summary>
Page Name	What you’ll see
Executive Overview	Top KPIs, profit map of US regions, sales vs. profit scatter
Regional & Segment Analysis	Profit matrix by region/segment, bottom 5 products, category treemap
Product & Discount Performance	Discount% vs. Profit% scatter, sub‑category bar chart, discount slicer
Discount Deep Dive	Drill‑through page with profit distribution box plots and discount bins
</details>

### 3️⃣ Run the Python analysis

bash
cd python_analysis
pip install -r requirements.txt
python superstore_report.py
What the script does automatically:

Prints KPIs (total sales, profit, avg discount, etc.)
Saves publication‑ready charts to outputs/ (PNG format)
Exports profit_by_region.csv and profit_by_subcategory.csv
All outputs are version‑controlled ready for reporting.

### 🔍 Key Business Insights

Insight	Implication
Technology category contributes 48% of total profit, with Copiers at 81% margin	Invest more in tech marketing and inventory
Tables and Bookcases lose money even at moderate discounts	Reconsider discount strategy or discontinue low‑margin variants
West region > highest sales but South region lowest profit due to deep furniture discounts	Regional discount caps or targeted promotions
Discounts >50% → 95% of transactions yield negative profit	Implement a hard discount ceiling (e.g., 40% max)
Consumer segment high volume, but Corporate has better profit per order	Tailor loyalty programs for corporate clients

### 🛠️ Built With

<div align="center">
Category	Technologies
Dashboard & Modelling	https://img.shields.io/badge/Power%2520BI-F2C811?style=flat-square&logo=powerbi&logoColor=black

Data Analysis	https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white

Visualisation	https://img.shields.io/badge/Matplotlib-11557c?style=flat-square&logo=python&logoColor=white https://img.shields.io/badge/Seaborn-4c72b0?style=flat-square&logo=python&logoColor=white

Version Control	https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white
</div>

### 📫 Contact & Contributing

Project Maintainer: Suman Krishna
📧 krishnasuman@myyahoo.com
🔗 GitHub Repository - [https://github.com/krishnaaidev/superstore-powerbi-dashboard]

Issues and pull requests are welcome. For major changes, please open a discussion first.

### 🙏 Acknowledgements

Data source: Sample Superstore dataset (publicly available via Tableau Community)
Inspiration: Power BI community DAX patterns and real‑world retail analytics
Libraries: Pandas, Matplotlib, Seaborn – open‑source heroes