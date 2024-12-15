from wordcloud import WordCloud
import pandas as pd
import matplotlib.pyplot as plt
import os
from collections import Counter
import re

# 한글 폰트 설정
plt.rc('font', family='Malgun Gothic')  # Windows의 경우

# CSV 파일이 있는 폴더 경로
folder_path = 'C:\\Users\\rosie\\Desktop\\24파이데\\wordcloud_data' 

# 특정 접미사로 끝나는 단어를 제외하는 함수
def filter_words(words, company):
    # 정규 표현식으로 '-다', '-며', '-는'으로 끝나는 단어를 제외
    filtered = [word for word in words if not re.search(r'[-다]$', word)]
    # 회사 이름 제외
    filtered = [word for word in filtered if word != company]
    return filtered

# 워드클라우드 생성 함수
def generate_wordcloud(company, text):  
    # 단어 빈도 계산
    words = text.split()
    filtered_words = filter_words(words, company)  # 필터링된 단어 리스트
    word_counts = Counter(filtered_words)
    
    # 상위 10% 단어 수 계산
    top_n = max(1, len(word_counts) // 10)  # 최소 1개 단어는 포함
    top_words = dict(word_counts.most_common(top_n))  # 상위 10% 단어 추출

    # 워드클라우드 생성
    wordcloud = WordCloud(font_path='C:/Windows/Fonts/malgun.ttf', 
                          background_color='white', 
                          width=800, 
                          height=400, 
                          normalize_plurals=False).generate_from_frequencies(top_words)  # 빈도 기반 생성
                          
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'Word Cloud for {company}')
    
    # 이미지 파일로 저장
    output_path = f'{company}_wordcloud.png'
    plt.savefig(output_path, bbox_inches='tight', pad_inches=0.1)  # 이미지 저장
    plt.close()  # 현재 플롯 닫기

# 폴더 내 모든 CSV 파일 순회
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        df = pd.read_csv(file_path, encoding='utf-8')
        
        # 각 열에 대해 워드클라우드 생성
        for column in df.columns:
            text = ' '.join(df[column].dropna().astype(str))  # NaN 값 처리 및 문자열 변환
            generate_wordcloud(column, text) 
