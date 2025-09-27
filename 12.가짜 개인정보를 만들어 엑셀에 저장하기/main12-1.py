from faker import Faker
import random

fake = Faker('ko_KR')  # 한국어 가짜 데이터 생성

# 가짜 이름 생성
name = fake.name()

# 가짜 주소 생성
address = fake.address()

# 가짜 전화번호 생성 (010으로 시작)
def generate_korean_phone():
    """010으로 시작하는 한국 전화번호 생성"""
    # 010-XXXX-XXXX 형식
    middle = random.randint(1000, 9999)
    last = random.randint(1000, 9999)
    return f"010-{middle}-{last}"

phone_number = generate_korean_phone()

# 가짜 이메일 주소 생성
email = fake.email()

# 가짜 생년월일 생성 (20세 이상 70세 미만)
birthdate = fake.date_of_birth(minimum_age=20, maximum_age=69)

print(f"이름: {name}")
print(f"주소: {address}")
print(f"전화번호: {phone_number}")
print(f"이메일: {email}")
print(f"생년월일: {birthdate}")
