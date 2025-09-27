import pytesseract
from PIL import Image
import os

# macOS에서 Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

# 이미지 불러오기
image_path = 'img.png'
if not os.path.exists(image_path):
    print(f"오류: 이미지 파일 '{image_path}'를 찾을 수 없습니다.")
    exit(1)

image = Image.open(image_path)

# 이미지에서 텍스트 추출 (한국어 + 영어)
try:
    text = pytesseract.image_to_string(image, lang='kor+eng')
    print("추출된 텍스트:")
    print("-" * 40)
    print(text)
    print("-" * 40)
except Exception as e:
    print(f"텍스트 추출 중 오류가 발생했습니다: {e}")
    print("한국어 언어팩이 설치되지 않았을 수 있습니다.")
    print("영어로만 추출을 시도합니다...")
    try:
        text = pytesseract.image_to_string(image, lang='eng')
        print("추출된 텍스트 (영어):")
        print("-" * 40)
        print(text)
        print("-" * 40)
    except Exception as e2:
        print(f"영어 추출도 실패했습니다: {e2}")
