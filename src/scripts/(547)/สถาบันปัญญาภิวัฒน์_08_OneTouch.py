import pyautogui
import time
from src.utils.utility_func import click, write_text
from src.utils.log_handler import log_handler

def main():
    try:
        log_handler("main_process", "DEBUG", "เริ่มต้นการทำงานของโปรแกรม")
        setup_environment()
        run_test_case()
    except Exception as e:
        log_handler("main_process", "ERROR", f"เกิดข้อผิดพลาดในโปรแกรมหลัก: {str(e)}")


def setup_environment():
    log_handler("setup", "DEBUG", "เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    log_handler("setup", "DEBUG", "การตั้งค่าเสร็จสิ้น")


def run_test_case():
    try:
        log_handler("test_case", "DEBUG", "เริ่มการทดสอบ...")

        click((210, 140), delay=10, description="กดปุ่มเคาน์เตอร์เซอร์วิส")
        log_handler("test_case", "INFO", "กดปุ่มเคาน์เตอร์เซอร์วิส")
        
        click((555,140), delay=5, description="กดปุ่มการศึกษา/ติวเตอร์/มหาวิทยาลัย")
        log_handler("test_case", "INFO", "กดปุ่มการศึกษา/ติวเตอร์/มหาวิทยาลัย")
        
        click((600, 340), delay=3, description="กดปุ่มบริจาค/มูลนิธิ")
        log_handler("test_case", "INFO", "กดปุ่มบริจาค/มูลนิธิ")
        
        click((80, 220), delay=3, description="กดปุ่มติวเตอร์/กวดวิชา")
        log_handler("test_case", "INFO", "กดปุ่มติวเตอร์/กวดวิชา")
        
        click((100, 350), delay=8, description="กดปุ่มสถาบันปัญญาภิวัฒน์")
        log_handler("test_case", "INFO", "กดปุ่มสถาบันปัญญาภิวัฒน์")
        
        click((500, 640), delay=8, description="กดปุ่มถัดไป")
        log_handler("test_case", "INFO", "กดปุ่มถัดไป")
        
        click((400, 460), delay=30, description="คลิกเลือก service")
        log_handler("test_case", "INFO", "คลิกเลือก service")
        
        write_text("5434567", delay=3, description="กรอกรหัสพนักงาน")
        log_handler("test_case", "INFO", "กรอกรหัสพนักงาน")
        
        pyautogui.press("enter")
        time.sleep(5)
        
        write_text("00123431", delay=3, description="กรอกเลขที่สัญญา")
        log_handler("test_case", "INFO", "กรอกเลขที่สัญญา")
        
        pyautogui.press("enter")
        time.sleep(30)
        
        log_handler("test_case", "INFO", "กรอกเบอร์โทรศัพท์ที่เครื่อง EDC")
        
        write_text("100", delay=5, description="กรอกจำนวนเงิน")
        log_handler("test_case", "INFO", "กรอกจำนวนเงิน: 100")

        click((668, 637), delay=5, description="กดปุ่มยืนยันทำรายการ")
        log_handler("test_case", "INFO", "ยืนยันทำรายการ")

        click((750, 636), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        log_handler("test_case", "INFO", "ยืนยันหน้าทวนข้อมูล")

        click((675, 636), delay=5, description="กดปุ่มชำระเงิน")
        log_handler("test_case", "INFO", "กดปุ่มชำระเงิน")

        click((558, 633), delay=5, description="กดปุ่มรับพอดี")
        log_handler("test_case", "INFO", "กดปุ่มรับพอดี")

        click((490, 430), delay=5, description="กดปุ่มยืนยันชำระเงิน")
        log_handler("test_case", "INFO", "ยืนยันชำระเงิน")

        log_handler("test_case", "DEBUG", "การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        log_handler("test_case", "DEBUG", f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {str(e)}")
        raise


if __name__ == "__main__":
    main()