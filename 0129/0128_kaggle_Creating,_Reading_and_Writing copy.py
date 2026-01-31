import pandas as pd
import streamlit as st
import altair as alt

st.set_page_config(page_title="COVID-19 Dashboard", layout="wide")

# OWID COVID 데이터 (공식 카탈로그, 최신/compact)
OWID_COMPACT_CSV = "https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv"

@st.cache_data(ttl=60 * 60)  # 1시간 캐시(너무 자주 다운받지 않게)
def load_data() -> pd.DataFrame:
    df = pd.read_csv(OWID_COMPACT_CSV)
    # 날짜 파싱
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    # 숫자 컬럼 안전 변환(혹시 모를 문자열 대비)
    num_cols = [
        "new_cases", "new_deaths",
        "new_cases_per_million", "new_deaths_per_million",
        "total_cases", "total_deaths",
        "people_vaccinated", "people_fully_vaccinated",
        "total_vaccinations", "new_vaccinations",
        "new_vaccinations_smoothed",
        "positive_rate", "tests_per_case",
        "icu_patients", "hosp_patients",
        "reproduction_rate",
    ]
    for c in num_cols:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors="coerce")
    return df

df = load_data()

st.title("🦠 COVID-19 Dashboard (OWID)")
st.caption("데이터 출처: Our World in Data (OWID) 카탈로그 CSV")

# -------------------------
# 사이드바 필터
# -------------------------
st.sidebar.header("필터")

# 국가/지역 리스트(OWID 지역코드 포함 가능)
locations = sorted(df["location"].dropna().unique().tolist())
default_loc = "South Korea" if "South Korea" in locations else (locations[0] if locations else None)

location = st.sidebar.selectbox("국가/지역 선택", options=locations, index=locations.index(default_loc) if default_loc else 0)

metric_map = {
    "일일 확진자 (new_cases)": "new_cases",
    "일일 확진자 / 백만명 (new_cases_per_million)": "new_cases_per_million",
    "일일 사망자 (new_deaths)": "new_deaths",
    "일일 사망자 / 백만명 (new_deaths_per_million)": "new_deaths_per_million",
    "누적 확진자 (total_cases)": "total_cases",
    "누적 사망자 (total_deaths)": "total_deaths",
    "신규 접종(스무딩) (new_vaccinations_smoothed)": "new_vaccinations_smoothed",
    "양성률 (positive_rate)": "positive_rate",
    "재생산지수 R (reproduction_rate)": "reproduction_rate",
    "입원환자 (hosp_patients)": "hosp_patients",
    "ICU 환자 (icu_patients)": "icu_patients",
}
metric_label = st.sidebar.selectbox("지표 선택", list(metric_map.keys()), index=1)
metric = metric_map[metric_label]

loc_df = df[df["location"] == location].copy()
loc_df = loc_df.dropna(subset=["date"]).sort_values("date")

if loc_df.empty:
    st.error("선택한 국가/지역 데이터가 없습니다.")
    st.stop()

min_date = loc_df["date"].min().date()
max_date = loc_df["date"].max().date()

date_range = st.sidebar.date_input(
    "기간 선택",
    value=(max_date - pd.Timedelta(days=180)).date() if (max_date - pd.Timedelta(days=180)).date() > min_date else min_date,
    min_value=min_date,
    max_value=max_date,
)

# date_input이 단일 날짜로 들어오는 경우 방어
if isinstance(date_range, tuple):
    start_date, end_date = date_range
else:
    start_date, end_date = date_range, max_date

mask = (loc_df["date"].dt.date >= start_date) & (loc_df["date"].dt.date <= end_date)
view_df = loc_df.loc[mask, ["date", metric]].dropna()

# -------------------------
# 상단 KPI
# -------------------------
latest = loc_df.dropna(subset=[metric]).tail(1)
latest_val = float(latest[metric].iloc[0]) if not latest.empty else None
latest_date = latest["date"].iloc[0].date() if not latest.empty else None

# 비교값(전일)
prev = loc_df.dropna(subset=[metric]).tail(2)
delta = None
if len(prev) == 2:
    delta = float(prev[metric].iloc[1] - prev[metric].iloc[0])

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(label=f"{location} - 선택 지표 최신값", value=f"{latest_val:,.3f}" if latest_val is not None else "N/A", delta=f"{delta:+,.3f}" if delta is not None else None)
with c2:
    st.metric(label="최신 데이터 날짜", value=str(latest_date) if latest_date else "N/A")
with c3:
    # 참고용: 누적 확진/사망 (있으면)
    total_cases = loc_df["total_cases"].dropna().tail(1)
    st.metric("누적 확진자", f"{int(total_cases.iloc[0]):,}" if not total_cases.empty else "N/A")
with c4:
    total_deaths = loc_df["total_deaths"].dropna().tail(1)
    st.metric("누적 사망자", f"{int(total_deaths.iloc[0]):,}" if not total_deaths.empty else "N/A")

st.divider()

# -------------------------
# 차트
# -------------------------
st.subheader(f"📈 {metric_label}")

if view_df.empty:
    st.warning("선택한 기간에 해당 지표 데이터가 없습니다.")
else:
    base = alt.Chart(view_df).mark_line().encode(
        x=alt.X("date:T", title="Date"),
        y=alt.Y(f"{metric}:Q", title=metric_label),
        tooltip=[alt.Tooltip("date:T", title="Date"), alt.Tooltip(f"{metric}:Q", title=metric_label, format=",.4f")],
    ).properties(height=380)

    st.altair_chart(base, use_container_width=True)

# -------------------------
# 테이블
# -------------------------
with st.expander("📋 원본 데이터 보기 (최근 50행)"):
    cols_to_show = ["date", "new_cases", "new_deaths", "new_cases_per_million", "new_deaths_per_million",
                    "total_cases", "total_deaths", "new_vaccinations_smoothed", "positive_rate", "reproduction_rate"]
    cols_to_show = [c for c in cols_to_show if c in loc_df.columns]
    st.dataframe(loc_df[cols_to_show].tail(50), use_container_width=True)

st.caption("※ 본 대시보드는 OWID 공개 데이터를 시각화합니다. 지표 정의/결측치(NaN) 존재 가능.")
