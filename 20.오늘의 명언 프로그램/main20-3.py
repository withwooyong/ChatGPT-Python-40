import random
import time
from datetime import datetime

# 명언 리스트 생성
sayings = [
    "노력하는 것만이 성공으로 이끄는 길이다. - 니키 라우드",
    "삶이 있는 한 희망은 있다. - 키케로",
    "오늘을 낭비하지 마라. 어제의 후회와 내일의 불안에 가로막혀 오늘을 놓치고 있다. - 에머슨",
    "문제점을 찾지 말고 해결책을 찾으라. - 헨리포드",
    "사람은 자신이 믿는 대로 된다. - 괴테",
    "지식은 인생을 바꾼다. - 윌리엄 제임스",
    "지금까지 당신이 살아온 모든 날들의 합이 오늘이라면, 오늘하루를 잘 살아야 합니다. - 괴테",
    "한번의 실패와 영원한 실패를 혼동하지 마라. - F.스콧 핏제랄드",
    "당신이 할 수 있다고 믿든 할 수 없다고 믿든 믿는 대로 될 것이다. - 헨리 포드",
    "성공한 사람을 보면 마치 그들이 실패한 적이 없는 것처럼 보이지만, 많은 실패들을 겪고 다시 일어난 것이다. - 왈트 디즈니",
]

def show_quote():
    """명언을 화면에 표시하는 함수"""
    saying = random.choice(sayings)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"\n{'='*60}")
    print(f"📢 오늘의 명언 - {current_time}")
    print(f"{'='*60}")
    print(f"💭 {saying}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    print("명언 프로그램을 시작합니다...")
    print("Ctrl+C를 눌러 종료할 수 있습니다.\n")
    
    try:
        while True:
            show_quote()
            # 1시간 대기 (테스트를 위해 10초로 변경)
            time.sleep(10)
    except KeyboardInterrupt:
        print("\n프로그램을 종료합니다. 좋은 하루 되세요! 🌟")
