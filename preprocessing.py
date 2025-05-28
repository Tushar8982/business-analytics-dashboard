import pandas as pd

def clean_data(df):
    # Rename if necessary (fallback for compatibility)
    if "order_date" in df.columns:
        df['Date'] = pd.to_datetime(df['order_date'])
    elif "Date" in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
    else:
        raise KeyError("No date column found in the data.")
    
    if 'Price' not in df.columns and 'unit_price' in df.columns:
        df['Price'] = df['unit_price']

    if 'Quantity' not in df.columns and 'quantity' in df.columns:
        df['Quantity'] = df['quantity']

    df['Revenue'] = df['Price'] * df['Quantity']
    return df
