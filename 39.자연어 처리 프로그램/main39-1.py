import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.tag import pos_tag
from collections import Counter
import re

# NLTK 데이터 다운로드
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
    print("NLTK 데이터 다운로드 완료")
except:
    print("NLTK 데이터 다운로드 중 오류 발생")

def preprocess_korean(text):
    """한국어 텍스트 전처리"""
    # 특수문자 제거 (한글, 영문, 숫자, 공백만 유지)
    text = re.sub(r'[^가-힣a-zA-Z0-9\s]', ' ', text)
    # 여러 공백을 하나로 변환
    text = re.sub(r'\s+', ' ', text).strip()
    # 소문자로 변환
    text = text.lower()
    return text

def preprocess_english(text):
    """영어 텍스트 전처리"""
    text = text.lower()
    words = word_tokenize(text)
    words = [word for word in words if word.isalpha()]
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if not word in stop_words]
    return words

def analyze_text(text):
    """텍스트 분석"""
    print(f"원본 텍스트: {text}")
    print("-" * 50)
    
    # 한국어와 영어 구분
    korean_chars = len(re.findall(r'[가-힣]', text))
    english_chars = len(re.findall(r'[a-zA-Z]', text))
    
    # 문장 분리 (언어에 따라 다르게 처리)
    try:
        if korean_chars > english_chars:
            # 한국어 문장 분리 (간단한 방법)
            sentences = re.split(r'[.!?]+', text)
            sentences = [s.strip() for s in sentences if s.strip()]
        else:
            # 영어 문장 분리
            sentences = sent_tokenize(text)
        print(f"문장 수: {len(sentences)}")
    except Exception as e:
        print(f"문장 분리 오류: {e}")
        sentences = [text]
        print(f"문장 수: {len(sentences)}")
    
    if korean_chars > english_chars:
        print("주요 언어: 한국어")
        processed_text = preprocess_korean(text)
        words = processed_text.split()
    else:
        print("주요 언어: 영어")
        words = preprocess_english(text)
    
    print(f"단어 수: {len(words)}")
    
    # 단어 빈도수 계산
    word_counts = Counter(words)
    top_words = word_counts.most_common(10)
    
    print("\n상위 10개 단어:")
    for word, count in top_words:
        print(f"  {word}: {count}회")
    
    # 영어 단어가 있는 경우 품사 태깅
    if english_chars > 0:
        try:
            english_words = [word for word in words if re.match(r'^[a-zA-Z]+$', word)]
            if english_words:
                tagged_words = pos_tag(english_words)
                print(f"\n영어 단어 품사 태깅 (처음 10개):")
                for word, tag in tagged_words[:10]:
                    print(f"  {word}: {tag}")
        except Exception as e:
            print(f"품사 태깅 오류: {e}")
    
    return {
        'sentences': len(sentences),
        'words': len(words),
        'top_words': top_words,
        'is_korean': korean_chars > english_chars
    }

def main():
    print("자연어 처리 프로그램")
    print("=" * 50)
    
    # 테스트용 텍스트들
    test_texts = [
        "안녕하세요. 파이썬으로 자연어 처리를 배우고 있습니다. 정말 재미있어요!",
        "Hello world! This is a natural language processing program. It's very interesting.",
        "파이썬과 NLTK를 사용하여 텍스트를 분석합니다. Python is great for NLP!"
    ]
    
    print("테스트 텍스트들:")
    for i, text in enumerate(test_texts, 1):
        print(f"\n--- 테스트 {i} ---")
        analyze_text(text)
        print()
    
    # 사용자 입력 받기
    print("직접 텍스트를 입력해보세요 (Enter로 종료):")
    while True:
        try:
            user_text = input("\n텍스트 입력: ").strip()
            if not user_text:
                break
            analyze_text(user_text)
        except KeyboardInterrupt:
            print("\n프로그램을 종료합니다.")
            break
        except Exception as e:
            print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()
