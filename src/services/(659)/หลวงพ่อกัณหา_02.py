import pyautogui
import time

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
    
    print("เริ่มการทดสอบ...")
    
    pyautogui.click(746, 134) #กดปุ่มกรอกบาร์โค้ด
    time.sleep(3)

    pyautogui.keyDown('shift')
    pyautogui.press('\\')
    pyautogui.keyUp('shift')
    pyautogui.write("659020000000002")
    time.sleep(2)
    
    pyautogui.click(480, 464, button="left")
    time.sleep(30)
    
    #flow กรอกเงิน+ชำระเงิน
    pyautogui.write("30000") #---------เพิ่ม validate log ทุก action //  handle function //util
    time.sleep(3)
    
    pyautogui.click(700, 640, button="left")
    time.sleep(5)
    
    pyautogui.click(730, 645, button="left")
    time.sleep(3)
    
    pyautogui.click(700, 640, button="left")
    time.sleep(5)
    
    pyautogui.click(550, 640, button="left")
    time.sleep(3)
    
    pyautogui.click(490, 433, button="left")
    time.sleep(3)
    
    print("การทดสอบเสร็จสมบูรณ์")
if __name__ == "__main__":
    main()