
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
    pyautogui.write("0107551000151")
    time.sleep(2)
    
    pyautogui.click(480, 464, button="left")
    time.sleep(10)
    
    pyautogui.click(354, 440, button="left")
    time.sleep(7)
    
    pyautogui.click(400, 555, button="left")
    time.sleep(35)
    
    pyautogui.write("5000")
    time.sleep(2)
    
    pyautogui.click(677, 635, button="left" )
    time.sleep(3)
    
    pyautogui.click(736, 636, button="left")
    time.sleep(5)
    
    pyautogui.click(700, 640, button="left")
    time.sleep(5)
    
    pyautogui.click(560, 630, button="left")
    time.sleep(3)
    
    pyautogui.click(500, 430, button="left")
    time.sleep(5)
    
    print("การทดสอบเสร็จสมบูรณ์")
if __name__ == "__main__":
    main()
