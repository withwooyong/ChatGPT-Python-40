import pyupbit

# 모든 가상화폐의 티커(ticker) 리스트를 조회합니다.
tickers = pyupbit.get_tickers()

# 가상화폐 이름 매핑
crypto_names = {
    'KRW-BTC': '비트코인',
    'KRW-ETH': '이더리움',
    'KRW-ADA': '에이다',
    'KRW-DOT': '폴카닷',
    'KRW-LINK': '체인링크',
    'KRW-XRP': '리플',
    'KRW-LTC': '라이트코인',
    'KRW-BCH': '비트코인캐시',
    'KRW-SOL': '솔라나',
    'KRW-AVAX': '아발란체',
    'KRW-ATOM': '코스모스',
    'KRW-MATIC': '폴리곤',
    'KRW-UNI': '유니스왑',
    'KRW-AAVE': '에이브',
    'KRW-SAND': '샌드박스',
    'KRW-MANA': '디센트럴랜드',
    'KRW-AXS': '엑시인피니티',
    'KRW-CHZ': '칠리즈',
    'KRW-ENJ': '엔진코인',
    'KRW-HBAR': '헤데라',
    'KRW-VET': '비체인',
    'KRW-ALGO': '알고랜드',
    'KRW-EGLD': '멀티버스X',
    'KRW-NEAR': '니어프로토콜',
    'KRW-FLOW': '플로우',
    'KRW-ICP': '인터넷컴퓨터',
    'KRW-THETA': '쎄타토큰',
    'KRW-FIL': '파일코인',
    'KRW-TRX': '트론',
    'KRW-ETC': '이더리움클래식',
    'KRW-XLM': '스텔라루멘',
    'KRW-APT': '앱토스',
    'KRW-SUI': '수이',
    'KRW-OP': '옵티미즘',
    'KRW-ARB': '아비트럼',
    'KRW-MNT': '만틀',
    'KRW-IMX': '이뮤터블X',
    'KRW-RENDER': '렌더토큰',
    'KRW-INJ': '인젝티브',
    'KRW-TIA': '셀레스티아',
    'KRW-JUP': '주피터',
    'KRW-WLD': '월드코인',
    'KRW-PYTH': '파이스',
    'KRW-STRK': '스트라이크',
    'KRW-ONDO': '온도파이낸스',
    'KRW-W': '웜홀',
    'KRW-ENA': '에나',
    'KRW-ALT': '알트레이어',
    'KRW-ZRO': '제로',
    'KRW-BLUR': '블러',
    'KRW-ARKM': '아크햄',
    'KRW-COMP': '컴파운드',
    'KRW-ENS': '이더리움네임서비스',
    'KRW-GRT': '그래프',
    'KRW-1INCH': '1인치',
    'KRW-SNX': '신세틱스',
    'KRW-ZRX': '0x',
    'KRW-BAT': '베이직어텐션토큰',
    'KRW-LRC': '루프링',
    'KRW-KNC': '카이버네트워크',
    'KRW-REP': '어거',
    'KRW-ZIL': '질리카',
    'KRW-ICX': '아이콘',
    'KRW-ONT': '온톨로지',
    'KRW-WAVES': '웨이브즈',
    'KRW-QTUM': '퀀텀',
    'KRW-NEO': '네오',
    'KRW-IOTA': '아이오타',
    'KRW-EOS': '이오스',
    'KRW-STEEM': '스팀',
    'KRW-SNT': '스테이터스',
    'KRW-REQ': '리퀘스트',
    'KRW-STORJ': '스토리지',
    'KRW-OMG': '오미세고',
    'KRW-POWR': '파워렛저',
    'KRW-LSK': '리스크',
    'KRW-ARK': '아크',
    'KRW-ADX': '아드엑스',
    'KRW-SYS': '시스코인',
    'KRW-PIVX': '피벡스',
    'KRW-EMC2': '아인스타이늄',
    'KRW-NAV': '네이비코인',
    'KRW-CVC': '시빅',
    'KRW-DGB': '디지바이트',
    'KRW-SC': '시아코인',
    'KRW-IGNIS': '이그니스',
    'KRW-STRAT': '스트라티스',
    'KRW-ARK': '아크',
    'KRW-ADX': '아드엑스',
    'KRW-SYS': '시스코인',
    'KRW-PIVX': '피벡스',
    'KRW-EMC2': '아인스타이늄',
    'KRW-NAV': '네이비코인',
    'KRW-CVC': '시빅',
    'KRW-DGB': '디지바이트',
    'KRW-SC': '시아코인',
    'KRW-IGNIS': '이그니스',
    'KRW-STRAT': '스트라티스'
}

print(f"총 {len(tickers)}개의 가상화폐 가격 정보:")
print("-" * 60)

for ticker in tickers:
    try:
        price = pyupbit.get_current_price(ticker)
        if price is not None:
            # 가격을 보기 좋게 포맷팅
            if price >= 1:
                formatted_price = f"{price:,.0f}"
            else:
                formatted_price = f"{price:.8f}".rstrip('0').rstrip('.')
            
            # 코인 이름 가져오기
            coin_name = crypto_names.get(ticker, ticker.split('-')[1] if '-' in ticker else ticker)
            
            print(f"{ticker}: {formatted_price}원 ({coin_name})")
    except Exception as e:
        print(f"{ticker}: 오류 - {str(e)}")