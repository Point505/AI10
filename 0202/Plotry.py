import plotly.express as px

df = px.data.tips()

fig = px.histogram(df, x="sex", y ="tip", histfunc ='sum',facet_col='smoker')

fig.update_xaxes(showline=True, linewidth=3, linecolor = 'black')

