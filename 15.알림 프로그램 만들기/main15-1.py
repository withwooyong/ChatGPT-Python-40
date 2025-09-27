import subprocess
import time

def show_notification(title, message):
    """macOS에서 알림을 표시하는 함수"""
    try:
        # osascript를 사용하여 macOS 알림 표시
        script = f'''
        display notification "{message}" with title "{title}"
        '''
        subprocess.run(['osascript', '-e', script], check=True)
        print(f"알림 전송: {title} - {message}")
    except subprocess.CalledProcessError as e:
        print(f"알림 전송 실패: {e}")

# 간단한 알림
show_notification("알림 프로그램", "안녕하세요! 이것은 알림 메시지입니다.")