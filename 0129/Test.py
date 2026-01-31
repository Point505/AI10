import pandas as pd


# CSV 파일 읽기 (기존 인덱스 사용)
reviews = pd.read_csv(
    r"C:\Users\김해강\Downloads\wine_reviews_sample.csv",
    index_col=0
)
countries_attr = reviews.country          # 속성 방식
countries_index = reviews['country']    

print(countries_attr)
print(countries_index)