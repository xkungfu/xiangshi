import plotly.graph_objects as go
import numpy as np
import itertools


f = open("Result For Old.txt", "r").readlines()[40:80]
df = []
for x in f:
    st = x.split(" ")
    df.append(st[-1])

x = np.arange(40)
y = np.array(df)
fig = go.Figure(data=go.Scatter(x=x, y=y))
fig.show()

