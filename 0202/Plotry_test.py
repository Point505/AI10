import plotly.graph_objects as go
import numpy as np

from plotly.subplots import  make_subplots

np.random.seed(1)


N = 100

random_x = np.linspace(0,1,N) # 시작과 끝 그리고 분할

random_y0 = np.random.randn(N)-5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N)+5



fig = go.Figure()


fig = make_subplots(rows=1,cols=2) # 1행에 2열 차트
fig.add_trace(go.Scatter(x=random_x,y=random_y0, mode='lines',name='lines'))
fig.add_trace(go.Scatter(x=random_x,y=random_y1, mode='lines',name='lines'))
fig.add_trace(go.Scatter(x=random_x,y=random_y2, mode='lines',name='lines'))

fig.add_trace(go.Scatter(x=random_x,y=random_y1, row=1,col=1))
fig.add_trace(go.Scatter(x=random_x,y=random_y2, row=1,col=2))



fig.show()