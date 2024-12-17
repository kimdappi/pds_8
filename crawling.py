import requests
from bs4 import BeautifulSoup
import os
import csv

# 기업 리뷰 URL 리스트 (기업 이름과 리뷰 페이지 URL을 매핑)
company_urls = {
    'NAVER': 'https://www.teamblind.com/kr/company/NAVER/review/QIUosA0v4',
    'KAKAO': 'https://www.teamblind.com/kr/company/KAKAO/review/URL2',
    'LINE': 'https://www.teamblind.com/kr/company/LINE/review/URL3'
}

# CSV 파일을 저장할 폴더 생성 (폴더가 없으면 자동으로 생성)
output_folder = '블라인드 현직자 리뷰'  # 리뷰 데이터를 저장할 폴더 이름
os.makedirs(output_folder, exist_ok=True)  # 이미 폴더가 존재해도 오류 발생 X


# 특정 기업의 리뷰와 댓글을 가져와 CSV 파일로 저장하는 함수
def fetch_reviews(url, company_name):
    print(f"[INFO] {company_name} 리뷰 데이터를 가져오는 중...")  # 작업 시작 알림

    # HTTP GET 요청을 보내 URL의 웹 페이지 데이터를 가져옴
    response = requests.get(url)

    # HTTP 응답 상태 코드가 200(성공)인지 확인
    if response.status_code == 200:
        # 가져온 HTML 데이터를 BeautifulSoup을 사용해 파싱
        soup = BeautifulSoup(response.text, 'html.parser')

        # 리뷰 목록이 담긴 ul 태그 찾기 (클래스명: 'review_item')
        review_list = soup.find('ul', class_='review_item')

        if review_list:
            # CSV 파일 저장 경로 설정 (기업명에 따라 파일명 변경)
            csv_file_path = os.path.join(output_folder, f'{company_name}_리뷰.csv')

            # CSV 파일 열기 및 헤더 작성
            with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['리뷰 제목', '댓글'])  # CSV 파일 첫 줄에 헤더 작성

                # 리뷰 항목(li 태그들)을 모두 찾기
                review_items = review_list.find_all('li')

                # 각 리뷰 항목을 순회하며 리뷰 제목과 댓글을 추출
                for review_item in review_items:
                    # 리뷰 제목 추출 (div 태그, 클래스명: 'rvtit')
                    review_title_tag = review_item.find('div', class_='rvtit')
                    review_title = review_title_tag.text.strip() if review_title_tag else "제목 없음"  # 예외 처리 포함

                    # 댓글 내용 추출 (div 태그, 클래스명: 'parag')
                    comment_tags = review_item.find_all('div', class_='parag')
                    comments = [comment.text.strip() for comment in comment_tags]  # 각 댓글에서 텍스트만 추출

                    # 리뷰 제목과 각 댓글을 CSV 파일에 저장
                    for comment in comments:
                        csv_writer.writerow([review_title, comment])

            print(f"[SUCCESS] {company_name} 리뷰 데이터를 {csv_file_path}에 저장했습니다.\n")  # 성공 메시지 출력
        else:
            # ul 태그를 찾지 못한 경우 에러 메시지 출력
            print(f"[ERROR] {company_name}: 리뷰 목록을 찾을 수 없습니다.")
    else:
        # HTTP 요청 실패 시 상태 코드 출력
        print(f"[ERROR] {company_name}: 페이지를 가져오지 못했습니다. 상태 코드: {response.status_code}")


# 모든 기업 URL에 대해 자동으로 리뷰 가져오기
for company_name, url in company_urls.items():
    fetch_reviews(url, company_name)  # 각 기업의 URL과 이름을 함수에 전달해 처리
