import pyautogui
import time

from src.utils.utility_func import click, log_action, write_text

def main():
    try:  
        setup_environment()
        run_test_case()     
    except Exception as e:
        print(f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")

def setup_environment():
    print("เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    print("การตั้งค่าเสร็จสิ้น")
    
def run_test_case():
    try:
        print("[INFO] เริ่มการทดสอบ...")
    
        click((746, 134), delay=3, description="คลิกปุ่มกรอกบาร์โค้ด")

        log_action("Write", "พิมพ์อักษรพิเศษ | ")
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("099400001030300", delay=2, description="กรอกบาร์โค้ด")
        
        log_action("Write", "พิมพ์อักษรพิเศษ | ")
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("652301107831126744", delay=2, description="")
        
        log_action("Write", "พิมพ์อักษรพิเศษ | ")
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("201587001867097", delay=2, description="")
        
        log_action("Write", "พิมพ์อักษรพิเศษ | ")
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("3000100", delay=2, description="")
        
        pyautogui.click(480, 464, button="left")
        time.sleep(30)
        
        # #flow กรอกเงิน+ชำระเงิน
        # pyautogui.write("30000") #---------เพิ่ม validate log ทุก action //  handle function //util
        # time.sleep(3)
        
        # pyautogui.click(700, 640, button="left")
        # time.sleep(5)
        
        click((730, 645), delay=10, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        
        click((700, 640), delay=7, description="กดปุ่มชำระเงิน")

        click((550, 640), delay=7, description="กดปุ่มรับพอดี")
        
        click((490, 433), delay=7, description="กดปุ่มยืนยันชำระเงิน")
        
        print("[INFO] การทดสอบเสร็จสมบูรณ์")
        
    except Exception as e:
        log_action("Error", f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        raise
    
if __name__ == "__main__":
        main()