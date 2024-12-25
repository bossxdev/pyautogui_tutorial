import pyautogui
import time
from src.utils.utility_func import click, write_text
from src.utils.log_state import log_state

def main():
    """
    ฟังก์ชันหลักสำหรับการควบคุมการทำงานของ Automated Test
    """
    try:
        log_state("S02_15test", log_level="DEBUG", log_message="เริ่มต้นการทำงาน Automated Testdddd")
        setup_environment()
        run_test_case()
    except Exception as e:
        log_state("S02_15test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        print(f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")

def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าระบบก่อนเริ่มการทดสอบ
    """
    log_state("S02_15test", log_level="INFO", log_message="เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    log_state("S02_15test", log_level="INFO", log_message="การตั้งค่าเสร็จสิ้น")

def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกข้อมูล หรือดำเนินการชำระเงิน
    """
    try:
        log_state("S02_15test", log_level="INFO", log_message="เริ่มการทดสอบ...")

        #คลิกปุ่มเคาน์เตอร์เซอร์วิส
        click((298, 131), delay=5, description="คลิกปุ่มเคาน์เตอร์เซอร์วิส")
        log_state("S02_15test", log_level="INFO", log_message="คลิกปุ่มเคาน์เตอร์เซอร์วิสสำเร็จ")
       # คลิกปุ่มผู้ว่าจ้าง
        click((560, 135), delay=5, description="คลิกปุ่มค้นหาผู้ว่าจ้าง")
        log_state("S02_15test", log_level="INFO", log_message="คลิกปุ่มค้นหาผู้ว่าจ้างสำเร็จ")
        
        write_text("นครหลวงคอนกรีด", delay=5, description="กรอกนครหลวงคอนกรีด")
        log_state("S02_15test", log_level="INFO", log_message="กรอกนครหลวงคอนกรีด")
        pyautogui.press('enter')

        click((361, 339), delay=5, description="คลิกเลือกสินเชื่อนาโน")
        log_state("S02_15test", log_level="INFO", log_message="คลิกเลือกสินเชื่อนาโนสำเร็จ")
        time.sleep(10)
        
        write_text("31000001", delay=4, description="รหัสลูกค้า")
        log_state("automation_test", log_level="INFO", log_message="กรอกรหัสลูกค้าสำเร็จ")
        pyautogui.press('enter')
        write_text("010019219999123", delay=4, description="กรอกเลขที่อ้างอิง")
        log_state("automation_test", log_level="INFO", log_message="กรอกเลขที่อ้างอิงสำเร็จ")
        pyautogui.press('enter')

        log_state("automation_test", log_level="INFO", log_message="รอลูกค้ากรอกหมายเลขโทรศัพท์ที่เครื่องedc")

        time.sleep(20)


        # กรอกจำนวนเงิน
        write_text("1632500", delay=5, description="กรอกจำนวนเงิน")
        log_state("S02_15test", log_level="INFO", log_message="กรอกจำนวนเงินสำเร็จ")

        # คลิกปุ่มยืนยันทำรายการ
        click((680, 646), delay=5, description="กดปุ่มยืนยันทำรายการ")
        click((740, 651), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        log_state("S02_15test", log_level="INFO", log_message="กดปุ่มยืนยันทำรายการสำเร็จ")

        # คลิกปุ่มยืนยัน
        click((690, 651), delay=6, description="กดปุ่มชำระเงิน")
        log_state("S02_15test", log_level="INFO", log_message="กดปุ่มชำระเงินสำเร็จ")

        # คลิกปุ่มรับพอดี
        click((574, 652), delay=8, description="กดปุ่มรับพอดี")
        log_state("S02_15test", log_level="INFO", log_message="กดปุ่มรับพอดีสำเร็จ")

        # คลิกปุ่มยืนยันการชำระเงิน
        click((470, 425), delay=4, description="กดปุ่มยืนยันชำระเงิน")
        log_state("S02_15test", log_level="INFO", log_message="การชำระเงินเสร็จสมบูรณ์")

        log_state("S02_15test", log_level="INFO", log_message="การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        log_state("S02_15test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        raise

if __name__ == "__main__":
    main()
