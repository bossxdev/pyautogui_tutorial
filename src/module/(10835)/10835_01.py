# นำเข้าไลบรารีที่จำเป็น
import pyautogui
import time  # ใช้สำหรับหน่วงเวลา (delay)
from src.utils.utility_func import click, write_text, log_action

# ฟังก์ชันหลักสำหรับทดสอบระบบ
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

# ฟังก์ชันสำหรับการตั้งค่าเริ่มต้น
def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าการทดสอบ เช่น เปิดแอปพลิเคชันหรือเตรียมหน้าต่าง
    """
    print("เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    print("การตั้งค่าเสร็จสิ้น")

# ฟังก์ชันสำหรับขั้นตอนการทดสอบ
def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกฟอร์ม หรือจำลองการทำงาน
    """
    print("เริ่มการทดสอบ...")

    # คลิกปุ่มกรอกบาร์โค้ด
    click((740, 149), delay=5, description="คลิกปุ่มกรอกบาร์โค้ด")

    # กรอกรหัสบาร์โค้ด
    log_action("Write", "พิมพ์บาร์โค้ด 010753700264801")
    pyautogui.keyDown('shift')
    pyautogui.press('\\')
    pyautogui.keyUp('shift')
    write_text("010753700264801", delay=3, description="กรอกบาร์โค้ดแรก")
    
    pyautogui.keyDown('shift')
    pyautogui.press('\\')
    pyautogui.keyUp('shift')
    write_text("31000001", delay=3, description="กรอกบาร์โค้ดที่สอง")
    
    pyautogui.keyDown('shift')
    pyautogui.press('\\')
    pyautogui.keyUp('shift')
    write_text("010019219999123", delay=3, description="กรอกบาร์โค้ดที่สาม")
    
    pyautogui.keyDown('shift')
    pyautogui.press('\\')
    pyautogui.keyUp('shift')
    write_text("123", delay=3, description="กรอกบาร์โค้ดสุดท้าย")
    pyautogui.press('enter')
    time.sleep(35)

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

if __name__ == "__main__":
    main()
