import pyzipper
import os

def compress_file_with_password(file_path, password):
    """파일을 암호화된 ZIP으로 압축하는 함수"""
    if not os.path.exists(file_path):
        print(f"파일을 찾을 수 없습니다: {file_path}")
        return False
    
    try:
        # read the file contents
        with open(file_path, 'rb') as f:
            data = f.read()
        
        # create a new zip file with the given name
        zip_filename = file_path + '_encrypted.zip'
        with pyzipper.AESZipFile(zip_filename, 'w', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as zip_file:
            # set password for the zip file
            zip_file.setpassword(password.encode('utf-8'))
            # write the file to the zip file
            zip_file.writestr(os.path.basename(file_path), data)
        
        print(f"암호화 압축 완료: {zip_filename}")
        print(f"비밀번호: {password}")
        return True
        
    except Exception as e:
        print(f"압축 중 오류 발생: {e}")
        return False

if __name__ == '__main__':
    # 현재 디렉토리에서 압축할 파일 찾기
    target_file = "압축.txt"
    password = "1234"
    
    if os.path.exists(target_file):
        print(f"압축할 파일을 찾았습니다: {target_file}")
        compress_file_with_password(target_file, password)
    else:
        print(f"압축할 파일을 찾을 수 없습니다: {target_file}")
        print("현재 디렉토리의 텍스트 파일들:")
        for file in os.listdir("."):
            if file.endswith('.txt'):
                print(f"  - {file}")
                # 첫 번째 텍스트 파일을 암호화 압축
                compress_file_with_password(file, password)
                break
