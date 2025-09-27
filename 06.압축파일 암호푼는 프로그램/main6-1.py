import itertools
import zipfile

def crack_zip_password(zipfilename, digits=True, letters=True, max_length=9):
    """주어진 zip 파일에서 비밀번호를 찾습니다.

    zipfilename : str
        비밀번호를 찾을 zip 파일의 경로
    digits : bool (기본값 True)
        비밀번호에 숫자를 포함할 것인지 여부
    letters : bool (기본값 True)
        비밀번호에 문자를 포함할 것인지 여부
    max_length : int (기본값 9)
        비밀번호의 최대 길이

    Returns:
    str : 비밀번호
    """

    # 비밀번호 후보를 생성합니다.
    # digits와 letters 매개변수에 따라 다른 문자 집합을 사용합니다.
    chars = ""
    if digits:
        chars += "0123456789"
    if letters:
        chars += "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    passwords = itertools.chain.from_iterable(
        itertools.product(chars, repeat=i) for i in range(1, max_length + 1)
    )

    # 비밀번호를 하나씩 시도합니다.
    with zipfile.ZipFile(zipfilename) as zf:
        for password in passwords:
            password = "".join(password)
            print(password)
            try:
                zf.extractall(pwd=password.encode())
                return password
            except:
                pass

    # 비밀번호를 찾지 못한 경우 None을 반환합니다.
    return None

# 현재 디렉토리에서 암호.zip 파일을 찾습니다
import os
zip_file = "암호.zip"

if os.path.exists(zip_file):
    print(f"압축 파일을 찾았습니다: {zip_file}")
    print("비밀번호를 찾는 중... (시간이 오래 걸릴 수 있습니다)")
    password = crack_zip_password(zip_file, digits=True, letters=True, max_length=6)
    if password:
        print(f"비밀번호를 찾았습니다: {password}")
    else:
        print("비밀번호를 찾지 못했습니다.")
else:
    print(f"압축 파일을 찾을 수 없습니다: {zip_file}")
    print("현재 디렉토리의 파일들:")
    for file in os.listdir("."):
        if file.endswith(('.zip', '.ZIP')):
            print(f"  - {file}")