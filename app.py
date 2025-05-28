# app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import io
import os

from dotenv import load_dotenv
load_dotenv()

from utils.preprocessing import clean_data
from utils.kpi import calculate_kpis
from utils.database import save_to_supabase

st.set_page_config(page_title="Business Analytics Dashboard", layout="wide")
st.title("📊 Business Analytics Dashboard")

uploaded_file = st.file_uploader("Upload a Sales CSV File", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    try:
        df = clean_data(df)
    except Exception as e:
        st.error(f"❌ Error in cleaning data: {e}")
        st.stop()

    # Show raw data
    with st.expander("🔍 Preview Cleaned Data"):
        st.dataframe(df.head(20))

    # KPIs
    st.markdown("### 📌 Key Performance Indicators (KPIs)")
    kpis = calculate_kpis(df)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Total Revenue", f"${kpis['Total Revenue']:.2f}")
    col2.metric("Total Orders", kpis['Total Orders'])
    col3.metric("Avg Order Value", f"${kpis['Avg Order Value']:.2f}")
    col4.metric("Top Product", kpis['Top Product'])

    # Visualizations
    st.markdown("### 📈 Revenue Over Time")
    fig_time = px.line(df, x='Date', y='Revenue', title='Revenue Trend')
    st.plotly_chart(fig_time, use_container_width=True)

    st.markdown("### 📦 Revenue by Product")
    rev_by_product = df.groupby('Product')['Revenue'].sum().reset_index().sort_values(by='Revenue', ascending=False)
    fig_product = px.bar(rev_by_product, x='Product', y='Revenue', title='Revenue by Product')
    st.plotly_chart(fig_product, use_container_width=True)

    # Export Excel
    st.markdown("### 📥 Download Excel Report")
    buffer = io.BytesIO()
    df.to_excel(buffer, index=False, sheet_name="Sales Report")
    buffer.seek(0)
    st.download_button(
        label="Download Processed Report",
        data=buffer,
        file_name="sales_report.xlsx",
        mime="application/vnd.ms-excel"
    )

    # Upload to Supabase
    if st.button("📤 Upload Data to Supabase"):
        if st.button("📤 Upload Data to Supabase", key="upload_button"):
            try:
                save_to_supabase(df, table_name="uploaded_sales_data", if_exists="replace")
                st.success("✅ Data uploaded to Supabase successfully!")
            except Exception as e:
                st.error(f"❌ Upload failed: {e}")
