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
        write_text("099400001030300", delay=2, description="กรอกบาร์โค้ด")
        log_state("test_case", "INFO", "กรอกบาร์โค้ด: 099400001030300")
        

        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("652301107831126744", delay=2, description="")
        log_state("test_case", "INFO", "กรอกบาร์โค้ด: 652301107831126744")
        

        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("201587001867097", delay=2, description="")
        log_state("test_case", "INFO", "กรอกบาร์โค้ด: 201587001867097")
        

        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("3000100", delay=2, description="")
        log_state("test_case", "INFO", "กรอกบาร์โค้ด: 3000100")
        
        click((480, 464), delay=30, description="กคลิกปุ่มยืนยัน pop up บาร์โค้ดด")
        log_state("test_case", "INFO", "คลิกปุ่มยืนยัน pop up บาร์โค้ด")
        
        # #flow กรอกเงิน+ชำระเงิน
        # pyautogui.write("30000") #---------เพิ่ม validate log ทุก action //  handle function //util
        # time.sleep(3)
        
        # pyautogui.click(700, 640, button="left")
        # time.sleep(5)
        
        click((730, 645), delay=10, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        log_state("test_case", "INFO", "ยืนยันหน้าทวนข้อมูล")
        
        click((700, 640), delay=7, description="กดปุ่มชำระเงิน")
        log_state("test_case", "INFO", "กดปุ่มชำระเงิน")

        click((550, 640), delay=7, description="กดปุ่มรับพอดี")
        log_state("test_case", "INFO", "กดปุ่มรับพอดี")
        
        click((490, 433), delay=7, description="กดปุ่มยืนยันชำระเงิน")
        log_state("test_case", "INFO", "ยืนยันชำระเงิน")
        
        log_state("main_process", "DEBUG", "การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        log_state("main_process", "DEBUG", f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {str(e)}")
        raise


if __name__ == "__main__":
    main()