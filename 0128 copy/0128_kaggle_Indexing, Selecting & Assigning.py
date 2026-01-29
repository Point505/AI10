# ==============================
# ## 학습 내용
# ==============================

# ### 오늘 학습한 챕터
# - pandas 데이터 선택(Selection) 기초
# - 컬럼 선택 (attribute / indexing)
# - iloc, loc을 이용한 인덱싱
# - 조건 기반 필터링
# - 데이터 할당(Assigning data)

# ==============================
# ### 주요 개념 정리
# ==============================

# - 컬럼 선택 방법
#   1) reviews.country  → 속성 접근 방식
#   2) reviews['country'] → 인덱싱 방식 (더 안전하고 일반적)
#
# - iloc (index-based selection)
#   : 행/열의 "위치(번호)" 기준으로 데이터 선택
#   예) iloc[0], iloc[:, 0], iloc[1:3, 0]
#
# - loc (label-based selection)
#   : 인덱스/컬럼 "이름(label)" 기준으로 데이터 선택
#   예) loc[0, 'country'], loc[:, ['points', 'price']]
#
# - iloc vs loc 차이
#   iloc → 끝 인덱스 미포함
#   loc  → 끝 인덱스 포함
#
# - 조건 필터링
#   비교 연산자(==, >= 등)로 boolean Series 생성 후 loc에 사용
#   &, | 연산자로 조건 결합
#
# - isin()
#   여러 값 중 하나에 해당하는지 필터링
#
# - isnull(), notnull()
#   결측치(NaN) 여부 확인
#
# - 데이터 할당
#   새로운 컬럼을 상수 또는 iterable로 추가 가능

# ==============================
# ### 실습 코드
# ==============================

import pandas as pd

# CSV 파일 읽기 (기존 인덱스 사용)
reviews = pd.read_csv(
    "../input/wine-reviews/winemag-data-130k-v2.csv",
    index_col=0
)

# 1. 컬럼 선택 (Series 추출)
countries_attr = reviews.country          # 속성 방식
countries_index = reviews['country']       # 인덱싱 방식

# 2. 단일 값 접근
first_country = reviews['country'][0]

# 3. iloc 사용 (위치 기반)
first_row = reviews.iloc[0]                # 첫 번째 행
country_column = reviews.iloc[:, 0]        # 첫 번째 컬럼
first_three_countries = reviews.iloc[:3, 0]
second_third = reviews.iloc[1:3, 0]
last_five_rows = reviews.iloc[-5:]

# 4. loc 사용 (라벨 기반)
first_country_loc = reviews.loc[0, 'country']
selected_columns = reviews.loc[:, ['taster_name', 'taster_twitter_handle', 'points']]

# 5. 인덱스 변경
reviews_by_title = reviews.set_index('title')

# 6. 조건 필터링
italy_wines = reviews.loc[reviews.country == 'Italy']
italy_high_score = reviews.loc[
    (reviews.country == 'Italy') & (reviews.points >= 90)
]

# OR 조건
italy_or_high_score = reviews.loc[
    (reviews.country == 'Italy') | (reviews.points >= 90)
]

# 7. isin 사용
italy_france = reviews.loc[
    reviews.country.isin(['Italy', 'France'])
]

# 8. 결측치 필터링
priced_wines = reviews.loc[reviews.price.notnull()]

# 9. 데이터 할당 (컬럼 추가)
reviews['critic'] = 'everyone'              # 상수 값 할당
reviews['index_backwards'] = range(len(reviews), 0, -1)

# ==============================
# ## 💡 학습하면서 느낀 점
# ==============================

# - iloc과 loc의 차이를 이해하는 게 중요하다고 느꼈다.
# - 조건 필터링을 사용하니 데이터에서 원하는 정보만 뽑아내는 게 가능해졌다.
# - pandas가 데이터 분석에 왜 많이 쓰이는지 체감했다.

# ==============================
# ## ❓ 질문 및 궁금한 점
# ==============================

# - loc과 iloc 중 실무에서는 어떤 방식을 더 많이 쓰는지 궁금함
# - 조건이 복잡해질 때 가독성을 높이는 방법은?

# ==============================
# ## ✅ 다음 학습 계획
# ==============================

# - 학습일: __________
# - 회차: __________
# - 다음 챕터: 데이터 요약과 통계
#   (describe, mean, value_counts, sort_values)
