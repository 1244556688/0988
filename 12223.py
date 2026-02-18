import time
import random
import sys

PASSWORD = "justin"
buffer = ""

lines = [
    "系統錯誤。",
    "你為什麼還在這裡？",
    "你不是已經想關掉了嗎。",
    "手機在你手上。",
    "但你沒有離開。",
    "想關嗎？",
    "不給你關。",
]

def slow_print(text):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.04)
    print()

try:
    slow_print("正在收集錯誤資訊…")
    time.sleep(1)

    while True:
        slow_print(random.choice(lines))
        time.sleep(random.uniform(0.8, 1.6))

        user = input("> ").lower()
        buffer += user

        if PASSWORD in buffer:
            slow_print("……")
            slow_print("你知道那個字。")
            slow_print("這次放你走。")
            break

except KeyboardInterrupt:
    print("\n你逃走了。")

