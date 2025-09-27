from datetime import datetime, timedelta
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

print("알림 프로그램이 시작되었습니다. (월, 수, 금 오전 9시 50분에 회의 알림)")
print("종료하려면 Ctrl+C를 누르세요.")

try:
    while True:
        now = datetime.now()
        if now.weekday() in [0, 2, 4] and now.hour == 9 and now.minute == 50:
            # 다음 회의 시작 시간 계산
            next_meeting_time = now + timedelta(minutes=10)
            next_meeting_time_str = next_meeting_time.strftime("%Y-%m-%d %H:%M:%S")

            # 알림 표시
            show_notification("회의 알림", f"{next_meeting_time_str}에 회의가 시작됩니다.")

        # 1초마다 반복
        time.sleep(1)
        
except KeyboardInterrupt:
    print("\n알림 프로그램이 종료되었습니다.")
