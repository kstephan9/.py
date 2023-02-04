
# https://www.youtube.com/watch?v=J_Cy_QjG6NE - Part 1
# https://www.youtube.com/watch?v=hRH01ZzT2NI - Part 2
# https://www.youtube.com/watch?v=wv2MXJIdKRY - Part 3
# https://www.youtube.com/watch?v=37Zj955LFT0 - Part 4

import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
import plotly
import plotly.graph_objs as go
from collections import deque
import datetime
import random

X = deque(maxlen=20)
Y = deque(maxlen=20)
X.append(1)
Y.append(1)


app = dash.Dash(__name__)
app.layout = html.Div(
    [
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1000,
            n_intervals = 0
            )
    ]
)

@app.callback(
    Output('live-graph', 'figure'),
#    events = [Event('graph-update', 'interval')])
    [Input('graph-update', 'n_intervals')])


def update_graph_scatter(n):
    #global X
    #global Y
    X.append(X[-1]+1)
    Y.append(Y[-1]+Y[-1]*random.uniform(-0.1, 0.1))

    data = plotly.graph.objs.Scatter(x=list(X), y=list(Y),
        name='Scatter',
        mode='line+markers'
        )

    return {'data' : [data], 'layout': go.Layout(xaxis = dict(range=[min(X), max(X)]),
                                                 yaxis = dict(range=[min(Y), max(Y)]))}


if __name__ == '__main__':
    app.run_server(debug=True)



