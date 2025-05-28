def calculate_kpis(df):
    total_revenue = df['Revenue'].sum()
    total_orders = df['Order ID'].nunique()
    avg_order_value = total_revenue / total_orders
    top_product = df.groupby('Product')['Revenue'].sum().idxmax()
    
    return {
        "Total Revenue": total_revenue,
        "Total Orders": total_orders,
        "Avg Order Value": avg_order_value,
        "Top Product": top_product
    }
