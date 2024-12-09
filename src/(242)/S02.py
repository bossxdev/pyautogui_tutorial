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

    #คลิกปุ่มกรอกบางโค้ด
    pyautogui.moveTo(740, 149, duration=0.5)  # เพิ่มเวลาในการเคลื่อนที่
    pyautogui.click(button="left") 
    time.sleep(5)
#กรอกรหัสบารโค้ด
    pyautogui.keyDown('shift')
    pyautogui.press('\\')
    pyautogui.keyUp('shift')
    pyautogui.write("099300017796702")
    pyautogui.press('enter')
    time.sleep(25)
#รอลูกค้ากรอกหมายเลขโทรศัพธที่เครือง edc

    pyautogui.write("50")
    time.sleep(5)


#คลิกปุ่มยืนยันทำรายการ

    pyautogui.moveTo(680, 646, duration=0.5)  # เพิ่มเวลาในการเคลื่อนที่
    pyautogui.click(button="left") 
    time.sleep(5)

    pyautogui.moveTo(740, 651, duration=0.5)  # เพิ่มเวลาในการเคลื่อนที่
    pyautogui.click(button="left") 
    time.sleep(5)
#คลิกปุ่มยืนยัน

    pyautogui.moveTo(690, 651, duration=0.5)  # เพิ่มเวลาในการเคลื่อนที่
    pyautogui.click(button="left") 
    time.sleep(6)

#คลิกรับมาพอดี
    pyautogui.moveTo(574, 652, duration=0.5)  # เพิ่มเวลาในการเคลื่อนที่
    pyautogui.click(button="left") 
    time.sleep(8)


#คลิกยืนยัน
    pyautogui.moveTo(470, 425, duration=0.5)  # เพิ่มเวลาในการเคลื่อนที่
    pyautogui.click(button="left") 
    time.sleep(4)

    print("การทดสอบเสร็จสมบูรณ์")
if __name__ == "__main__":
    main()
