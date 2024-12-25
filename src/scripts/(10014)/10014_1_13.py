import pyautogui
import time
from src.utils.utility_func import click, write_text
from src.utils.state import state
import traceback  


def monitor_image_display(image_path):
    # เริ่มต้นนับเวลา
    start_time = time.time()
    timeout = 20  # เวลารอสูงสุด 20 วินาที

    while time.time() - start_time < timeout:
        print("กำลังตรวจสอบภาพหน้าจอ...")
        try:
            # ใช้ pyautogui.locateOnScreen เพื่อจับภาพหน้าจอและตรวจสอบ
         if pyautogui.locateOnScreen(image_path, confidence=0.6):  # เพิ่มค่าความมั่นใจหรือลดให้เหมาะสม
            state("automation_test", level="INFO", message="พบภาพที่คาดหวังแล้ว")
 
            return True  # พบภาพที่ต้องการแล้ว
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการจับภาพหน้าจอ: {e}")
            state("automation_test", level="ERROR", message=f"เกิดข้อผิดพลาดในการตรวจสอบภาพ: {e}")

            return False  # หากเกิดข้อผิดพลาดในการจับภาพ

    # หากหมดเวลา 20 วินาทีโดยไม่มีการแสดงผล
    print("ข้อมูลไม่ถูกต้อง หรือหน้าจอไม่แสดงผลลัพธ์ที่คาดหวัง")
    state("automation_test", level="ERROR", message="ไม่พบภาพที่คาดหวังภายใน 20 วินาที")
    return False


def main():
    """
    ฟังก์ชันหลักสำหรับการควบคุมการทำงานของ Automated Test
    """
    try:
        state("automation_test", level="DEBUG", message="เริ่มต้นการทำงาน Automated Test")
        setup_environment()
        run_test_case()
    except Exception as e:
        state("automation_test", level="ERROR", message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        print(f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")


def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าระบบก่อนเริ่มการทดสอบ
    """
    state("automation_test", level="INFO", message="เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    state("automation_test", level="INFO", message="การตั้งค่าเสร็จสิ้น")


def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกฟอร์ม หรือดำเนินการชำระเงิน
    """
    try:
        state("automation_test", level="INFO", message="เริ่มการทดสอบ...")

        # คลิกปุ่มกรอกบาร์โค้ด
        click((740, 149), delay=5, description="คลิกปุ่มกรอกบาร์โค้ด")
        state("automation_test", level="INFO", message="คลิกปุ่มกรอกบาร์โค้ดสำเร็จ")

        # กรอกรหัสบาร์โค้ด
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("0107537001374", delay=2, description="กรอกรหัสบาร์โค้ด")

         # ตรวจสอบภาพหลังจากกรอกรหัสบาร์โค้ด
        if not monitor_image_display("EDC.png"):  # ตรวจสอบภาพหลังจากกรอกบาร์โค้ด
            state("automation_test", level="ERROR", message="ข้อมูลไม่ถูกต้อง")
            return
        # กดยืนยันบาร์โค้ด
        pyautogui.press('enter')
        state("automation_test", level="INFO", message="กรอกรหัสบาร์โค้ดสำเร็จ")

        time.sleep(10)
 
        click((361, 339), delay=5, description="คลิกเลือกค่าสินค้าร้านค้า")
        state("S02_15test", level="INFO", message="คลิกเลือกค่าสินค้าร้านค้า")
        pyautogui.press('enter')
        
        write_text("123456789", delay=4, description="กรอกรหัสลูกค้า")
        state("automation_test", level="INFO", message="กรอกรหัสลูกค้าสำเร็จ")
        pyautogui.press('enter')

        write_text("1234567893434", delay=4, description="กรอกเลขผู้เสียภาษาษี")
        state("automation_test", level="INFO", message="กรอกเลขผู้เสียภาษาษีสำเร็จ")
 
        time.sleep(20)

        # กรอกจำนวนเงิน
        write_text("30000", delay=4, description="กรอกจำนวนเงิน")
        state("automation_test", level="INFO", message="กรอกจำนวนเงินสำเร็จ")

        # คลิกปุ่มยืนยันทำรายการ
        click((680, 646), delay=5, description="กดปุ่มยืนยันทำรายการ")
        click((740, 651), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        state("automation_test", level="INFO", message="กดปุ่มยืนยันทำรายการสำเร็จ")

        click((690, 651), delay=6, description="กดปุ่มยืนยันชำระเงิน")
        state("automation_test", level="INFO", message="กดปุ่มชำระเงินสำเร็จ")

        # คลิกปุ่มรับพอดี
        click((574, 652), delay=8, description="กดปุ่มรับพอดี")
        state("automation_test", level="INFO", message="กดปุ่มรับพอดีสำเร็จ")

        # คลิกปุ่มยืนยันการชำระเงิน
        click((522, 454), delay=4, description="กดปุ่มยืนยันการชำระเงิน")

        state("automation_test", level="INFO", message="การชำระเงินเสร็จสมบูรณ์")

        state("automation_test", level="INFO", message="การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        # แสดงข้อผิดพลาดที่เกิดขึ้นพร้อมรายละเอียด
        error_message = f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {str(e)}"
        state("automation_test", level="ERROR", message=error_message)
        
        # แสดง stack trace เพื่อหาสาเหตุของข้อผิดพลาด
        traceback_message = traceback.format_exc()
        state("automation_test", level="ERROR", message=f"Stack Trace: {traceback_message}")
        
        print(error_message) 
        raise 


if __name__ == "__main__":
    main()