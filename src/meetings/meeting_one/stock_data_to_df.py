# Import the library you're using, e.g., yfinance
import yfinance as yf
import pandas as pd

def make_df():
  #Define your stock symbol and date range
  stock_symbol = "AAPL"
  start_date = "2023-01-01"
  end_date = "2023-12-31"

  #Fetch historical data
  stock = yf.Ticker(stock_symbol)
  data = stock.history(start=start_date, end=end_date)

  #Convert to a Pandas DataFrame
  df = pd.DataFrame(data)

  #erase all columns other than close and date
  df = df.drop(['Open', 'High', 'Low', 'Volume', 'Dividends', 'Stock Splits'], axis=1)
  return df

print(make_df())