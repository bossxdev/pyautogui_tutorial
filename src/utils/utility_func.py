import pyautogui
import time
import os


def log_action(action, details):
    print(f"[LOG] {action}: {details}")


def click(position, delay=2, button="left", description=""):
    try:
        log_action("Click", f"ตำแหน่ง {position} {description}")
        pyautogui.click(*position, button=button)
        time.sleep(delay)
    except Exception as e:
        log_action("Error", f"เกิดข้อผิดพลาดในการคลิกตำแหน่ง {position}: {e}")
        raise


def write_text(text, delay=2, description=""):
    try:
        log_action("Write", f"พิมพ์ข้อความ: {text} {description}")
        pyautogui.write(text)
        time.sleep(delay)
    except Exception as e:
        log_action("Error", f"เกิดข้อผิดพลาดในการพิมพ์ข้อความ {text}: {e}")
        raise


def get_image_path(current_dir, image_name=""):
    return os.path.join(current_dir, image_name)
