from pykospacing import Spacing

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
            '안되라고': '안 되라고'
        }
        
        # 맞춤법 교정 적용
        for wrong, correct in corrections.items():
            corrected_text = corrected_text.replace(wrong, correct)
        
        return corrected_text
    except Exception as e:
        print(f"오류 발생: {e}")
        return text

# 맞춤법 검사를 수행할 문장을 입력합니다.
sentence = "외안되요오랫만에만났어요안하면안된다고했는데"  # 복합 맞춤법 오류 테스트 문장
print(f'원본 문장: {sentence}')
checked_sentence = correct_spelling(sentence)
print('검사 결과:', checked_sentence)

