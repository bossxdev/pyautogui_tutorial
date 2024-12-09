
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
    
    pyautogui.click(746, 134)
    time.sleep(3)

    
    pyautogui.keyDown('shift')
    pyautogui.press('\\')
    pyautogui.keyUp('shift')
    pyautogui.write("0993000070241")
    time.sleep(2)
    
    pyautogui.click(479, 456, button="left")
    time.sleep(10)
    
    pyautogui.click(370, 275, button="left") #เปลี่ยนรายการ
    time.sleep(20)
    
    pyautogui.write("5000")
    time.sleep(3)
    
    pyautogui.click(668, 637, button="left")
    time.sleep(3)
    
    pyautogui.click(750, 636, button="left")
    time.sleep(5)
    
    pyautogui.click(675, 636, button="left")
    time.sleep(5)
    
    pyautogui.click(558, 633, button="left")
    time.sleep(5)
    
    pyautogui.click(490, 430, button="left")
    time.sleep(5)
    
    
    print("การทดสอบเสร็จสมบูรณ์")
if __name__ == "__main__":
    main()
