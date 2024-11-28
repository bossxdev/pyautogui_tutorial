# นำเข้าไลบรารีที่จำเป็น
import pyautogui
import time  # ใช้สำหรับหน่วงเวลา (delay)

# ฟังก์ชันหลักสำหรับทดสอบระบบ
def main():
    """
    ฟังก์ชันหลักที่ใช้ในการควบคุมการทำงานของ Automated Test
    """
    try:
        # 1. การตั้งค่าเบื้องต้น
        setup_environment()

        # 2. ขั้นตอนการทดสอบ
        run_test_case()


    except Exception as e:
        print(f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")

# ฟังก์ชันสำหรับการตั้งค่าเริ่มต้น
def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าการทดสอบ เช่น เปิดแอปพลิเคชันหรือเตรียมหน้าต่าง
    """
    print("เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    print("การตั้งค่าเสร็จสิ้น")

# ฟังก์ชันสำหรับขั้นตอนการทดสอบ
def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกฟอร์ม หรือจำลองการทำงาน
    """
    print("เริ่มการทดสอบ...")

    
    pyautogui.moveTo(746, 134) #ปุ่มกรอกบาร์โค้ด
    pyautogui.click(button="left") 
    time.sleep(3)

    
    pyautogui.keyDown('shift')
    pyautogui.press('\\')
    pyautogui.keyUp('shift')
    pyautogui.write("0993000177967")
    time.sleep(2)

   
    pyautogui.click(479, 456, button="left")
    time.sleep(30)

    
    pyautogui.click(377, 559, button="left")
    pyautogui.write("3500")
    time.sleep(3)

    
    pyautogui.click(679, 641, button="left")
    time.sleep(5)

    pyautogui.click(729, 646, button="left")
    time.sleep(5)

    pyautogui.click(671, 644, button="left")
    time.sleep(5)

    pyautogui.click(560, 639, button="left")
    time.sleep(5)

    pyautogui.click(486, 427, button="left")

    print("การทดสอบเสร็จสมบูรณ์")
if __name__ == "__main__":
    main()
