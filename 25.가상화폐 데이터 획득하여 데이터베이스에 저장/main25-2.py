import pyupbit
import sqlite3
import datetime
import time

# 데이터베이스 연결
conn = sqlite3.connect('upbit.db')
cur = conn.cursor()

# 테이블 생성 (main25-1.py와 동일한 스키마)
cur.execute("""
CREATE TABLE IF NOT EXISTS BTC_KRW (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT NOT NULL,
    price REAL NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

print("비트코인 가격 모니터링을 시작합니다... (Ctrl+C로 종료)")
print("-" * 50)

# 10초마다 시세 조회 및 데이터베이스에 저장
try:
    while True:
        try:
            price = pyupbit.get_current_price("KRW-BTC")
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            # 조회 결과 출력
            print(f"[{now}] 비트코인 가격: {price:,.0f}원")

            # 데이터베이스에 저장
            cur.execute("INSERT INTO BTC_KRW (timestamp, price) VALUES (?, ?)", (now, price))
            conn.commit()

            # 10초 대기
            time.sleep(10)

        except Exception as e:
            print(f"오류 발생: {e}")
            time.sleep(1)

except KeyboardInterrupt:
    print("\n모니터링을 종료합니다.")

# 연결 종료
conn.close()
