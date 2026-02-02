import plotly.express as px
import plotly.graph_objects as go

df = px.data.iris()

fig = px.scatter(
    df,
    x="sepal_width",
    y="sepal_length",
    color="species",
    title="Using add_trace() with a Plotly Express Figure",
)

fig.add_trace(
    go.Scatter(
        x=[2, 4],
        y=[4, 8],
        mode="lines",
        line=dict(color="gray"),
        showlegend=False,
    )
)

fig.show()

# pyhon -c "import plotry; print(plotly.__version__)"