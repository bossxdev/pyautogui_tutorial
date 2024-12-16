import pyautogui
import time

from src.utils.utility_func import click, log_action, write_text

def main():
    """
    ฟังก์ชันหลักที่ใช้ในการควบคุมการทำงานของ Automated Test
    """
    try:
        setup_environment()
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
    try:
        print("[INFO] เริ่มการทดสอบ...")

        # คลิกปุ่มกรอกบาร์โค้ด
        click((740, 149), delay=5, description="คลิกปุ่มกรอกบาร์โค้ด")

        # กรอกรหัสบาร์โค้ด
        log_action("Write", "พิมพ์อักษรพิเศษ | ")
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("020553200042302", delay=3, description="กรอกบาร์โค้ดส่วนแรก")

        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("14689007083", delay=20, description="กรอกบาร์โค้ดส่วนที่สอง")

        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("4900000", delay=6, description="กรอกบาร์โค้ดส่วนที่สาม")
        pyautogui.press('enter')

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
