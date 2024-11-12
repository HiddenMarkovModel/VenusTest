import time
import argparse

def main(duration_minutes):
    duration_seconds = duration_minutes * 60  # 将分钟转换为秒
    start_time = time.time()
    
    while time.time() - start_time < duration_seconds:
        print(1)
        time.sleep(1)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="持续输出数字1，指定执行时间（分钟）")
    parser.add_argument("--duration", type=int, required=True, help="执行时间，单位：分钟")
    args = parser.parse_args()
    
    main(args.duration)
