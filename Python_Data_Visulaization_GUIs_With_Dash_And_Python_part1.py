
# https://www.youtube.com/watch?v=J_Cy_QjG6NE - Part 1
# https://www.youtube.com/watch?v=hRH01ZzT2NI - Part 2
# https://www.youtube.com/watch?v=wv2MXJIdKRY - Part 3
# https://www.youtube.com/watch?v=37Zj955LFT0 - Part 4

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
import plotly
import plotly.graph_objs as go
from collections import deque

X = deque(maxlen=20)
Y = deque(maxlen=20)
X.append(1)
Y.append(1)

import random
import datetime

stock = 'TSLA'

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime.now()

df = web.DataReader(stock, 'yahoo', start, end)
print(df.head())

app = dash.Dash()
app.layout = html.Div(children=[
    html.Div('symbol to graph:'),
    dcc.Input(id='input', value='', type='text'),
    html.Div(id='output-graph')
])

@app.callback(
    Output(component_id='output-graph', component_property='children'),
    [Input(component_id='input', component_property='value')]
    )

def update_graph(input_data):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime.now()

    df = web.DataReader(input_data, 'yahoo', start, end)

    return dcc.Graph(id='example-graph',
            figure={'data' : [
                { 'x': df.index, 'y' : df.Close, 'type': 'line', 'name': stock},
                ],
                'layout' :{
                    'title': input_data
                }
            }
        )

if __name__ == '__main__':
    app.run_server(debug=True)



