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
    time.sleep(2)  # หน่วงเวลาเพื่อเตรียมระบบ
    print("การตั้งค่าเสร็จสิ้น")

def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกฟอร์ม หรือจำลองการทำงาน
    """
    try:
        print("[INFO] เริ่มการทดสอบ...")

        # คลิกปุ่มกรอกบาร์โค้ด
        click((740, 149), delay=5, description="คลิกปุ่มกรอกบาร์โค้ด")

        # กรอกรหัสบาร์โค้ด
        log_action("Write", "พิมพ์บาร์โค้ด")
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("099300017796702", delay=0, description="กรอกบาร์โค้ด")
        pyautogui.press('enter')

        # รอลูกค้ากรอกหมายเลขโทรศัพท์ที่เครื่อง EDC
        write_text("50", delay=5, description="กรอกหมายเลขโทรศัพท์")

        # คลิกปุ่มยืนยันทำรายการ
        click((680, 646), delay=5, description="กดปุ่มยืนยันทำรายการ")

        # คลิกปุ่มยืนยันหน้าทวนข้อมูล
        click((740, 651), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")

        # คลิกปุ่มยืนยัน
        click((690, 651), delay=6, description="กดปุ่มยืนยัน")

        # คลิกรับพอดี
        click((574, 652), delay=8, description="กดปุ่มรับพอดี")

        # คลิกยืนยัน
        click((470, 425), delay=4, description="กดปุ่มยืนยันชำระเงิน")

        print("[INFO] การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        log_action("Error", f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        raise

if __name__ == "__main__":
    main()
