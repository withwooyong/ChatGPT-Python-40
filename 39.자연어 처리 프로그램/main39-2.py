from konlpy.tag import Komoran, Okt, Kkma
import time

def analyze_korean_text(text, analyzer_name='komoran'):
    """한국어 텍스트 형태소 분석"""
    print(f"원본 텍스트: {text}")
    print("-" * 50)
    
    try:
        if analyzer_name == 'komoran':
            analyzer = Komoran()
            print("사용된 분석기: Komoran")
        elif analyzer_name == 'okt':
            analyzer = Okt()
            print("사용된 분석기: Okt (Open Korean Text)")
        elif analyzer_name == 'kkma':
            analyzer = Kkma()
            print("사용된 분석기: Kkma (꼬꼬마)")
        else:
            print("지원되지 않는 분석기입니다.")
            return
        
        # 형태소 분석 및 품사 태깅
        start_time = time.time()
        words = analyzer.pos(text)
        end_time = time.time()
        
        print(f"분석 시간: {end_time - start_time:.3f}초")
        print(f"총 형태소 수: {len(words)}")
        print("\n형태소 분석 결과:")
        print("-" * 30)
        
        # 품사별 그룹화
        pos_groups = {}
        for word, pos in words:
            if pos not in pos_groups:
                pos_groups[pos] = []
            pos_groups[pos].append(word)
        
        # 결과 출력
        for word, pos in words:
            print(f"{word:10} ({pos})")
        
        print("\n품사별 단어 분류:")
        print("-" * 30)
        for pos, words_list in pos_groups.items():
            print(f"{pos}: {', '.join(words_list)}")
        
        return words
        
    except Exception as e:
        print(f"형태소 분석 중 오류 발생: {e}")
        return None

def compare_analyzers(text):
    """여러 분석기 비교"""
    print("=" * 60)
    print("한국어 형태소 분석기 비교")
    print("=" * 60)
    
    analyzers = ['komoran', 'okt', 'kkma']
    
    for analyzer_name in analyzers:
        print(f"\n{'='*20} {analyzer_name.upper()} {'='*20}")
        analyze_korean_text(text, analyzer_name)
        print()

def main():
    print("한국어 형태소 분석 프로그램")
    print("=" * 50)
    
    # 테스트용 텍스트들
    test_texts = [
        "오늘은 날씨가 좋아서 산책을 하고 싶습니다.",
        "파이썬으로 자연어 처리를 배우고 있어요.",
        "안녕하세요! 반갑습니다. 오늘 하루도 화이팅!",
        "머신러닝과 딥러닝은 정말 흥미로운 분야입니다."
    ]
    
    print("테스트 텍스트들:")
    for i, text in enumerate(test_texts, 1):
        print(f"\n--- 테스트 {i} ---")
        analyze_korean_text(text)
        print()
    
    # 분석기 비교
    print("\n" + "="*60)
    print("분석기 비교 (첫 번째 텍스트로)")
    compare_analyzers(test_texts[0])
    
    # 사용자 입력 받기
    print("직접 텍스트를 입력해보세요 (Enter로 종료):")
    while True:
        try:
            user_text = input("\n한국어 텍스트 입력: ").strip()
            if not user_text:
                break
            
            print("\n어떤 분석기를 사용하시겠습니까?")
            print("1. Komoran (기본)")
            print("2. Okt")
            print("3. Kkma")
            print("4. 모든 분석기 비교")
            
            choice = input("선택 (1-4): ").strip()
            
            if choice == '1':
                analyze_korean_text(user_text, 'komoran')
            elif choice == '2':
                analyze_korean_text(user_text, 'okt')
            elif choice == '3':
                analyze_korean_text(user_text, 'kkma')
            elif choice == '4':
                compare_analyzers(user_text)
            else:
                print("잘못된 선택입니다. Komoran으로 분석합니다.")
                analyze_korean_text(user_text, 'komoran')
                
        except KeyboardInterrupt:
            print("\n프로그램을 종료합니다.")
            break
        except Exception as e:
            print(f"오류 발생: {e}")

if __name__ == "__main__":
    main()
