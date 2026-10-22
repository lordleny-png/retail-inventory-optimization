
import streamlit as st
import pandas as pd
import plotly.express as px

# --------------------------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------------------------
st.set_page_config(
    page_title="Retail Inventory Optimization",
    page_icon="📦",
    layout="wide"
)

# --------------------------------------------------
# 2. CUSTOM COLORS AND STYLING
# --------------------------------------------------
COLORS = {
    "blue": "#3498DB",
    "green": "#2ECC71",
    "orange": "#F39C12",
    "red": "#E74C3C",
    "purple": "#9B59B6"
}

st.title("📦 Retail Inventory Optimization")
st.caption(
    "Business Analytics Dashboard | Sales, Demand & Inventory Risk"
)

st.markdown("""
<style>
[data-testid="stMetric"] {
    background-color: rgba(52, 152, 219, 0.08);
    padding: 16px;
    border-radius: 12px;
    border: 1px solid rgba(52, 152, 219, 0.25);
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 3. LOAD DATA
# --------------------------------------------------
@st.cache_data
def load_data():
    data = pd.read_csv("retail_inventory.csv")
    data["Date"] = pd.to_datetime(data["Date"], errors="coerce")
    data["Estimated Revenue"] = data["Units Sold"] * data["Price"]

    data["Absolute Forecast Error"] = (
        data["Units Sold"] - data["Demand Forecast"]
    ).abs()

    valid_forecast = data["Demand Forecast"].where(
        data["Demand Forecast"] > 0
    )

    data["Stock Coverage Days"] = (
        data["Inventory Level"] / valid_forecast
    )

    data["Potential Stockout Risk"] = (
        data["Stock Coverage Days"] < 1
    )

    data["Potential Overstock"] = (
        data["Stock Coverage Days"] > 3
    )

    return data


try:
    df = load_data()
except Exception as e:
    st.error(
        "Could not load retail_inventory.csv. "
        "Make sure the CSV is uploaded beside app.py."
    )
    st.exception(e)
    st.stop()

# --------------------------------------------------
# 4. SIDEBAR FILTERS
# --------------------------------------------------
st.sidebar.header("🔎 Dashboard Filters")

categories = sorted(df["Category"].dropna().unique())
selected_categories = st.sidebar.multiselect(
    "Product Categories",
    categories,
    default=categories
)

stores = sorted(df["Store ID"].dropna().unique())
selected_stores = st.sidebar.multiselect(
    "Stores",
    stores,
    default=stores
)

min_date = df["Date"].min().date()
max_date = df["Date"].max().date()

date_range = st.sidebar.date_input(
    "Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)

filtered = df[
    df["Category"].isin(selected_categories)
    & df["Store ID"].isin(selected_stores)
].copy()

if len(date_range) == 2:
    start_date, end_date = date_range
    filtered = filtered[
        filtered["Date"].dt.date.between(start_date, end_date)
    ]

if filtered.empty:
    st.warning("No records match your selected filters.")
    st.stop()

# --------------------------------------------------
# 5. KPI CARDS
# --------------------------------------------------
total_units = filtered["Units Sold"].sum()
total_revenue = filtered["Estimated Revenue"].sum()
average_inventory = filtered["Inventory Level"].mean()
forecast_error = filtered["Absolute Forecast Error"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("📈 Units Sold", f"{total_units:,.0f}")
col2.metric("💰 Estimated Revenue", f"{total_revenue:,.2f}")
col3.metric("📦 Average Inventory", f"{average_inventory:,.1f}")
col4.metric("🎯 Mean Forecast Error", f"{forecast_error:,.2f}")

st.divider()

# --------------------------------------------------
# 6. INVENTORY RISK SUMMARY
# --------------------------------------------------
st.subheader("🚦 Inventory Risk Overview")

stockout_count = int(filtered["Potential Stockout Risk"].sum())
overstock_count = int(filtered["Potential Overstock"].sum())

risk_col1, risk_col2 = st.columns(2)

risk_col1.metric(
    "🔴 Potential Stockout Records",
    f"{stockout_count:,}"
)

risk_col2.metric(
    "🟠 Potential Overstock Records",
    f"{overstock_count:,}"
)

st.caption(
    "Preliminary screening only: stockout risk means less than "
    "one day of forecast demand; potential overstock means more "
    "than three days. These are illustrative thresholds."
)

# --------------------------------------------------
# 7. CATEGORY PERFORMANCE
# --------------------------------------------------
st.subheader("📊 Performance by Category")

category_data = (
    filtered.groupby("Category", as_index=False)
    .agg(
        Units_Sold=("Units Sold", "sum"),
        Estimated_Revenue=("Estimated Revenue", "sum"),
        Average_Inventory=("Inventory Level", "mean")
    )
)

left, right = st.columns(2)

with left:
    fig_revenue = px.bar(
        category_data.sort_values("Estimated_Revenue"),
        x="Estimated_Revenue",
        y="Category",
        orientation="h",
        color="Category",
        title="Estimated Revenue by Category",
        color_discrete_sequence=px.colors.qualitative.Bold
    )
    st.plotly_chart(fig_revenue, use_container_width=True)

with right:
    fig_units = px.pie(
        category_data,
        names="Category",
        values="Units_Sold",
        title="Share of Units Sold",
        color_discrete_sequence=px.colors.qualitative.Set2,
        hole=0.4
    )
    st.plotly_chart(fig_units, use_container_width=True)

# --------------------------------------------------
# 8. TOP 10 PRODUCTS
# --------------------------------------------------
st.subheader("🏆 Top 10 Products by Estimated Revenue")

product_data = (
    filtered.groupby("Product ID", as_index=False)
    .agg(
        Units_Sold=("Units Sold", "sum"),
        Estimated_Revenue=("Estimated Revenue", "sum"),
        Average_Inventory=("Inventory Level", "mean")
    )
    .sort_values("Estimated_Revenue", ascending=False)
    .head(10)
    .sort_values("Estimated_Revenue")
)

fig_products = px.bar(
    product_data,
    x="Estimated_Revenue",
    y="Product ID",
    orientation="h",
    color="Estimated_Revenue",
    color_continuous_scale="Viridis",
    title="Top 10 Products by Estimated Revenue",
    hover_data=["Units_Sold", "Average_Inventory"]
)

st.plotly_chart(fig_products, use_container_width=True)

# --------------------------------------------------
# 9. INVENTORY COVERAGE
# --------------------------------------------------
st.subheader("📦 Average Stock Coverage by Category")

coverage_data = (
    filtered.groupby("Category", as_index=False)
    ["Stock Coverage Days"]
    .mean()
    .dropna()
)

fig_coverage = px.bar(
    coverage_data,
    x="Category",
    y="Stock Coverage Days",
    color="Stock Coverage Days",
    color_continuous_scale="RdYlGn",
    title="Average Stock Coverage (Days)"
)

st.plotly_chart(fig_coverage, use_container_width=True)

# --------------------------------------------------
# 10. DETAILED DATA TABLE
# --------------------------------------------------
st.subheader("🔍 Inventory Records")

st.dataframe(
    filtered[
        [
            "Date", "Store ID", "Product ID", "Category",
            "Inventory Level", "Units Sold", "Demand Forecast",
            "Stock Coverage Days", "Estimated Revenue"
        ]
    ].sort_values("Date", ascending=False),
    use_container_width=True,
    hide_index=True
)

# --------------------------------------------------
# 11. DOWNLOAD FILTERED REPORT
# --------------------------------------------------
csv_data = filtered.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Filtered Inventory Report",
    data=csv_data,
    file_name="retail_inventory_report.csv",
    mime="text/csv"
)

st.divider()
st.caption(
    "Retail Inventory Optimization | Educational Business Analytics Project"
)
