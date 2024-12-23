import pyautogui
import time
from src.utils.utility_func import click, write_text
from src.utils.log_handler import log_handler

def main():
    """
    ฟังก์ชันหลักสำหรับการควบคุมการทำงานของ Automated Test
    """
    try:
        log_handler("S02_15test", log_level="DEBUG", log_message="เริ่มต้นการทำงาน Automated Testdddd")
        setup_environment()
        run_test_case()
    except Exception as e:
        log_handler("S02_15test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        print(f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")

def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าระบบก่อนเริ่มการทดสอบ
    """
    log_handler("S02_15test", log_level="INFO", log_message="เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    log_handler("S02_15test", log_level="INFO", log_message="การตั้งค่าเสร็จสิ้น")

def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกข้อมูล หรือดำเนินการชำระเงิน
    """
    try:
        log_handler("S02_15test", log_level="INFO", log_message="เริ่มการทดสอบ...")

        #คลิกปุ่มเคาน์เตอร์เซอร์วิส
        click((298, 131), delay=5, description="คลิกปุ่มเคาน์เตอร์เซอร์วิส")
        log_handler("S02_15test", log_level="INFO", log_message="คลิกปุ่มเคาน์เตอร์เซอร์วิสสำเร็จ")
       # คลิกปุ่มผู้ว่าจ้าง
        click((560, 135), delay=5, description="คลิกปุ่มค้นหาผู้ว่าจ้าง")
        log_handler("S02_15test", log_level="INFO", log_message="คลิกปุ่มค้นหาผู้ว่าจ้างสำเร็จ")
        
        write_text("สำนักงาน สสว.", delay=5, description="กรอกสำนักงาน สสว")
        log_handler("S02_15test", log_level="INFO", log_message="กรอกสำนักงาน สสว")
        pyautogui.press('enter')

   # คลิกเลือกมูลนิธิเพื่อนหญิง
        click((298, 131), delay=5, description="คลิกเลือกสำนักงาน สสว")
        log_handler("S02_15test", log_level="INFO", log_message="คลิกเลือกสำนักงาน สสว")
        time.sleep(10)
      
        click((361, 339), delay=5, description="คลิกเลือกโครงการพลิกพื้น")
        log_handler("S02_15test", log_level="INFO", log_message="คลิกเลือกโครงการพลิกพื้นสำเร็จ")
        time.sleep(10)
        
        
              
        write_text("12345678901", delay=4, description="กรอกรหัสลูกค้า")
        log_handler("automation_test", log_level="INFO", log_message="กรอกรหัสลูกค้าสำเร็จ")
        pyautogui.press('enter')

        log_handler("automation_test", log_level="INFO", log_message="รอลูกค้ากรอกหมายเลขโทรศัพท์ที่เครื่องedc")

        time.sleep(20)

        # กรอกจำนวนเงิน
        write_text("49000", delay=5, description="กรอกจำนวนเงิน")
        log_handler("S02_15test", log_level="INFO", log_message="กรอกจำนวนเงินสำเร็จ")

        # คลิกปุ่มยืนยันทำรายการ
        click((680, 646), delay=5, description="กดปุ่มยืนยันทำรายการ")
        click((740, 651), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        log_handler("S02_15test", log_level="INFO", log_message="กดปุ่มยืนยันทำรายการสำเร็จ")

        # คลิกปุ่มยืนยัน
        click((690, 651), delay=6, description="กดปุ่มชำระเงิน")
        log_handler("S02_15test", log_level="INFO", log_message="กดปุ่มชำระเงินสำเร็จ")

        # คลิกปุ่มรับพอดี
        click((574, 652), delay=8, description="กดปุ่มรับพอดี")
        log_handler("S02_15test", log_level="INFO", log_message="กดปุ่มรับพอดีสำเร็จ")

        # คลิกปุ่มยืนยันการชำระเงิน
        click((470, 425), delay=4, description="กดปุ่มยืนยันชำระเงิน")
        log_handler("S02_15test", log_level="INFO", log_message="การชำระเงินเสร็จสมบูรณ์")

        log_handler("S02_15test", log_level="INFO", log_message="การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        log_handler("S02_15test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        raise

if __name__ == "__main__":
    main()
