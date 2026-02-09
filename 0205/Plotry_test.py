# 2️⃣ 슬라이더로 프레임 이동(드래그 가능)
import plotly.graph_objects as go

frames = [
    go.Frame(name=str(i), data=[go.Scatter(y=[i, i+1, i+2])])
    for i in range(5)
]

fig = go.Figure(
    data=[go.Scatter(y=[0, 1, 2])],
    frames=frames
)

fig.update_layout(
    sliders=[dict(
        steps=[dict(method="animate", args=[[str(i)]], label=str(i))
               for i in range(5)]
    )]
)

fig.show()
