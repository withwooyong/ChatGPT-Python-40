import os
import shutil
import datetime

source_dir = '원본폴더' # 복사할 폴더의 경로
target_dir = '백업폴더' # 복사될 대상 폴더의 경로

# 원본 폴더가 존재하는지 확인
if not os.path.exists(source_dir):
    print(f"오류: 원본 폴더 '{source_dir}'가 존재하지 않습니다.")
    exit(1)

# 백업 폴더가 이미 존재하는 경우 타임스탬프 추가
if os.path.exists(target_dir):
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    target_dir = f"{target_dir}_{timestamp}"

# 대상 폴더 생성
os.makedirs(target_dir, exist_ok=True)

try:
    # 폴더 전체 복사
    shutil.copytree(source_dir, target_dir, dirs_exist_ok=True)
    print(f"백업이 완료되었습니다!")
    print(f"원본: {source_dir}")
    print(f"백업: {target_dir}")
except Exception as e:
    print(f"백업 중 오류가 발생했습니다: {e}")
