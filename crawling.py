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




#ul → review_list : ul 태그가 리뷰 목록을 나타내므로 의미를 반영해 이름을 변경했습니다.
#lis → review_items : 리뷰 항목(li 태그들)을 나타내므로 의미를 반영했습니다.
#li → review_item : 반복문에서 각 리뷰 항목을 처리하므로 이름 변경.
#review_text → review_title : 리뷰 제목을 저장하는 변수로 이름 변경.
#불필요한 조건 제거:
#lis = ul.find_all('li') if ul else []는 이미 ul의 존재를 확인했으므로 중복 조건을 제거했습니다.
#에러 처리 강화:
#review_title_tag 및 comment_tag 유효성 확인을 추가하여, 태그가 없는 경우에 대한 에러 방지.