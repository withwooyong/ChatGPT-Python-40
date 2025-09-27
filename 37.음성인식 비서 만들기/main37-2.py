import speech_recognition as sr
import webbrowser
import time
import os

def voice_assistant():
    # 음성인식을 위한 객체 생성
    r = sr.Recognizer()
    
    try:
        # 음성 입력 받기
        with sr.Microphone() as source:
            print("마이크를 조정하고 있습니다...")
            r.adjust_for_ambient_noise(source, duration=1)
            print("말씀하세요... (3초 후 녹음 시작)")
            time.sleep(3)
            print("🎤 녹음 중...")
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        
        # 음성 인식
        print("음성을 인식하고 있습니다...")
        text = r.recognize_google(audio, language='ko-KR')
        print(f"인식된 음성: {text}")
        
        # 음성 명령에 따라 동작 수행
        text_lower = text.lower()
        
        if "구글" in text_lower or "google" in text_lower:
            print("구글을 열고 있습니다...")
            webbrowser.open("https://www.google.com")
            
        elif "유튜브" in text_lower or "youtube" in text_lower:
            print("유튜브를 열고 있습니다...")
            webbrowser.open("https://www.youtube.com")
            
        elif "검색" in text_lower:
            query = text.split("검색")[1].strip()
            if query:
                print(f"'{query}'를 검색하고 있습니다...")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                print("검색할 내용을 말씀해주세요.")
                
        elif "날씨" in text_lower:
            print("날씨 정보를 검색하고 있습니다...")
            webbrowser.open("https://www.google.com/search?q=날씨")
            
        elif "뉴스" in text_lower:
            print("뉴스를 검색하고 있습니다...")
            webbrowser.open("https://www.google.com/search?q=뉴스")
            
        elif "종료" in text_lower or "끝" in text_lower:
            print("음성 비서를 종료합니다.")
            return False
            
        else:
            print("해당 명령을 이해할 수 없습니다.")
            print("사용 가능한 명령: 구글, 유튜브, 검색, 날씨, 뉴스, 종료")
            
        return True
        
    except sr.WaitTimeoutError:
        print("시간이 초과되었습니다. 다시 시도해주세요.")
        return True
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다. 다시 말씀해주세요.")
        return True
    except sr.RequestError as e:
        print(f"음성 인식 서비스 오류: {e}")
        return True
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
        return True

if __name__ == "__main__":
    print("🎤 음성 비서를 시작합니다!")
    print("사용 가능한 명령: 구글, 유튜브, 검색, 날씨, 뉴스, 종료")
    print("프로그램을 종료하려면 Ctrl+C를 누르세요.")
    print("-" * 50)
    
    try:
        while True:
            if not voice_assistant():
                break
            print("-" * 50)
            
    except KeyboardInterrupt:
        print("\n음성 비서를 종료합니다.")
