
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
    pyautogui.write("3470000000000")
    time.sleep(2)
    
    pyautogui.click(490, 470, button="left")
    time.sleep(20)
    
    pyautogui.write("20000")
    time.sleep(3)
    
    pyautogui.click(670, 640, button="left")
    time.sleep(3)
    
    pyautogui.click(740, 646, button="left")
    time.sleep(3)
    
    pyautogui.click(700, 645, button="left")
    time.sleep(5)
    
    pyautogui.click(560, 634, button="left")
    time.sleep(3)
    
    pyautogui.click(488, 442, button="left")
    time.sleep(3)
    
    print("การทดสอบเสร็จสมบูรณ์")
if __name__ == "__main__":
    main()
