from faker import Faker
from openpyxl import Workbook
import random

fake = Faker('ko_KR')

def generate_korean_phone():
    """010으로 시작하는 한국 전화번호 생성"""
    # 010-XXXX-XXXX 형식
    middle = random.randint(1000, 9999)
    last = random.randint(1000, 9999)
    return f"010-{middle}-{last}"

# 엑셀 파일 생성
wb = Workbook()
ws = wb.active

# 헤더 추가
ws.append(['이름', '성별', '이메일', '전화번호', '주소', '생년월일'])

print("가짜 개인정보를 생성하고 있습니다...")

# 가짜 데이터 생성 및 저장
for i in range(1000):
    name = fake.name()
    gender = fake.random_element(elements=('남', '여'))
    email = fake.email()
    phone_number = generate_korean_phone()  # 010으로 시작하는 전화번호
    address = fake.address()
    birthdate = fake.date_of_birth(minimum_age=20, maximum_age=69)  # 20세 이상 70세 미만
    ws.append([name, gender, email, phone_number, address, birthdate])
    
    # 진행률 표시
    if (i + 1) % 100 == 0:
        print(f"진행률: {i + 1}/1000")

# 엑셀 파일 저장 (현재 디렉토리에 저장)
wb.save('개인정보.xlsx')
print("엑셀 파일이 생성되었습니다: 개인정보.xlsx")
print(f"총 {1000}개의 가짜 개인정보가 저장되었습니다.")
