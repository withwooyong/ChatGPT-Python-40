import psutil
import time
import os

def clear_screen():
    """화면을 지웁니다."""
    os.system('cls' if os.name == 'nt' else 'clear')

def format_bytes(bytes_value):
    """바이트를 읽기 쉬운 형태로 변환합니다."""
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.1f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.1f} PB"

def get_system_info():
    """시스템 정보를 가져옵니다."""
    # CPU 사용량
    cpu_percent = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count()
    
    # 메모리 정보
    mem = psutil.virtual_memory()
    mem_total = format_bytes(mem.total)
    mem_used = format_bytes(mem.used)
    mem_available = format_bytes(mem.available)
    mem_percent = mem.percent
    
    # 디스크 정보
    disk = psutil.disk_usage('/')
    disk_total = format_bytes(disk.total)
    disk_used = format_bytes(disk.used)
    disk_free = format_bytes(disk.free)
    disk_percent = (disk.used / disk.total) * 100
    
    # 네트워크 정보
    net_io = psutil.net_io_counters()
    
    return {
        'cpu_percent': cpu_percent,
        'cpu_count': cpu_count,
        'mem_total': mem_total,
        'mem_used': mem_used,
        'mem_available': mem_available,
        'mem_percent': mem_percent,
        'disk_total': disk_total,
        'disk_used': disk_used,
        'disk_free': disk_free,
        'disk_percent': disk_percent,
        'net_bytes_sent': format_bytes(net_io.bytes_sent),
        'net_bytes_recv': format_bytes(net_io.bytes_recv)
    }

def display_system_info():
    """시스템 정보를 화면에 표시합니다."""
    info = get_system_info()
    
    print("=" * 60)
    print("🖥️  시스템 모니터 (Ctrl+C로 종료)")
    print("=" * 60)
    print(f"💻 CPU 사용량: {info['cpu_percent']:6.1f}% ({info['cpu_count']} 코어)")
    print(f"🧠 메모리 사용량: {info['mem_percent']:6.1f}%")
    print(f"   총 메모리: {info['mem_total']:>10} | 사용: {info['mem_used']:>10} | 여유: {info['mem_available']:>10}")
    print(f"💾 디스크 사용량: {info['disk_percent']:6.1f}%")
    print(f"   총 용량: {info['disk_total']:>10} | 사용: {info['disk_used']:>10} | 여유: {info['disk_free']:>10}")
    print(f"🌐 네트워크: 송신 {info['net_bytes_sent']:>10} | 수신 {info['net_bytes_recv']:>10}")
    print("=" * 60)

def main():
    """메인 함수"""
    print("시스템 모니터를 시작합니다...")
    print("Ctrl+C를 눌러 종료하세요.")
    time.sleep(2)
    
    try:
        while True:
            clear_screen()
            display_system_info()
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n시스템 모니터를 종료합니다.")
        print("감사합니다! 👋")

if __name__ == "__main__":
    main()
