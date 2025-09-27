import requests
from bs4 import BeautifulSoup

code = input("종목 번호를 입력하세요: ")
url = f'https://finance.naver.com/item/main.nhn?code={code}'

try:
    res = requests.get(url)
    res.raise_for_status()  # HTTP 오류가 있으면 예외 발생
    soup = BeautifulSoup(res.content, 'html.parser')
    
    # 여러 가능한 CSS 선택자 시도
    price_selectors = [
        '.no_today .blind',  # 현재 주가
        '#_nowVal',  # 현재가
        '.no_today',  # 오늘의 가격
        '.today .blind',  # 오늘 가격
        'p.no_today .blind'  # 현재가 (더 구체적)
    ]
    
    price = None
    for selector in price_selectors:
        price_element = soup.select_one(selector)
        if price_element:
            price = price_element
            break
    
    if price:
        print(f"현재 {code} 주가는 {price.text}원입니다.")
    else:
        print(f"종목 코드 {code}의 주가 정보를 찾을 수 없습니다.")
        print("다른 종목 코드를 시도해보세요. (예: 005930 - 삼성전자)")
        
except requests.exceptions.RequestException as e:
    print(f"네트워크 오류가 발생했습니다: {e}")
except Exception as e:
    print(f"오류가 발생했습니다: {e}")