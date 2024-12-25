import pyautogui
import time
from src.utils.utility_func import click, write_text
from src.utils.state import state

def main():
    """
    ฟังก์ชันหลักสำหรับการควบคุมการทำงานของ Automated Test
    """
    try:
        state("S02_15test", level="DEBUG", message="เริ่มต้นการทำงาน Automated Testdddd")
        setup_environment()
        run_test_case()
    except Exception as e:
        state("S02_15test", level="ERROR", message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        print(f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")

def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าระบบก่อนเริ่มการทดสอบ
    """
    state("S02_15test", level="INFO", message="เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    state("S02_15test", level="INFO", message="การตั้งค่าเสร็จสิ้น")

def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกข้อมูล หรือดำเนินการชำระเงิน
    """
    try:
        state("S02_15test", level="INFO", message="เริ่มการทดสอบ...")

        #คลิกปุ่มเคาน์เตอร์เซอร์วิส
        click((298, 131), delay=5, description="คลิกปุ่มเคาน์เตอร์เซอร์วิส")
        state("S02_15test", level="INFO", message="คลิกปุ่มเคาน์เตอร์เซอร์วิสสำเร็จ")
       # คลิกปุ่มผู้ว่าจ้าง
        click((560, 135), delay=5, description="คลิกปุ่มค้นหาผู้ว่าจ้าง")
        state("S02_15test", level="INFO", message="คลิกปุ่มค้นหาผู้ว่าจ้างสำเร็จ")
        
        write_text("นครหลวงคอนกรีด", delay=5, description="กรอกนครหลวงคอนกรีด")
        state("S02_15test", level="INFO", message="กรอกนครหลวงคอนกรีด")
        pyautogui.press('enter')

        click((361, 339), delay=5, description="คลิกเลือกสินเชื่อสาขา")
        state("S02_15test", level="INFO", message="คลิกเลือกสินเชื่อสาขาโนสำเร็จ")
        time.sleep(10)
        
        write_text("31000001", delay=4, description="รหัสลูกค้า")
        state("automation_test", level="INFO", message="กรอกรหัสลูกค้าสำเร็จ")
        pyautogui.press('enter')
        write_text("010019219999123", delay=4, description="กรอกเลขที่อ้างอิง")
        state("automation_test", level="INFO", message="กรอกเลขที่อ้างอิงสำเร็จ")
        pyautogui.press('enter')

        state("automation_test", level="INFO", message="รอลูกค้ากรอกหมายเลขโทรศัพท์ที่เครื่องedc")

        time.sleep(20)


        # กรอกจำนวนเงิน
        write_text("1632500", delay=5, description="กรอกจำนวนเงิน")
        state("S02_15test", level="INFO", message="กรอกจำนวนเงินสำเร็จ")

        # คลิกปุ่มยืนยันทำรายการ
        click((680, 646), delay=5, description="กดปุ่มยืนยันทำรายการ")
        click((740, 651), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        state("S02_15test", level="INFO", message="กดปุ่มยืนยันทำรายการสำเร็จ")

        # คลิกปุ่มยืนยัน
        click((690, 651), delay=6, description="กดปุ่มชำระเงิน")
        state("S02_15test", level="INFO", message="กดปุ่มชำระเงินสำเร็จ")

        # คลิกปุ่มรับพอดี
        click((574, 652), delay=8, description="กดปุ่มรับพอดี")
        state("S02_15test", level="INFO", message="กดปุ่มรับพอดีสำเร็จ")

        # คลิกปุ่มยืนยันการชำระเงิน
        click((470, 425), delay=4, description="กดปุ่มยืนยันชำระเงิน")
        state("S02_15test", level="INFO", message="การชำระเงินเสร็จสมบูรณ์")

        state("S02_15test", level="INFO", message="การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        state("S02_15test", level="ERROR", message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        raise

if __name__ == "__main__":
    main()
