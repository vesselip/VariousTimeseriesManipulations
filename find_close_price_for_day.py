import pandas as pd
import numpy as np

# Sample data
data = {
    'timestamp': [
        '2024-12-11 09:30:00', '2024-12-11 16:00:00',
        '2024-12-12 09:30:00', '2024-12-12 16:00:00',
        '2024-12-13 09:30:00', '2024-12-13 15:59:59'
    ],
    'bid': [100, 102, 103, 105, 106, 107],
    'ask': [101, 103, 104, 106, 107, 108]
}

data = pd.read_csv('C:\\Users\\vesse\\Downloads\\tick_data.csv')

# Create DataFrame
df = pd.DataFrame(data)
df['DateTime'] = pd.to_datetime(df['DateTime'])  # Convert to datetime

# Sort by timestamp (important if not already sorted)
df = df.sort_values('DateTime')

# Add a 'date' column to group by day
df['date'] = df['DateTime'].dt.date

# Assuming closing price is the last 'bid' of the day
closing_prices = df.groupby('date')['Bid'].last()

# Convert result to a DataFrame if needed
closing_prices_df = closing_prices.reset_index()
closing_prices_df.columns = ['date', 'closing_price']

print(closing_prices_df)
