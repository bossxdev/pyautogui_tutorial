import pyautogui
import time

from src.utils.utility_func import click, log_action, write_text


def main():
    try:
        setup_environment()
        run_test_case()
    except Exception as e:
        print(f"[ERROR] เกิดข้อผิดพลาดในโปรแกรมหลัก: {e}")


def setup_environment():
    print("[INFO] เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    print("[INFO] การตั้งค่าเสร็จสิ้น")


def run_test_case():
    try:
        print("[INFO] เริ่มการทดสอบ...")

        click((746, 134), delay=3, description="คลิกปุ่มกรอกบาร์โค้ด")

        log_action("Write", "พิมพ์อักษรพิเศษ | ")
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("0993000070241", delay=2, description="กรอกบาร์โค้ด")

        click((479, 456), delay=10, description="คลิกปุ่มยืนยัน pop up บาร์โค้ด")

        click((370, 275), delay=20, description="คลิกเลือก service")

        write_text("5000", delay=3, description="กรอกจำนวนเงิน")

        click((668, 637), delay=5, description="กดปุ่มยืนยันทำรายการ")

        click((750, 636), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")

        click((675, 636), delay=5, description="กดปุ่มชำระเงิน")

        click((558, 633), delay=5, description="กดปุ่มรับพอดี")

        click((490, 430), delay=5, description="กดปุ่มยืนยันชำระเงิน")

        print("[INFO] การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        log_action("Error", f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        raise


if __name__ == "__main__":
    main()
