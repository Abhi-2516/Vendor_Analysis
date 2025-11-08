import streamlit as st
import pandas as pd
import sqlite3
import seaborn as sns
import matplotlib.pyplot as plt
import warnings

# --- Page Configuration ---
# Set the page title, icon, and layout
st.set_page_config(
    page_title="Vendor Performance Analysis",
    page_icon="📦",
    layout="wide"
)

# --- Data Loading ---
# Use st.cache_data to load the data only once
@st.cache_data
def load_data():
    warnings.filterwarnings('ignore')
    # Connect to the database
    conn = sqlite3.connect('inventory.db')
    # [cite_start]Load the main analysis table created by the script [cite: 539-540]
    df = pd.read_sql_query("SELECT * FROM vendor_sales_summary", conn)
    conn.close()
    
    # Data cleaning and feature engineering
    # This is from our 'my_new_analysis.ipynb' notebook
    analysis_df = df[
        (df['ProfitMargin'] > 0) & (df['ProfitMargin'] < 100) &
        (df['FreightCost'] > 0) & (df['TotalPurchaseDollars'] > 0)
    ].copy()
    analysis_df['FreightCost_Percent'] = (analysis_df['FreightCost'] / analysis_df['TotalPurchaseDollars']) * 100
    # Filter out extreme outliers for cleaner charts
    analysis_df = analysis_df[analysis_df['FreightCost_Percent'] < 25]
    
    return df, analysis_df

# Load the data
df, analysis_df = load_data()


# --- Title and Introduction ---
st.title("📦 Vendor Performance Analysis")
st.write("""
This interactive dashboard analyzes vendor profitability and efficiency. 
It is based on the project by Ayushi Mishra and has been extended with new analysis.
""")

# --- KPI Metrics from the Report ---
st.header("Overall Performance Snapshot")
kpi1, kpi2, kpi3, kpi4 = st.columns(4)

# Calculate KPIs from the original, unfiltered dataframe
total_sales = df['TotalSalesDollars'].sum()
total_purchase = df['TotalPurchaseDollars'].sum()
gross_profit = df['GrossProfit'].sum()
unsold_capital = (df['TotalPurchaseQuantity'] - df['TotalSalesQuantity']) * df['PurchasePrice']
unsold_capital = unsold_capital[unsold_capital > 0].sum()

kpi1.metric(label="Total Sales", value=f"${total_sales/1_000_000:.2f}M")
kpi2.metric(label="Total Purchase", value=f"${total_purchase/1_000_000:.2f}M")
kpi3.metric(label="Gross Profit", value=f"${gross_profit/1_000_000:.2f}M")
kpi4.metric(label="Unsold Capital", value=f"${unsold_capital/1_000_000:.2f}M")

st.markdown("---")

# --- New Analysis: Freight Cost ---
st.header("New Analysis: How Freight Costs Impact Profitability")
st.write("This analysis shows the relationship between a vendor's freight costs (as a percentage of their purchase cost) and their final profit margin.")

# Create two columns for the chart and the vendor table
col1, col2 = st.columns([2, 1]) # Make the chart column 2x wider

with col1:
    st.subheader("Profit Margin vs. Freight Cost %")
    
    # Create the chart
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(
        data=analysis_df,
        x='FreightCost_Percent',
        y='ProfitMargin',
        alpha=0.4,
        s=50,
        ax=ax
    )
    # Add the trendline
    sns.regplot(
        data=analysis_df,
        x='FreightCost_Percent',
        y='ProfitMargin',
        scatter=False, # Don't re-plot the scatter
        color='red',
        line_kws={'linestyle':'--'},
        ax=ax
    )
    ax.set_title('Profit Margin vs. Freight Cost as % of Purchase')
    ax.set_xlabel('Freight Cost (% of Purchase)')
    ax.set_ylabel('Profit Margin (%)')
    st.pyplot(fig)

with col2:
    st.subheader("Vendors Most Affected by Freight")
    st.write("These vendors have the highest average freight cost percentage.")
    
    # Get the top vendors table (from our notebook)
    vendor_freight = analysis_df.groupby('VendorName')[['FreightCost_Percent', 'ProfitMargin']].mean().reset_index()
    vendors_high_freight = vendor_freight.sort_values(by='FreightCost_Percent', ascending=False)
    
    # Display the table in Streamlit
    st.dataframe(
        vendors_high_freight.head(10),
        column_config={
            "VendorName": "Vendor",
            "FreightCost_Percent": st.column_config.ProgressColumn(
                "Freight %",
                format="%.2f%%",
                min_val=0,
                max_val=float(vendors_high_freight['FreightCost_Percent'].max())
            ),
            "ProfitMargin": st.column_config.ProgressColumn(
                "Avg. Profit %",
                format="%.2f%%",
                min_val=0,
                max_val=100
            )
        },
        hide_index=True
    )

# --- Add a way to see the original data ---
st.markdown("---")
if st.checkbox("Show Full Analysis Data"):
    st.subheader("Filtered Analysis Data")
    st.dataframe(analysis_df)