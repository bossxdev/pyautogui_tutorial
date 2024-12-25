import pyautogui
import time
from src.utils.utility_func import click, write_text
from src.utils.log_state import log_state

def main():
    """
    ฟังก์ชันหลักสำหรับการควบคุมการทำงานของ Automated Test
    """
    try:
        log_state("automation_test", log_level="DEBUG", log_message="เริ่มต้นการทำงาน Automated Testdddd")
        setup_environment()
        run_test_case()
    except Exception as e:
        log_state("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        print(f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")

def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าระบบก่อนเริ่มการทดสอบ
    """
    log_state("automation_test", log_level="INFO", log_message="เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    log_state("automation_test", log_level="INFO", log_message="การตั้งค่าเสร็จสิ้น")


def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกฟอร์ม หรือจำลองการทำงาน
    """
    try:
        log_state("automation_test", log_level="INFO", log_message="เริ่มการทดสอบ...")

        # คลิกปุ่มกรอกบาร์โค้ด
        click((740, 149), delay=5, description="คลิกปุ่มกรอกบาร์โค้ด")

        # กรอกรหัสบาร์โค้ด
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("099400001123700", delay=3, description="กรอกบาร์โค้ดส่วนแรก")
        log_state("automation_test", log_level="INFO", log_message="กรอกบาร์โค้ดส่วนแรกสำเร็จ")

        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("12345678901", delay=20, description="กรอกบาร์โค้ดส่วนที่สอง")
        log_state("automation_test", log_level="INFO", log_message="กรอกรหัสลูกค้าสำเร็จ")
        
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("49000", delay=6, description="กรอกบาร์โค้ดส่วนที่สาม")
        log_state("automation_test", log_level="INFO", log_message="กรอกจำนวนเงินสำเร็จ")

        pyautogui.press('enter')
        log_state("automation_test", log_level="INFO", log_message="กรอกรหัสบาร์โค้ดสำเร็จ")
        log_state("automation_test", log_level="INFO", log_message="รอลูกค้ากรอกหมายเลขโทรศัพท์ที่เครื่องedc")
        time.sleep(20)
            # คลิกปุ่มยืนยันทำรายการ
        click((680, 646), delay=5, description="กดปุ่มยืนยันทำรายการ")
        click((740, 651), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        log_state("automation_test", log_level="INFO", log_message="กดปุ่มยืนยันทำรายการสำเร็จ")

        click((690, 651), delay=6, description="กดปุ่มยืนยันชำระเงิน")
        log_state("automation_test", log_level="INFO", log_message="กดปุ่มชำระเงินสำเร็จ")

        # คลิกปุ่มรับพอดี
        click((574, 652), delay=8, description="กดปุ่มรับพอดี")
        log_state("automation_test", log_level="INFO", log_message="กดปุ่มรับพอดีสำเร็จ")

        # คลิกปุ่มยืนยันการชำระเงิน
        click((522, 454), delay=4, description="กดปุ่มยืนยันการชำระเงิน")

        log_state("automation_test", log_level="INFO", log_message="การชำระเงินเสร็จสมบูรณ์")

        log_state("automation_test", log_level="INFO", log_message="การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        log_state("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        raise


if __name__ == "__main__":
    main()
