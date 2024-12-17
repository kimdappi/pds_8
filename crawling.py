import requests
from bs4 import BeautifulSoup

# 리뷰 페이지 URL 설정
url = 'https://www.teamblind.com/kr/company/NAVER/review/QIUosA0v4'

# HTTP GET 요청을 보내 페이지 응답 받기
response = requests.get(url)

# 응답 성공 여부 확인
if response.status_code == 200:
    # HTML 파싱
    soup = BeautifulSoup(response.text, 'html.parser')

    # 리뷰 목록을 포함한 ul 태그 찾기
    review_list = soup.find('ul', class_='review_item')

    if review_list:
        # 리뷰 항목(li 태그들) 추출
        review_items = review_list.find_all('li')

        for review_item in review_items:
            # 리뷰 제목 추출
            review_title_tag = review_item.find('div', class_='rvtit')
            if review_title_tag:
                review_title = review_title_tag.text.strip()
                print(f"리뷰 제목: {review_title}")

            # 리뷰에 포함된 댓글 추출
            comment_tags = review_item.find_all('div', class_='parag')
            for comment_tag in comment_tags:
                comment_text = comment_tag.text.strip()
                print(f"댓글: {comment_text}")
    else:
        print('리뷰 목록을 포함한 ul 태그를 찾을 수 없습니다.')
else:
    # 요청 실패 시 상태 코드 출력
    print(f'페이지를 가져오지 못했습니다. 상태 코드: {response.status_code}')

