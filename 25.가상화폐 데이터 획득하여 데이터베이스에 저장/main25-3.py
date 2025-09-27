import sqlite3

# 데이터베이스 연결
conn = sqlite3.connect('upbit.db')
cur = conn.cursor()

# BTC-KRW 가격 조회
cur.execute("SELECT * FROM BTC_KRW ORDER BY id DESC")
rows = cur.fetchall()

print("비트코인 가격 데이터베이스 조회 결과:")
print("-" * 60)
print(f"{'ID':<5} {'시간':<20} {'가격':<15} {'생성일시':<20}")
print("-" * 60)

# 조회 결과 출력
for row in rows:
    id_val, timestamp, price, created_at = row
    print(f"{id_val:<5} {timestamp:<20} {price:>12,.0f}원 {created_at:<20}")

# 통계 정보
cur.execute("SELECT COUNT(*), MIN(price), MAX(price), AVG(price) FROM BTC_KRW")
stats = cur.fetchone()
print("-" * 60)
print(f"총 데이터 수: {stats[0]}개")
print(f"최저가: {stats[1]:,.0f}원")
print(f"최고가: {stats[2]:,.0f}원")
print(f"평균가: {stats[3]:,.0f}원")

# 연결 종료
conn.close()
