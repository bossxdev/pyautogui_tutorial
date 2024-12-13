import pyautogui
import time
import cv2
import numpy as np
import os

from src.utils.utility_func import get_image_path


def check_image_existence(image_path):
    """
    ฟังก์ชันตรวจสอบว่าไฟล์ภาพสามารถเปิดได้หรือไม่
    """
    image = cv2.imread(image_path)
    if image is None:
        print("ไม่สามารถอ่านไฟล์ภาพได้ อาจเกิดจากไฟล์เสียหายหรือไม่รองรับ")
        return False
    else:
        print("ไฟล์ภาพเปิดได้สำเร็จ")
        return True


def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกฟอร์ม หรือจำลองการทำงาน
    """
    print("เริ่มการทดสอบ...")

    try:
        # คลิกปุ่มกรอกบางโค้ด
        pyautogui.moveTo(740, 149, duration=0.5)  # เพิ่มเวลาในการเคลื่อนที่
        pyautogui.click(button="left")
        time.sleep(5)

        # กรอกรหัสบาร์โค้ด
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        pyautogui.write("010753700137401")
        time.sleep(3)
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        pyautogui.write("123456789")
        time.sleep(3)
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        pyautogui.write("1234567893434")
        time.sleep(3)
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        pyautogui.write("30000")
        pyautogui.press('enter')
        time.sleep(10)

        # ตรวจสอบการแสดงผลภายใน 20 วินาที
        start_time = time.time()
        timeout = 20  # เวลารอสูงสุด 20 วินาที
        image_path = get_image_path(os.path.dirname(__file__), 'EDC.png')

        if not check_image_existence(image_path):
            return  # หากไฟล์ภาพไม่สามารถเปิดได้ ให้หยุดการทำงาน

        while time.time() - start_time < timeout:
            print("กำลังตรวจสอบภาพหน้าจอ...")
            try:
                # ใช้ pyautogui.locateOnScreen เพื่อจับภาพหน้าจอและตรวจสอบ
                if pyautogui.locateOnScreen(image_path, confidence=0.8):  # เพิ่มค่าความมั่นใจหรือลดให้เหมาะสม
                    print("หน้าจอแสดงให้กรอกเบอร์โทรแล้ว")
                    break
            except Exception as e:
                print(f"เกิดข้อผิดพลาดในการจับภาพหน้าจอ: {e}")
                return

            time.sleep(1)

        else:
            # หากหมดเวลา 20 วินาทีโดยไม่มีการแสดงผล
            print("ข้อมูลไม่ถูกต้อง หรือหน้าจอไม่แสดงผลลัพธ์ที่คาดหวัง")
            return  # หยุดการทำงานของโปรแกรม

    except Exception as e:
        print(f"เกิดข้อผิดพลาดในฟังก์ชัน run_test_case: {e}")


# เรียกใช้งานฟังก์ชัน
run_test_case()
