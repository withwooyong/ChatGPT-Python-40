import zipfile
import os

def compress_file(file_path):
    """파일을 압축하는 함수"""
    if not os.path.exists(file_path):
        print(f"파일을 찾을 수 없습니다: {file_path}")
        return False
    
    zip_filename = file_path + '.zip'
    try:
        with zipfile.ZipFile(zip_filename, 'w') as zip_file:
            zip_file.write(file_path)
        print(f"압축 완료: {zip_filename}")
        return True
    except Exception as e:
        print(f"압축 중 오류 발생: {e}")
        return False

if __name__ == '__main__':
    # 현재 디렉토리에서 압축할 파일 찾기
    target_file = "압축.txt"
    
    if os.path.exists(target_file):
        print(f"압축할 파일을 찾았습니다: {target_file}")
        compress_file(target_file)
    else:
        print(f"압축할 파일을 찾을 수 없습니다: {target_file}")
        print("현재 디렉토리의 텍스트 파일들:")
        for file in os.listdir("."):
            if file.endswith('.txt'):
                print(f"  - {file}")
                # 첫 번째 텍스트 파일을 압축
                compress_file(file)
                break