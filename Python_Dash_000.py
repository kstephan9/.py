#

import dash
import dash_core_components as dcc
import dash_html_components as html
import datetime
from iexfinance.stocks import get_historical_data
from dateutil.relativedelta   import relativedelta
import plotly.graph_objs as go

import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style

import pandas as pd
import pandas_datareader.data as web



start_date = datetime.datetime.today() - relativedelta(years=5)
end_date = datetime.datetime.today()

start = dt.datetime(2000, 1, 1)
end   = dt.datetime(2019, 12, 31)

df = web.DataReader('TSLA', 'yahoo', start, end)

#df = get_historical_data("GE", start=start_date,end=end_date, output_format = "pandas")


app = dash.Dash()

app.layout = html.Div(
    html.H1(children="Hello, Nora")
    )

print("Done!")
if __name__ == "__main__":
    app.run_server(debug=True)
    gc.

