import pyupbit
import sqlite3
import datetime

# 데이터베이스 연결
conn = sqlite3.connect('upbit.db')
cur = conn.cursor()

# 기존 테이블 삭제 (스키마 변경을 위해)
cur.execute("DROP TABLE IF EXISTS BTC_KRW")

# 테이블 생성 (더 나은 스키마)
cur.execute("""
CREATE TABLE BTC_KRW (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    price REAL NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# 시세 조회
price = pyupbit.get_current_price("KRW-BTC")
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# 조회 결과 출력
print(f"시간: {now}, 비트코인 가격: {price:,.0f}원")

# 데이터베이스에 저장 (경고 해결)
cur.execute("INSERT INTO BTC_KRW (timestamp, price) VALUES (?, ?)", (now, price))
conn.commit()

# 저장된 데이터 확인
cur.execute("SELECT COUNT(*) FROM BTC_KRW")
count = cur.fetchone()[0]
print(f"총 저장된 데이터 수: {count}개")

# 최근 5개 데이터 조회
cur.execute("SELECT timestamp, price FROM BTC_KRW ORDER BY id DESC LIMIT 5")
recent_data = cur.fetchall()
print("\n최근 5개 데이터:")
for data in recent_data:
    print(f"  {data[0]}: {data[1]:,.0f}원")

# 연결 종료
conn.close()
