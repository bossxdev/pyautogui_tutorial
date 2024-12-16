import pyautogui
import time  # ใช้สำหรับหน่วงเวลา (delay)
from src.utils.utility_func import click, write_text, log_action

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

def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกฟอร์ม หรือจำลองการทำงาน
    """
    print("เริ่มการทดสอบ...")

    # คลิกกรอกบาร์โค้ด
    click((746, 134), delay=2, description="คลิกกรอกบาร์โค้ด")

    # กรอกรหัสบาร์โค้ด
    log_action("Write", "พิมพ์บาร์โค้ด 1")
    pyautogui.keyDown('shift')
    pyautogui.press('\\')
    pyautogui.keyUp('shift')
    write_text("0994000072635", delay=2, description="กรอกบาร์โค้ด 1")
    pyautogui.press('enter')

    time.sleep(10)

    write_text("A12345678", delay=2, description="กรอกบาร์โค้ด 2")
    pyautogui.press('enter')
    time.sleep(8)

    write_text("1234", delay=2, description="กรอกบาร์โค้ด 3")
    pyautogui.press('enter')
    time.sleep(20)

    # รอลูกค้ากรอกเบอร์โทรที่เครื่อง EDC

    # กรอกจำนวนเงิน
    write_text("49010", delay=4, description="กรอกจำนวนเงิน")

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
