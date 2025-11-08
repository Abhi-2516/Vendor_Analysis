Vendor Performance Analysis – Retail Inventory & Sales
Analyzing vendor efficiency and profitability to support strategic purchasing and inventory decisions using SQL, Python, Streamlit, and Power BI.

📌 Table of Contents
<a href="#overview">Overview</a>

<a href="#live-dashboard">Live Interactive Dashboard</a>

<a href="#business-problem">Business Problem</a>

<a href="#tools--technologies">Tools & Technologies</a>

<a href="#project-structure">Project Structure</a>

<a href="#research-questions--key-findings">Research Questions & Key Findings</a>

<a href="#how-to-run-this-project">How to Run This Project</a>

<a href="#final-recommendations">Final Recommendations</a>

<a href="#acknowledgements">Acknowledgements</a>

<a href="#author--contact">Author & Contact</a>

<h2><a class="anchor" id="overview"></a>Overview</h2>

This project evaluates vendor performance and retail inventory dynamics to drive strategic insights for purchasing, pricing, and inventory optimization. A complete data pipeline was built using SQL for ETL and Python (Pandas, Seaborn, SciPy) for analysis and hypothesis testing.

The final findings are presented in an interactive web application built with Streamlit, which includes the original project's key findings and new analysis on freight cost impact.



<h2><a class="anchor" id="business-problem"></a>Business Problem</h2>

Effective inventory and sales management are critical in the retail sector. This project aims to:

Identify underperforming brands needing pricing or promotional adjustments

Determine vendor contributions to sales and profits

Analyze the cost-benefit of bulk purchasing

Investigate inventory turnover inefficiencies

Statistically validate differences in vendor profitability

<h2><a class="anchor" id="tools--technologies"></a>Tools & Technologies</h2>

Data Analysis: Python (Pandas, Matplotlib, Seaborn, SciPy)

Database: SQL (Common Table Expressions, Joins) & SQLite

Interactive App: Streamlit

BI Dashboarding: Power BI

Version Control: GitHub

<h2><a class="anchor" id="project-structure"></a>Project Structure</h2>

vendor-performance-analysis/
│
├── README.md
├── app.py                      # The Streamlit web application
├── requirements.txt            # Python libraries for the app
├── inventory.db                # The SQLite database with all processed data
├── Vendor Performance Report.pdf # Updated report with new findings
│
├── notebooks/                  # Jupyter notebooks for analysis
│   ├── exploratory_data_analysis.ipynb
│   ├── vendor_performance_analysis.ipynb
│   
│
├── scripts/                    # Original Python scripts for ETL
│   ├── ingestion_db.py
│   └── get_vendor_summary.py
│
├── dashboard/                  # Power BI dashboard file
│   └── vendor_performance_dashboard.pbix
<h2><a class="anchor" id="research-questions--key-findings"></a>Research Questions & Key Findings</h2>


Brands for Promotions: 198 brands were identified with low sales but high profit margins, making them prime targets for promotional adjustments .


Top Vendors: The top 10 vendors account for 65.69% of total purchases, indicating a significant risk of over-reliance .


Bulk Purchasing Impact: Large orders receive an average 72% cost savings per unit compared to small orders .


Inventory Turnover: A total of $2.71M in capital is locked in unsold inventory, highlighting inefficiencies in stock management.


Vendor Profitability: Low-performing vendors have a statistically higher mean profit margin (41.55%) than top-performing vendors (31.17%), suggesting they operate on different business models .


Hypothesis Testing: A T-test confirmed a statistically significant difference (p < 0.05) in profit margins between high and low-performing vendors .

New Finding - Freight Cost Impact: My analysis shows a clear negative correlation between freight costs (as a % of purchase) and profit margins, highlighting logistical efficiency as a key profitability driver.

<h2><a class="anchor" id="how-to-run-this-project"></a>How to Run This Project</h2>


Clone the repository:

Bash

git clone https://github.com/your-username/vendor-performance-analysis.git
cd vendor-performance-analysis
Install the required libraries:

Bash

pip install -r requirements.txt
Run the Streamlit app:

Bash

streamlit run app.py
Your browser will automatically open with the interactive dashboard.

2. (Optional) Run the Original Analysis
If you want to explore the original Jupyter notebooks or Power BI file:

Jupyter: Run jupyter notebook from your terminal and open any file in the notebooks/ folder.

Power BI: Open the dashboard/vendor_performance_dashboard.pbix file in Power BI Desktop.

<h2><a class="anchor" id="final-recommendations"></a>Final Recommendations</h2>


Diversify vendor base to reduce dependency risk on the top 10 suppliers.


Optimize bulk order strategies to leverage the 72% cost savings.


Reprice slow-moving, high-margin brands to increase sales volume.


Launch clearance sales or revise storage strategies to clear the $2.71M in unsold inventory.


Improve marketing for low-performing vendors to boost their sales volume.

<h2><a class="anchor" id="acknowledgements"></a>Acknowledgements</h2>

This project is an extension of the original "Vendor Performance Analysis" project by Ayushi Mishra . I have built upon the original analysis by adding new insights on freight cost impact and deploying the findings in a new, interactive Streamlit web application.

You can find the original author's portfolio here:


LinkedIn 


Portfolio 

<h2><a class="anchor" id="author--contact"></a>Author & Contact</h2>

[Abhishek Yadav]

Data Analyst
