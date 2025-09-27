from gtts import gTTS
import os
import sys

# 텍스트를 입력받습니다.
text = input('텍스트를 입력하세요: ')

# 한국어로 음성을 출력하도록 설정합니다.
tts = gTTS(text, lang='ko')

# 음성을 mp3 파일로 저장합니다.
tts.save('output.mp3')

print("음성 파일이 생성되었습니다: output.mp3")

# 시스템 기본 플레이어로 재생
if sys.platform == "darwin":  # macOS
    print("macOS에서 음성을 재생합니다...")
    os.system("afplay output.mp3")
elif sys.platform == "win32":  # Windows
    print("Windows에서 음성을 재생합니다...")
    os.system("start output.mp3")
else:  # Linux
    print("Linux에서 음성을 재생합니다...")
    os.system("mpg123 output.mp3 || mplayer output.mp3 || vlc output.mp3")

print("재생이 완료되었습니다.")

# 재생 완료 후 임시 파일 삭제 (선택사항)
# os.remove('output.mp3')