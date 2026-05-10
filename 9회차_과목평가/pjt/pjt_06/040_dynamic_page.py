import time
import os

from bs4 import BeautifulSoup
#웹 브라우저의 자동화를 가능하게 해주는 라이브러리
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service as EdgeService



# ===== 드라이버 생성 함수 =====
def get_driver_chrome():
    """
    크롬 드라이버를 초기화하여 WebDriver 객체를 반환합니다.
    - 옵션 및 경로 설정을 한 곳에서 관리
    """
    chromeDriver_path = "chromedriver-win64/chromedriver.exe"

    # 크롬 옵션 세팅
    chrome_options = webdriver.ChromeOptions()

    #시작할 때부터 최대화 상태로 열기
    chrome_options.add_argument("--start-maximized")

    # 필요시 활성화
    # chrome_options.add_argument("--headless")

    #navigator.webdriver -> o
    chrome_options.add_argument("disable-blink-features=AutomationControlled")

    #Chrome이 자동화된 테스트 소프트웨어에 의해 제어되고 있습니다 -> x
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation","enable-logging"])

    #시스템 로그 수준 억제 (3: FATAL 에러만 표시)
    chrome_options.add_argument("--log-level=3")


    service = Service(executable_path=chromeDriver_path,log_output=os.devnull)
    return webdriver.Chrome(service=service, options=chrome_options)

def get_driver_edge():
    # 엣지 전용 옵션
    options = webdriver.EdgeOptions()
    service = EdgeService(executable_path="edgedriver_win64/msedgedriver.exe")
    return webdriver.Edge(service=service, options=options)

# ===== 크롤링 함수 =====
def get_google_data(keyword):
    """
    지정된 키워드를 사용하여 Google 검색 결과 페이지의 HTML을 가져온 뒤,
    BeautifulSoup으로 구조화하여 파일로 저장합니다.
    """
    driver = get_driver_chrome()
    # driver = get_driver_edge()

    #구글 접속
    # driver.get(f"https://www.google.com")


    driver.get(f"https://www.google.com/search?q={keyword}")

    time.sleep(15)


    #페이지 HTML 소스 가져오기
    html_doc = driver.page_source
    # print(html_doc)

    #BeautifulSoup으로 파싱
    soup = BeautifulSoup(html_doc, "html.parser")

    results = soup.select("h3")
    titles = []
    for title in results:
        title_text = title.get_text().strip()
        if title_text:
            titles.append(title_text)

    #결과를 파일로 저장
    with open("04_result.txt", "w", encoding="utf-8") as result_file:
        for idx, title in enumerate(titles, 1):
            result_file.write(f"{idx}. {title}\n")
    print(f"04_result.txt 저장 완료 (총 {len(titles)}개)")

    driver.quit()


get_google_data("파이썬")
