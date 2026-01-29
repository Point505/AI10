
# ## 학습 내용
#
# ### 오늘 학습한 챕터
# - pandas groupby()
# - 집계 함수(count, min, max, agg)
# - apply() 활용
# - MultiIndex 개념
# - reset_index()
# - 데이터 정렬(sort_values, sort_index)
#

# ## 실습 코드
#
import pandas as pd


# 1. 점수(points) 기준으로 그룹화 후 개수 세기
# value_counts()와 동일한 동작

points_count = reviews.groupby('points').points.count()
print(points_count)


# 2. 점수별 최저 가격 와인 확인

min_price_by_points = reviews.groupby('points').price.min()
print(min_price_by_points)


# 3. 와이너리별 첫 번째 리뷰 와인 선택 (apply 사용)

first_wine_by_winery = reviews.groupby('winery').apply(
    lambda df: df.title.iloc[0]
)
print(first_wine_by_winery)


# 4. 국가 + 주(province) 기준으로 최고 점수 와인 선택
# idxmax(): 가장 높은 점수의 인덱스 반환

best_wine_by_country_province = reviews.groupby(
    ['country', 'province']
).apply(
    lambda df: df.loc[df.points.idxmax()]
)
print(best_wine_by_country_province)


# 5. agg()를 사용한 여러 통계값 동시 계산

price_summary_by_country = reviews.groupby('country').price.agg(
    ['len', 'min', 'max']
)
print(price_summary_by_country)


# 6. MultiIndex 예제
# 국가 + 주 기준 리뷰 개수

countries_reviewed = reviews.groupby(
    ['country', 'province']
).description.agg(['len'])
print(countries_reviewed)

# MultiIndex 확인
print(type(countries_reviewed.index))


# 7. reset_index()
# MultiIndex → 일반 DataFrame으로 변환

countries_reviewed_reset = countries_reviewed.reset_index()
print(countries_reviewed_reset)


# 8. 값 기준 정렬 (오름차순)

sorted_by_len = countries_reviewed_reset.sort_values(by='len')
print(sorted_by_len)


# 9. 값 기준 정렬 (내림차순)

sorted_by_len_desc = countries_reviewed_reset.sort_values(
    by='len',
    ascending=False
)
print(sorted_by_len_desc)


# 10. 인덱스 기준 정렬

sorted_by_index = countries_reviewed_reset.sort_index()
print(sorted_by_index)

#
# 11. 여러 컬럼 기준 정렬

sorted_multi = countries_reviewed_reset.sort_values(
    by=['country', 'len']
)
print(sorted_multi)


# ## 💡 학습하면서 느낀 점
#
# - groupby는 단순 집계가 아니라 데이터 분석의 핵심 도구라는 걸 느낌
# - value_counts()의 내부 동작을 이해하게 됨
# - apply()는 강력하지만 남용하면 느려질 수 있을 것 같음
# - MultiIndex는 처음엔 헷갈리지만 reset_index()로 해결 가능
# - 정렬을 통해 데이터의 의미가 더 잘 보임
