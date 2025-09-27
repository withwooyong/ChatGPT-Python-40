import qrcode
import os

# QR 코드에 넣을 데이터
data = "Hello, Ted!"

# QR 코드 생성
img = qrcode.make(data)

# 이미지 파일로 저장 (현재 디렉토리에 저장)
file_path = "qrcode_hello_world.png"
img.save(file_path)

print(f"QR코드가 생성되었습니다: {file_path}")
