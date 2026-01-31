import plotly.express as px
import numpy as np
import pandas as pdimport 
import plotly.express as px
import plotly.graph_objects as go


# 데이터 불러오기
df = px.data.iris()

# express를 활용한 scatter plot 생성
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 title="Using The add_trace() method With A Plotly Express Figure")

fig.add_trace(
    go.Scatter(
        x=[2, 4],
        y=[4, 8],
        mode="lines",
        line=go.scatter.Line(color="gray"),
        showlegend=False)
)

fig.show()


# 데이터 불러오기
df = px.data.iris()

# express를 활용한 scatter plot 생성
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species",
                 title="Using The add_trace() method With A Plotly Express Figure")

fig.add_trace(
    go.Scatter(
        x=[2, 4],
        y=[4, 8],
        mode="lines",
        line=go.scatter.Line(color="gray"),
        showlegend=False)
)

fig.show()
