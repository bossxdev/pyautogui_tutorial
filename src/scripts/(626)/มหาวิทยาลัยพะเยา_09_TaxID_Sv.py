import pyautogui
import time
from src.utils.utility_func import click, write_text
from src.utils.log_state import log_state

def main():
    try:
        log_state("main_process", "DEBUG", "เริ่มต้นการทำงานของโปรแกรม")
        setup_environment()
        run_test_case()
    except Exception as e:
        log_state("main_process", "ERROR", f"เกิดข้อผิดพลาดในโปรแกรมหลัก: {str(e)}")


def setup_environment():
    log_state("setup", "DEBUG", "เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    log_state("setup", "DEBUG", "การตั้งค่าเสร็จสิ้น")
    
def run_test_case():
    try:
        log_state("test_case", "DEBUG", "เริ่มการทดสอบ...")

        click((746, 134), delay=3, description="คลิกปุ่มกรอกบาร์โค้ด")
        log_state("test_case", "INFO", "คลิกปุ่มกรอกบาร์โค้ด")

        log_state("test_case", "INFO", "พิมพ์อักษรพิเศษ |")
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("099400077225409", delay=2, description="กรอกบาร์โค้ด")
        log_state("test_case", "INFO", "กรอกบาร์โค้ด: 099400077225409")
        
        click((480, 464), delay=20, description="คลิกปุ่มยืนยัน pop up บาร์โค้ด")
        log_state("test_case", "INFO", "คลิกปุ่มยืนยัน pop up บาร์โค้ด")
        
        write_text("2279900836778", delay=3, description="")
        log_state("test_case", "INFO", "")
        
        pyautogui.press("enter")
        time.sleep(10)
        
        write_text("207200189531126790", delay=3, description="") 
        log_state("test_case", "INFO", "")
        
        pyautogui.press("enter")
        time.sleep(7)

        write_text("100", delay=3, description="กรอกจำนวนเงิน")
        log_state("test_case", "INFO", "กรอกจำนวนเงิน: 100")
        
       # flow การชำระเงิน
        click((668, 637), delay=5, description="กดปุ่มยืนยันทำรายการ")
        log_state("test_case", "INFO", "ยืนยันทำรายการ")

        click((750, 636), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        log_state("test_case", "INFO", "ยืนยันหน้าทวนข้อมูล")

        click((675, 636), delay=5, description="กดปุ่มชำระเงิน")
        log_state("test_case", "INFO", "กดปุ่มชำระเงิน")

        click((558, 633), delay=5, description="กดปุ่มรับพอดี")
        log_state("test_case", "INFO", "กดปุ่มรับพอดี")

        click((490, 430), delay=5, description="กดปุ่มยืนยันชำระเงิน")
        log_state("test_case", "INFO", "ยืนยันชำระเงิน")
        # flow การชำระเงิน
        
        log_state("main_process", "DEBUG", "การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        log_state("main_process", "DEBUG", f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {str(e)}")
        raise


if __name__ == "__main__":
    main()