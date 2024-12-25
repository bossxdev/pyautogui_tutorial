import pyautogui
import time
from src.utils.utility_func import click, write_text
from src.utils.state import state

def main():
    try:
        state("main_process", "DEBUG", "เริ่มต้นการทำงานของโปรแกรม")
        setup_environment()
        run_test_case()
    except Exception as e:
        state("main_process", "ERROR", f"เกิดข้อผิดพลาดในโปรแกรมหลัก: {str(e)}")


def setup_environment():
    state("setup", "DEBUG", "เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    state("setup", "DEBUG", "การตั้งค่าเสร็จสิ้น")
    
def run_test_case():
    try:
        state("test_case", "DEBUG", "เริ่มการทดสอบ...")

        click((746, 134), delay=3, description="คลิกปุ่มกรอกบาร์โค้ด")
        state("test_case", "INFO", "คลิกปุ่มกรอกบาร์โค้ด")

        state("test_case", "INFO", "พิมพ์อักษรพิเศษ |")
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("0994000772254", delay=2, description="กรอกบาร์โค้ด")
        state("test_case", "INFO", "กรอกบาร์โค้ด: 0994000772254")
        
        click((480, 464), delay=15, description="คลิกปุ่มยืนยัน pop up บาร์โค้ด")
        state("test_case", "INFO", "คลิกปุ่มยืนยัน pop up บาร์โค้ด")
        
        click((500, 531), delay=4, description="")
        
        click((400, 450), delay=8, description="")
        
        write_text("2311000096115", delay=3, description="")
        state("test_case", "INFO", "กรอกรหัสอ้างอิง: 2311000096115")
        
        pyautogui.press("enter")
        time.sleep(10)
        
        write_text("7703760231126748", delay=2, description="")
        state("test_case", "INFO", "กรอกรหัสใบสมัคร")

        
        pyautogui.press("enter")
        time.sleep(7)
        state("test_case", "INFO", "กด Enter")
        
        write_text("100", delay=3, description="กรอกจำนวนเงิน")
        state("test_case", "INFO", "กรอกจำนวนเงิน: 100")

        
        # flow การชำระเงิน
        click((668, 637), delay=5, description="กดปุ่มยืนยันทำรายการ")
        state("test_case", "INFO", "ยืนยันทำรายการ")

        click((750, 636), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        state("test_case", "INFO", "ยืนยันหน้าทวนข้อมูล")

        click((675, 636), delay=5, description="กดปุ่มชำระเงิน")
        state("test_case", "INFO", "กดปุ่มชำระเงิน")

        click((558, 633), delay=5, description="กดปุ่มรับพอดี")
        state("test_case", "INFO", "กดปุ่มรับพอดี")

        click((490, 430), delay=5, description="กดปุ่มยืนยันชำระเงิน")
        state("test_case", "INFO", "ยืนยันชำระเงิน")
        # flow การชำระเงิน
        
        state("main_process", "DEBUG", "การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        state("main_process", "DEBUG", f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {str(e)}")
        raise


if __name__ == "__main__":
    main()