import pyautogui
import time
from src.utils.utility_func import click, write_text
from src.utils.state import state

def main():
    """
    ฟังก์ชันหลักสำหรับการควบคุมการทำงานของ Automated Test
    """
    try:
        state("automation_test", level="DEBUG", message="เริ่มต้นการทำงาน Automated Testdddd")
        setup_environment()
        run_test_case()
    except Exception as e:
        state("automation_test", level="ERROR", message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        print(f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")

def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าระบบก่อนเริ่มการทดสอบ
    """
    state("automation_test", level="INFO", message="เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    state("automation_test", level="INFO", message="การตั้งค่าเสร็จสิ้น")


def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกฟอร์ม หรือจำลองการทำงาน
    """
    try:
        state("automation_test", level="INFO", message="เริ่มการทดสอบ...")

        # คลิกปุ่มกรอกบาร์โค้ด
        click((740, 149), delay=5, description="คลิกปุ่มกรอกบาร์โค้ด")

        # กรอกรหัสบาร์โค้ด
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("010753700264803", delay=3, description="กรอกบาร์โค้ดส่วนแรก")
        state("automation_test", level="INFO", message="กรอกบาร์โค้ดส่วนแรกสำเร็จ")

        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("31000001", delay=20, description="กรอกบาร์โค้ดส่วนที่สอง")
        state("automation_test", level="INFO", message="กรอกรหัสลูกค้าสำเร็จ")
        
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("010019219999123", delay=20, description="กรอกบาร์โค้ดส่วนทีสาม")
        state("automation_test", level="INFO", message="กรอกเลขที่อ้างอิงสำเร็จ")
        
        
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("123", delay=6, description="กรอกบาร์โค้ดส่วนที่สี่")
        state("automation_test", level="INFO", message="กรอกจำนวนเงินสำเร็จ")

        pyautogui.press('enter')
        state("automation_test", level="INFO", message="กรอกรหัสบาร์โค้ดสำเร็จ")
        state("automation_test", level="INFO", message="รอลูกค้ากรอกหมายเลขโทรศัพท์ที่เครื่องedc")
        time.sleep(20)
            # คลิกปุ่มยืนยันทำรายการ
        click((680, 646), delay=5, description="กดปุ่มยืนยันทำรายการ")
        click((740, 651), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        state("automation_test", level="INFO", message="กดปุ่มยืนยันทำรายการสำเร็จ")

        click((690, 651), delay=6, description="กดปุ่มยืนยันชำระเงิน")
        state("automation_test", level="INFO", message="กดปุ่มชำระเงินสำเร็จ")

        # คลิกปุ่มรับพอดี
        click((574, 652), delay=8, description="กดปุ่มรับพอดี")
        state("automation_test", level="INFO", message="กดปุ่มรับพอดีสำเร็จ")

        # คลิกปุ่มยืนยันการชำระเงิน
        click((522, 454), delay=4, description="กดปุ่มยืนยันการชำระเงิน")

        state("automation_test", level="INFO", message="การชำระเงินเสร็จสมบูรณ์")

        state("automation_test", level="INFO", message="การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        state("automation_test", level="ERROR", message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        raise


if __name__ == "__main__":
    main()
