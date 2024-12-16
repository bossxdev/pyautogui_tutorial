import pyautogui
import time
import cv2
import numpy as np
from src.utils.utility_func import log_action,write_text,click # Assuming log_action is available

def main():
    """
    ฟังก์ชันหลักที่ใช้ในการควบคุมการทำงานของ Automated Test
    """
    try:
        # 1. การตั้งค่าเบื้องต้น
        setup_environment()

        # 2. ขั้นตอนการทดสอบ
        run_test_case()

    except Exception as e:
        log_action("Error", f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")

def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าการทดสอบ เช่น เปิดแอปพลิเคชันหรือเตรียมหน้าต่าง
    """
    print("เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    print("การตั้งค่าเสร็จสิ้น")

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
        click((740, 149), delay=5, description="คลิกปุ่มกรอกบาร์โค้ด")

        # กรอกรหัสบาร์โค้ด
        log_action("Write", "พิมพ์บาร์โค้ด")
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("010753700137401", delay=3, description="กรอกบาร์โค้ด 1")

        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("123456789", delay=3, description="กรอกบาร์โค้ด 2")

        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("1234567893434", delay=3, description="กรอกบาร์โค้ด 3")

        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("30000", delay=3, description="กรอกบาร์โค้ด 4")
        
        pyautogui.press('enter')
        time.sleep(10)

        # ตรวจสอบการแสดงผลภายใน 20 วินาที
        start_time = time.time()
        timeout = 20  # เวลารอสูงสุด 20 วินาที
        image_path = 'C:/Users/himma/Automatetest/pyautogui_tutorial/src/10014/Screenshot 2024-12-09 125059.jpg'

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

        # คลิกปุ่มยืนยันทำรายการ
        click((680, 646), delay=5, description="คลิกปุ่มยืนยันทำรายการ")
        click((740, 651), delay=5, description="คลิกปุ่มยืนยันหน้าทวนข้อมูล")

        # คลิกปุ่มยืนยัน
        click((690, 651), delay=6, description="คลิกปุ่มยืนยัน")

        # คลิกรับพอดี
        click((574, 652), delay=8, description="คลิกปุ่มรับพอดี")

        # คลิกยืนยัน
        click((470, 425), delay=4, description="คลิกปุ่มยืนยันชำระเงิน")

        print("การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        print(f"เกิดข้อผิดพลาดในฟังก์ชัน run_test_case: {e}")

if __name__ == "__main__":
    main()
