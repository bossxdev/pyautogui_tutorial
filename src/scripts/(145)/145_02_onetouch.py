import pyautogui
import time
from src.utils.utility_func import click, write_text
from src.utils.state import state

def main():
    """
    ฟังก์ชันหลักสำหรับการควบคุมการทำงานของ Automated Test
    """
    try:
        state("automation_test", log_level="DEBUG", log_message="เริ่มต้นการทำงาน Automated Testdddd")
        setup_environment()
        run_test_case()
    except Exception as e:
        state("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        print(f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")

def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าระบบก่อนเริ่มการทดสอบ
    """
    state("automation_test", log_level="INFO", log_message="เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    state("automation_test", log_level="INFO", log_message="การตั้งค่าเสร็จสิ้น")

def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกฟอร์ม หรือดำเนินการชำระเงิน
    """
    try:
        state("automation_test", log_level="INFO", log_message="เริ่มการทดสอบ...")
        #คลิกปุ่มเคาน์เตอร์เซอร์วิส
           #คลิกปุ่มเคาน์เตอร์เซอร์วิส
        click((298, 131), delay=5, description="คลิกปุ่มเคาน์เตอร์เซอร์วิส")
        state("S02_15test", log_level="INFO", log_message="คลิกปุ่มเคาน์เตอร์เซอร์วิสสำเร็จ")
       # คลิกปุ่มผู้ว่าจ้าง
        click((560, 135), delay=5, description="คลิกปุ่มค้นหาผู้ว่าจ้าง")
        state("S02_15test", log_level="INFO", log_message="คลิกปุ่มค้นหาผู้ว่าจ้างสำเร็จ")
        
        write_text("มูลนิธิสันติสุธ", delay=5, description="กรอกมูลนิธิสันติสุธ")
        state("S02_15test", log_level="INFO", log_message="กรอกมูลนิธิสันติสุธสำเร็จ")
        pyautogui.press('enter')

   # คลิกเลือกมูลนิธิสันติสุธ
        click((298, 131), delay=5, description="คลิกเลือกมูลนิธิสันติสุธ")
        state("S02_15test", log_level="INFO", log_message="คลิกเลือกมูลนิธิสันติสุธ")
        time.sleep(10)
 
        click((361, 339), delay=5, description="คลิกเลือกรับบริจาค")
        state("S02_15test", log_level="INFO", log_message="คลิกเลือกรับบริจาค")
        time.sleep(10)
        
        
        # กรอกจำนวนเงิน
        write_text("30000", delay=4, description="กรอกจำนวนเงิน")
        state("automation_test", log_level="INFO", log_message="กรอกจำนวนเงินสำเร็จ")

        # คลิกปุ่มยืนยันทำรายการ
        click((680, 646), delay=5, description="กดปุ่มยืนยันทำรายการ")
        click((740, 651), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        state("automation_test", log_level="INFO", log_message="กดปุ่มยืนยันทำรายการสำเร็จ")

        click((690, 651), delay=6, description="กดปุ่มยืนยันชำระเงิน")
        state("automation_test", log_level="INFO", log_message="กดปุ่มชำระเงินสำเร็จ")

        # คลิกปุ่มรับพอดี
        click((574, 652), delay=8, description="กดปุ่มรับพอดี")
        state("automation_test", log_level="INFO", log_message="กดปุ่มรับพอดีสำเร็จ")

        # คลิกปุ่มยืนยันการชำระเงิน
        click((522, 454), delay=4, description="กดปุ่มยืนยันการชำระเงิน")

        state("automation_test", log_level="INFO", log_message="การชำระเงินเสร็จสมบูรณ์")

        state("automation_test", log_level="INFO", log_message="การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        state("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        raise
if __name__ == "__main__":
    main()
