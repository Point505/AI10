import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1) 엑셀 파일 읽기
# -----------------------------
file_path = r"C:\Users\김해강\Downloads\질병관리청_코로나19 시군구별 월별 확진자 및 사망 발생 현황_20230831.xlsx"

df = pd.read_excel(file_path)

# -----------------------------
# 2) 컬럼명 확인 (안 보이면 print로 한 번 찍어봐도 됨)
# -----------------------------
# print(df.columns)

# 컬럼명 표준화 (실제 데이터에 맞게 자동 대응)
df = df.rename(columns={
    "시도": "region",
    "시도명": "region",
    "시군구": "district",
    "시군구명": "district",
    "확진자수": "confirmed",
    "확진자": "confirmed",
    "월간 확진자 수": "confirmed"
})

# -----------------------------
# 3) 필요한 컬럼만 선택
# -----------------------------
df = df[["region", "confirmed"]]

# 혹시 문자열이면 숫자로 변환
df["confirmed"] = pd.to_numeric(df["confirmed"], errors="coerce").fillna(0)

# -----------------------------
# 4) 시도(지역) 단위로 집계
# -----------------------------
region_sum = (
    df.groupby("region", as_index=False)["confirmed"]
      .sum()
      .sort_values("confirmed", ascending=False)
)

regions = region_sum["region"].tolist()
counts = region_sum["confirmed"].tolist()

# -----------------------------
# 5) 색상 맵 (확진자 많을수록 진하게)
# -----------------------------
max_v = max(counts)
colors = [plt.cm.Greens(v / max_v) for v in counts]

# -----------------------------
# 6) k 단위 포맷 함수
# -----------------------------
def fmt_k(v):
    return f"{v/1000:.1f}k" if v >= 1000 else str(int(v))

# -----------------------------
# 7) 그래프 출력
# -----------------------------
plt.figure(figsize=(15, 6))
bars = plt.bar(regions, counts, color=colors)

plt.suptitle("🗺️ 지역별 확진자 발생 비교", fontsize=16, fontweight="bold")
plt.title("질병관리청 시군구별 데이터를 시도 단위로 집계 (2023-08-31 기준)", fontsize=11)

plt.xlabel("지역")
plt.ylabel("확진자 수")

plt.grid(axis="y", linestyle="--", alpha=0.3)

# 막대 위 라벨
for bar, v in zip(bars, counts):
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        bar.get_height(),
        fmt_k(v),
        ha="center",
        va="bottom",
        fontsize=9
    )

plt.tight_layout()
plt.show()
