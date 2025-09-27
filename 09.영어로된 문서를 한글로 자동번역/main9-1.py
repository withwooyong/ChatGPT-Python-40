from deep_translator import GoogleTranslator
import os

def translate_file(input_file, output_file):
    """영어 파일을 한글로 번역하는 함수"""
    try:
        # 파일 읽기
        with open(input_file, "r", encoding="utf-8") as input_file_handle:
            text = input_file_handle.read()
        
        print(f"원본 파일을 읽었습니다: {input_file}")
        print(f"번역 중... (텍스트 길이: {len(text)} 문자)")
        
        # 번역 (Google Translate 사용)
        translator = GoogleTranslator(source='auto', target='ko')
        translated_text = translator.translate(text)
        
        # 번역된 결과를 파일에 쓰기
        with open(output_file, "w", encoding="utf-8") as output_file_handle:
            output_file_handle.write(translated_text)
        
        print(f"번역 완료: {output_file}")
        print(f"번역된 텍스트 미리보기: {translated_text[:100]}...")
        return True
        
    except Exception as e:
        print(f"번역 중 오류 발생: {e}")
        return False

if __name__ == "__main__":
    # 현재 디렉토리에서 번역할 파일 찾기
    input_file = "영어문서.txt"
    output_file = "한글번역.txt"
    
    if os.path.exists(input_file):
        print(f"번역할 파일을 찾았습니다: {input_file}")
        translate_file(input_file, output_file)
    else:
        print(f"번역할 파일을 찾을 수 없습니다: {input_file}")
        print("현재 디렉토리의 텍스트 파일들:")
        for file in os.listdir("."):
            if file.endswith('.txt'):
                print(f"  - {file}")
                # 첫 번째 텍스트 파일을 번역
                output_name = file.replace('.txt', '_한글번역.txt')
                translate_file(file, output_name)
                break
