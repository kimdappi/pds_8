
import pandas as pd
import re
from konlpy.tag import Okt # Import Okt from konlpy.tag
import nltk
nltk.download('punkt_tab')

# CSV 파일을 다시 데이터프레임으로 불러오기
df = pd.read_csv('blind_review.csv')

# 확인을 위해 데이터프레임 출력
print(df.head(1))

import pandas as pd
from nltk import word_tokenize, pos_tag
from konlpy.tag import Okt
import re

# CSV 파일을 데이터프레임으로 불러오기
df = pd.read_csv('blind_review.csv')

def tokenize_pros_values(df, column_names):
    tokenized_dict = {}

    for column_name in column_names:
        # 각 열의 값을 가져와서 텍스트로 결합
        text_data = ' '.join(df[column_name].dropna().astype(str))

        # 텍스트를 단어 토큰화
        tokenized_sentence = word_tokenize(text_data)

        # 딕셔너리에 열 명과 토큰화 결과 추가
        tokenized_dict[column_name] = tokenized_sentence

    return tokenized_dict

# 함수 호출 예시
pros_columns = ['네이버 장점', '카카오 장점', '라인 장점', '쿠팡 장점', '배민 장점', '페이스북 장점', '아마존 장점', '애플 장점', '넷플릭스 장점', '구글 장점']
result_pros_dic = tokenize_pros_values(df, pros_columns)

# 결과 출력
for key, value in result_pros_dic.items():
    print(f"{key}: {value}")

print('-----------------------------------------------------------------------')

# 예시로 불용어 처리할 불용어 리스트 생성
stop_words = set(". , 점 를 이 가 은 것 것도 그리고 는 입니다 또한 ? ".split())

# Okt 객체 생성
okt = Okt()

# 각 장점 열에 대해 불용어 제거 수행
result_pros_dic_no_stopwords = {}

for key, value in result_pros_dic.items():
    # 불용어 제거
    result = [word for word in value if word not in stop_words]
    result_pros_dic_no_stopwords[key] = result

# 결과 출력
for key, value in result_pros_dic_no_stopwords.items():
    print(f"{key} 불용어 제거 전: {result_pros_dic[key]}")
    print(f"{key} 불용어 제거 후: {value}\n")

import pandas as pd
from nltk import word_tokenize, pos_tag
from konlpy.tag import Okt
import re

# CSV 파일을 데이터프레임으로 불러오기
df = pd.read_csv('blind_review.csv')

def tokenize_cons_values(df, column_names):
    tokenized_dict = {}

    for column_name in column_names:
        # 각 열의 값을 가져와서 텍스트로 결합
        text_data = ' '.join(df[column_name].dropna().astype(str))

        # 텍스트를 단어 토큰화
        tokenized_sentence = word_tokenize(text_data)

        # 딕셔너리에 열 명과 토큰화 결과 추가
        tokenized_dict[column_name] = tokenized_sentence

    return tokenized_dict

# 함수 호출 예시
cons_columns = ['네이버 단점', '카카오 단점', '라인 단점', '쿠팡 단점', '배민 단점', '페이스북 단점', '아마존 단점', '애플 단점', '넷플릭스 단점', '구글 단점']
result_cons_dic = tokenize_cons_values(df, cons_columns)

# 결과 출력
for key, value in result_cons_dic.items():
    print(f"{key}: {value}")

print('-----------------------------------------------------------------------')

# 예시로 불용어 처리할 불용어 리스트 생성
stop_words = set(". , 점 를 이 가 은 것 것도 그리고 는 입니다 또한 ? ".split())

# Okt 객체 생성
okt = Okt()

# 각 장점 열에 대해 불용어 제거 수행
result_cons_dic_no_stopwords = {}

for key, value in result_cons_dic.items():
    # 불용어 제거
    result = [word for word in value if word not in stop_words]
    result_cons_dic_no_stopwords[key] = result

# 결과 출력
for key, value in result_cons_dic_no_stopwords.items():
    print(f"{key} 불용어 제거 전: {result_cons_dic[key]}")
    print(f"{key} 불용어 제거 후: {value}\n")

#텍스트 정제 시도 - ok
# CSV 파일을 데이터프레임으로 불러오기
new_df = pd.read_csv('blind_review.csv')

# 정규표현식을 사용하여 특수문자 제거
def clean_text(text):
    # 정규표현식을 사용하여 특수문자 제거
    cleaned_text = re.sub(r'[;,!?\ㅠㅠ.():/~-ㅇㅇ....~]', '', str(text))
    return cleaned_text


company_list = ['네이버 장점', '네이버 단점', '카카오 장점', '카카오 단점',
                    '라인 장점', '라인 단점', '쿠팡 장점', '쿠팡 단점',
                    '배민 장점', '배민 단점', '페이스북 장점', '페이스북 단점',
                    '아마존 장점', '아마존 단점', '애플 장점', '애플 단점',
                    '넷플릭스 장점', '넷플릭스 단점', '구글 장점', '구글 단점']


for i in company_list:
  df[i] = df[i].apply(clean_text)



# 정제된 데이터프레임을 새로운 CSV 파일로 저장
df.to_csv('cleaned_blind_review.csv', index=False)

# CSV 파일을 다시 데이터프레임으로 불러오기 (확인을 위해)
clean_df = pd.read_csv('cleaned_blind_review.csv')

# 확인을 위해 데이터프레임 출력
print(clean_df.head(5))
