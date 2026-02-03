"""import plotly.express as px

df = px.data.tips()

fig = px.histogram(df, x="sex", y ="tip", histfunc ='sum',facet_col='smoker')

fig.update_xaxes(showline=True, linewidth=3, linecolor = 'black')


fig.show()
"""

"""
        Figure (fig)
    ├─ Trace 1  ← 선 / 점 / 막대 하나
    ├─ Trace 2
    ├─ Trace 3
    └─ Layout   ← 제목, 축, 범례, 크기
        
"""
"""
import plotly.graph_objects as go

x = ["A", "B", "C", "D"]

confirmed = [100, 200, 150, 300]

death_rate = [0.2, 0.15, 0.18, 0.12]

fig = go.Figure()

fig.add_trace(go.Bar(x=x, y=confirmed, name="confirmed", yaxis="y1"))

fig.add_trace(go.Histogram(x=x, y=death_rate, name="death_rate", yaxis="y2"))


fig.update_layout(
    title="Dual axis: bar + line", #  상단에 나올 이름
    yaxis=dict(title="confirmed"), # 
    yaxis2=dict(title="death rate", overlaying="y", side="right"),
    # 위치는 y 축 오른쪽
)

fig.show()"""



import pandas as pd
import plotly.graph_objects as go

file_path = r"C:\Users\김해강\Downloads\covid.xlsx"

# =========================
# 1) 확진자 시트 읽기 (헤더 2줄)
# =========================
df_c = pd.read_excel(file_path, sheet_name="확진자", header=[6, 7])

# =========================
# 2) 사망자 시트 읽기 (헤더 2줄)
# =========================
df_d = pd.read_excel(file_path, sheet_name="사망자", header=[7, 8])

# =========================
# 3) 사용할 컬럼 지정
#    (MultiIndex 컬럼이라 ('2023년', '8월...') 이런 식으로 선택해야 함)
# =========================
REGION_COL = ("시도명", "Unnamed: 0_level_1")
DISTRICT_COL = ("시군구", "Unnamed: 1_level_1")
TARGET_COL = ("2023년", "8월 (~'23.8.31.)")   # 원하는 월로 바꾸면 됨

# =========================
# 4) 필요한 컬럼만 뽑고, 시도(지역) 단위 "합계" 행만 사용
#    - 각 시도마다 시군구 '합계' 행이 있어서 이걸 쓰면 깔끔함
# =========================
cases = df_c[[REGION_COL, DISTRICT_COL, TARGET_COL]].copy()
cases.columns = ["region", "district", "confirmed"]

deaths = df_d[[REGION_COL, DISTRICT_COL, TARGET_COL]].copy()
deaths.columns = ["region", "district", "death"]

# '합계' 행만 남기기 (시도별 합계)
cases = cases[cases["district"] == "합계"].copy()
deaths = deaths[deaths["district"] == "합계"].copy()

# 숫자 변환 (사망자 시트는 '-' 같은 문자가 있어서 처리 필요)
cases["confirmed"] = pd.to_numeric(cases["confirmed"], errors="coerce").fillna(0)
deaths["death"] = pd.to_numeric(deaths["death"], errors="coerce").fillna(0)

# =========================
# 5) 확진자-사망자 병합 + 사망률 계산
# =========================
merged = pd.merge(cases[["region", "confirmed"]], deaths[["region", "death"]], on="region", how="inner")

# 사망률(%) = 사망 / 확진 * 100 (0 나눗셈 방지)
merged["death_rate"] = merged.apply(
    lambda r: (r["death"] / r["confirmed"] * 100) if r["confirmed"] > 0 else 0,
    axis=1
)

# 확진자 많은 순으로 정렬
merged = merged.sort_values("confirmed", ascending=False)

x = merged["region"]
confirmed = merged["confirmed"]
death_rate = merged["death_rate"]

# =========================
# 6) Plotly 이중축 그래프 생성
# =========================
fig = go.Figure()

# 막대: 확진자(왼쪽 y축)
fig.add_trace(
    go.Bar(
        x=x,
        y=confirmed,
        name="확진자 수",
        yaxis="y1"
    )
)

# 선: 사망률(오른쪽 y축)
fig.add_trace(
    go.Scatter(
        x=x,
        y=death_rate,
        name="사망률(%)",
        mode="lines+markers",
        yaxis="y2"
    )
)

fig.update_layout(
    title="지역별 확진자 수(막대) + 사망률(선) (2023년 8월)",
    xaxis=dict(title="지역(시도)"),
    yaxis=dict(title="확진자 수"),
    yaxis2=dict(title="사망률(%)", overlaying="y", side="right"),
    template="plotly_white",
    legend=dict(x=0.01, y=0.99)
)

fig.show()
