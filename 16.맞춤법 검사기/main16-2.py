from pykospacing import Spacing

# 맞춤법 검사를 수행할 파일 경로를 지정합니다.
input_path = "틀린맞춤법.txt"
# 수정된 맞춤법을 저장할 파일 경로를 지정합니다.
output_path = "수정맞춤법.txt"

# 맞춤법 검사를 수행하는 함수를 정의합니다.
def correct_spelling(text):
    try:
        # PyKoSpacing 라이브러리를 사용하여 띄어쓰기를 보정합니다.
        spacing = Spacing()
        corrected_text = spacing(text)
        
        # 일반적인 맞춤법 오류를 수정합니다.
        corrections = {
            '외 안 되': '왜 안 돼',
            '오랫만에': '오랜만에',
            '안으면 않된다': '안 하면 안 된다',
            '안되': '안 돼',
            '않된다': '안 된다',
            '안되요': '안 돼요',
            '안되나': '안 되나',
            '안되네': '안 되네',
            '안되다': '안 되다',
            '안되지': '안 되지',
            '안되죠': '안 되죠',
            '안되니까': '안 되니까',
            '안되면': '안 되면',
            '안되서': '안 되어서',
            '안되지만': '안 되지만',
            '안되도록': '안 되도록',
            '안되게': '안 되게',
            '안되기': '안 되기',
            '안되다가': '안 되다가',
            '안되던': '안 되던',
            '안되든': '안 되든',
            '안되든지': '안 되든지',
            '안되라': '안 되라',
            '안되라고': '안 되라고',
            '안되면': '안 되면',
            '안되니까': '안 되니까',
            '안되서': '안 되어서',
            '안되지만': '안 되지만',
            '안되도록': '안 되도록',
            '안되게': '안 되게',
            '안되기': '안 되기',
            '안되다가': '안 되다가',
            '안되던': '안 되던',
            '안되든': '안 되든',
            '안되든지': '안 되든지',
            '안되라': '안 되라',
            '안되라고': '안 되라고'
        }
        
        # 맞춤법 교정 적용
        for wrong, correct in corrections.items():
            corrected_text = corrected_text.replace(wrong, correct)
        
        return corrected_text
    except Exception as e:
        print(f"오류 발생: {e}")
        return text

# 입력 파일을 읽어서 맞춤법을 보정한 뒤 출력 파일에 저장합니다.
with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()
    corrected_text = correct_spelling(text)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(corrected_text)

print(f"맞춤법 검사가 완료되었습니다. 수정된 파일은 {output_path}에 저장되었습니다.")
print(corrected_text)
