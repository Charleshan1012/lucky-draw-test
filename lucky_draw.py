import json
import random
import os
from datetime import datetime

# 历史记录文件
HISTORY_FILE = "data/history.json"

# 生成大乐透号码 (5+2)
def generate_lottery():
    red_balls = random.sample(range(1, 36), 5)  # 5个红球（1-35）
    blue_balls = random.sample(range(1, 13), 2)  # 2个蓝球（1-12）
    return sorted(red_balls), sorted(blue_balls)

# 生成双色球号码 (6+1)
def generate_double_color():
    red_balls = random.sample(range(1, 34), 6)  # 6个红球（1-33）
    blue_ball = random.randint(1, 16)  # 1个蓝球（1-16）
    return sorted(red_balls), blue_ball

# 记录历史
def save_to_history(lottery_type, numbers):
    history = []
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            history = json.load(f)

    history.append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "type": lottery_type,
        "numbers": numbers
    })

    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=4)

# 读取历史记录
def load_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            return json.load(f)
    return []

# 主程序
def main():
    print("🎲 LuckyDraw Helper 🎲")
    print("1. 生成大乐透号码 (5+2)")
    print("2. 生成双色球号码 (6+1)")
    print("3. 查看历史记录")
    choice = input("请选择 (1/2/3)：")

    if choice == "1":
        numbers = generate_lottery()
        print(f"🎉 大乐透号码：{numbers[0]} + {numbers[1]}")
        save_to_history("大乐透", numbers)

    elif choice == "2":
        numbers = generate_double_color()
        print(f"🎉 双色球号码：{numbers[0]} + [{numbers[1]}]")
        save_to_history("双色球", numbers)

    elif choice == "3":
        history = load_history()
        if not history:
            print("📜 还没有历史记录！")
        else:
            for entry in history:
                print(f"{entry['date']} | {entry['type']} : {entry['numbers']}")

    else:
        print("❌ 选择错误，请重新运行程序。")

if __name__ == "__main__":
    main()