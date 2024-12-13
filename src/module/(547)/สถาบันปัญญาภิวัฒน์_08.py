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
        write_text("099400063398008",delay=2, description="กรอกบาร์โค้ด")
        
        click((480, 464), delay=20, description="คลิกปุ่มยืนยัน pop up บาร์โค้ด")
        
        write_text("5434567", delay=3, description="กรอกจำนวนเงิน")
        
        pyautogui.press("enter")
        time.sleep(3)

        write_text("00123431", delay=3, description="")

        pyautogui.press("enter") #เบอร์ 0865562828
        time.sleep(20)
        
        write_text("31000", delay=3, description="")
        
        # flow การชำระเงิน
        click((670, 640),delay=5, description="กดปุ่มยืนยันทำรายการ")
        
        click((750, 636), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        
        click((675, 636), delay=5, description="กดปุ่มชำระเงิน")
        
        click((558, 633), delay=5, description="กดปุ่มรับพอดี")
        
        click((490, 430), delay=5, description="กดปุ่มยืนยันชำระเงิน")
        # flow การชำระเงิน
        
        print("[INFO] การทดสอบเสร็จสมบูรณ์")
        
    except Exception as e:
        log_action("Error", f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        raise
    

if __name__ == "__main__":
        main()
