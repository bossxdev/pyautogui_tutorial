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
        click((207, 140), delay=10, description="คลิกปุ่มเคาน์เตอร์เซอร์วิส")
        log_handler("S02_15test", log_level="INFO", log_message="คลิกปุ่มเคาน์เตอร์เซอร์วิสสำเร็จ")
        time.sleep(5)
       # คลิกปุ่มผู้ว่าจ้าง
        click((570, 154), delay=7, description="คลิกปุ่มกลุ่มผู้ว่าจ้าง")
        log_handler("S02_15test", log_level="INFO", log_message="คลิกปุ่มกลุ่มผู้ว่าจ้างสำเร็จ")
        # คลิกปุ่มผู้ว่าจ้าง
        click((208, 336), delay=7, description="คลิกปุ่มชำระค่าสินค้า/ขายตรง/หนังสือ")
        log_handler("S02_15test", log_level="INFO", log_message="คลิกปุ่มชำระค่าสินค้า/ขายตรง/หนังสือสำเร็จ")
        # คลิกปุ่มผู้ว่าจ้าง
        click((71, 221), delay=7, description="คลิกปุ่มชำระค่าสินค้า")
        log_handler("S02_15test", log_level="INFO", log_message="คลิกปุ่มชำระค่าสินค้าสำเร็จ")
        # คลิกปุ่มผู้ว่าจ้าง
        click((510, 649), delay=7, description="คลิกปุ่มหน้าถัดไป")
        log_handler("S02_15test", log_level="INFO", log_message="คลิกปุ่มหน้าถัดไปสำเร็จ")
        time.sleep(5)

        
   # คลิกเลือกมูลนิธิเพื่อนหญิง
        click((219, 224,), delay=5, description="คลิกเลือกบริษัท ไอ.ซี.ซี.อินเตอร์เนชั่นแนลจำกัด")
        log_handler("S02_15test", log_level="INFO", log_message="คลิกเลือกบริษัท ไอ.ซี.ซี.อินเตอร์เนชั่นแนลจำกัดสำเร็จ")
        time.sleep(10)
        click((360, 287), delay=5, description="คลิกเลือกค่าสินค้าร้านค้า")
        log_handler("S02_15test", log_level="INFO", log_message="คลิกเลือกค่าสินค้าร้านค้า")
        time.sleep(10)
        
        write_text("123456789", delay=4, description="กรอกรหัสลูกค้า")
        pyautogui.press('enter')

        log_handler("automation_test", log_level="INFO", log_message="กรอกรหัสลูกค้าสำเร็จ")
        
        write_text("1234567893434", delay=4, description="กรอกเลขผู้เสียภาษาษี")
        log_handler("automation_test", log_level="INFO", log_message="กรอกเลขผู้เสียภาษาษีสำเร็จ")

        pyautogui.press('enter')
 
        time.sleep(20)

        # กรอกจำนวนเงิน
        write_text("50", delay=5, description="กรอกจำนวนเงิน")
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
