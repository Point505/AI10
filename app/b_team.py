# b_team.py
import pandas as pd
import plotly.graph_objects as go

def run_market_map_slider(df, selected_regions):
    """
    df: app.py에서 기간 필터까지 적용된 DataFrame(filtered_df)
    selected_regions: 사이드바에서 선택된 지역 리스트
    return: plotly Figure (Treemap + 날짜 슬라이더)
    """
    df = df.copy()

    # 날짜 처리/정렬
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values("date")

    # ✅ 선택 지역만 사용 (df에 존재하는 컬럼만)
    regions = [r for r in selected_regions if r in df.columns]
    if not regions:
        return None

    # 숫자 변환
    df[regions] = df[regions].apply(pd.to_numeric, errors="coerce").fillna(0)

    # ✅ 누적합 (이미 누적 데이터면 이 줄 주석처리)
    df_cum = df.copy()
    df_cum[regions] = df_cum[regions].cumsum()

    dates = df_cum["date"].dt.strftime("%Y-%m-%d").tolist()

    labels = regions
    parents = [""] * len(regions)

    # 프레임 생성(날짜별)
    frames = []
    for i, d in enumerate(dates):
        row = df_cum.iloc[i]
        values = [row[r] for r in regions]

        frames.append(
            go.Frame(
                name=d,
                data=[go.Treemap(
                    labels=labels,
                    parents=parents,
                    values=values,
                    marker=dict(colors=values, colorscale="Reds"),
                    textinfo="label+value",
                    hovertemplate="<b>%{label}</b><br>누적값: %{value:,}<extra></extra>",
                )],
                layout=go.Layout(title_text=f"마켓맵 (기준일: {d})")
            )
        )

    # 초기 화면
    init_row = df_cum.iloc[0]
    init_values = [init_row[r] for r in regions]

    fig = go.Figure(
        data=[go.Treemap(
            labels=labels,
            parents=parents,
            values=init_values,
            marker=dict(colors=init_values, colorscale="Reds"),
            textinfo="label+value",
            hovertemplate="<b>%{label}</b><br>누적값: %{value:,}<extra></extra>",
        )],
        frames=frames
    )

    # 슬라이더
    steps = []
    for d in dates:
        steps.append(dict(
            method="animate",
            args=[[d], {"mode": "immediate",
                        "frame": {"duration": 0, "redraw": True},
                        "transition": {"duration": 0}}],
            label=d
        ))

    fig.update_layout(
        title=f"마켓맵 (기준일: {dates[0]})",
        template="plotly_white",
        margin=dict(t=70, l=10, r=10, b=10),
        sliders=[dict(
            active=0,
            currentvalue={"prefix": "기준일: "},
            pad={"t": 40},
            steps=steps
        )],
    )

    return fig
