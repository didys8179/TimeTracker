
from datetime import datetime


class TimeTracker:

# 시간에 대해 빈 공간값은 '00이 아닌 None으로!
    def __init__(self):
        self.start_time = None
        self.endtime = None
        self.elapsed_time = None

    def start(self):
        self.start_time = datetime.now()
        print(f'시작시간: {self.start_time}')

    def stop(self):
        self.end_time = datetime.now()
        print(f'종료시간: {self.end_time}')

    def get_elapsed_time(self):
        elapsed_time = self.end_time - self.start_time
        elapsed_time = elapsed_time.total_seconds()/60
        return round(elapsed_time, 2)


# 사용 예시
if __name__ == "__main__":
    tracker = TimeTracker()
    tracker.start()

    # # 여기서 실제로 시간을 지연시키려면 time.sleep()을 사용할 수 있지만, 코드 실행을 바로 확인하기 위해 주석 처리함
    import time
    time.sleep(10)  # 10초 대기

    tracker.stop()
    print(f"공부한 시간: {tracker.get_elapsed_time()} 분")
