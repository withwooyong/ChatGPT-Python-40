import qrcode
import os

# 데이터가 저장된 파일 경로 (현재 디렉토리)
file_path = "qrdata.txt"

# QR 코드 생성 함수
def create_qrcode(data):
    # QR 코드 생성
    img = qrcode.make(data)

    # 파일명에 사용할 수 없는 문자 제거
    safe_filename = "".join(c for c in data if c.isalnum() or c in (' ', '-', '_')).rstrip()
    safe_filename = safe_filename.replace(' ', '_')[:20]  # 길이 제한

    # 이미지 파일로 저장 (현재 디렉토리)
    img_file_path = f"qrcode_{safe_filename}.png"
    img.save(img_file_path)
    print(f"QR코드 생성 완료: {img_file_path}")

# qrdata.txt 파일에서 데이터 읽어오기
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # 개행 문자 제거
            data = line.strip()
            if data:  # 빈 줄이 아닌 경우만 처리
                create_qrcode(data)
    print("모든 QR코드 생성이 완료되었습니다!")
except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다: {file_path}")
except Exception as e:
    print(f"오류가 발생했습니다: {e}")
