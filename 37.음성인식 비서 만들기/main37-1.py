# pip install SpeechRecognition pyaudio

import speech_recognition as sr
import time

def voice_recognition():
    # 음성 인식기 초기화
    r = sr.Recognizer()
    
    try:
        # 마이크에서 음성을 받아들입니다.
        with sr.Microphone() as source:
            print("마이크를 조정하고 있습니다... 잠시만 기다려주세요.")
            r.adjust_for_ambient_noise(source, duration=1)
            print("말씀해주세요. (3초 후 녹음 시작)")
            time.sleep(3)
            print("🎤 녹음 중...")
            audio = r.listen(source, timeout=5, phrase_time_limit=10)
        
        # 인식된 음성에서 텍스트를 추출합니다.
        print("음성을 인식하고 있습니다...")
        text = r.recognize_google(audio, language='ko-KR')
        
        print(f"인식된 텍스트: {text}")
        return text
        
    except sr.WaitTimeoutError:
        print("시간이 초과되었습니다. 다시 시도해주세요.")
        return None
    except sr.UnknownValueError:
        print("음성을 인식할 수 없습니다. 다시 말씀해주세요.")
        return None
    except sr.RequestError as e:
        print(f"음성 인식 서비스 오류: {e}")
        return None
    except Exception as e:
        print(f"오류가 발생했습니다: {e}")
        return None

if __name__ == "__main__":
    print("음성 인식 프로그램을 시작합니다.")
    print("프로그램을 종료하려면 Ctrl+C를 누르세요.")
    
    try:
        while True:
            result = voice_recognition()
            if result:
                print(f"결과: {result}")
            print("-" * 50)
            
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다.")
