import pyautogui
import time
from src.utils.utility_func import click, write_text
from src.utils.log_handler import log_handler


def main():
    """
    ฟังก์ชันหลักสำหรับการควบคุมการทำงานของ Automated Test
    """
    try:
        log_handler("automation_test", log_level="DEBUG", log_message="เริ่มต้นการทำงาน Automated Testdddd")
        setup_environment()
        run_test_case()
        
    except Exception as e:
        log_handler("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        print(f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")

def monitor_image_display(image_path, timeout=2):
    """
    Returns:
        bool: True ถ้าพบภาพที่ต้องการ, False ถ้าไม่พบหรือเกิดข้อผิดพลาด
    """
    start_time = time.time()

    while time.time() - start_time < timeout:
        print("กำลังตรวจสอบภาพหน้าจอ...")
        try:
            # ใช้ pyautogui.locateOnScreen เพื่อตรวจสอบภาพ
            if pyautogui.locateOnScreen(image_path, confidence=0.8):
                print("INFO: พบภาพที่คาดหวังแล้ว")
                return False  # พบภาพที่ต้องการแล้ว        
        except Exception as e:
            print(f"ERROR: เกิดข้อผิดพลาดในการตรวจสอบภาพ: {e}")
            return True  # หากเกิดข้อผิดพลาดในการจับภาพ

    print("INFO: ไม่พบภาพที่ต้องการภายในเวลาที่กำหนด")
    return True
def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าระบบก่อนเริ่มการทดสอบ
    """
    log_handler("automation_test", log_level="INFO", log_message="เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    log_handler("automation_test", log_level="INFO", log_message="การตั้งค่าเสร็จสิ้น")


def run_test_case():                                
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกฟอร์ม หรือจำลองการทำงาน
    """
    try:
        
        log_handler("automation_test", log_level="INFO", log_message="เริ่มการทดสอบ...")
        # คลิกปุ่มกรอกบาร์โค้ด
        click((740, 149), delay=5, description="คลิกปุ่มกรอกบาร์โค้ด")
        log_handler("automation_test", log_level="INFO", log_message="คลิกปุ่มกรอกบาร์โค้ดสำเร็จ")

        # กรอกรหัสบาร์โค้ด
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("0105544096014", delay=3, description="กรอกบาร์โค้ด")
        pyautogui.press('enter')

        log_handler("automation_test", log_level="INFO", log_message="กรอกรหัสบาร์โค้ดสำเร็จ")

        time.sleep(20)


        click((361, 339), delay=5, description="คลิกเลือกประกันอีซี่")
        log_handler("automation_test", log_level="INFO", log_message="คลิกเลือกประกันอีซี่สำเร็จ")
        time.sleep(10)
     
        click((414, 553), delay=5, description="คลิกเลือกคีย์เลขที่บัตร")
        log_handler("automation_test", log_level="INFO", log_message="คลิกเลือกคีย์เลขที่บัตรสำเร็จ")

        # click((404, 539), delay=5, description="คลิกเลือกกรอกบัตรประชาชน")
        # log_handler("automation_test", log_level="INFO", log_message="คลิกเลือกกรอกบัตรประชาชนสำเร็จ")
        time.sleep(20)
        write_text("0997317464", delay=3, description="กรอกหมายเลขโทรศัพท์")
        log_handler("automation_test", log_level="INFO", log_message="กรอกหมายเลขโทรศัพท์")
        pyautogui.press('enter')

        time.sleep(5)
    
           # กรอกจำนวนเงิน
        amount = 30001  # ตัวอย่างจำนวนเงินที่ต้องการกรอก
        write_text(str(amount), delay=5, description="กรอกจำนวนเงิน")
        log_handler("automation_test", log_level="INFO", log_message="กรอกจำนวนเงินสำเร็จ")
        pyautogui.press('enter')
        if not monitor_image_display("test1.png", timeout=3):
            log_handler("automation_test", log_level="CRITICAL", log_message=f"กรุณาคีย์จำนวนเงิน")
            return
        
        # กดปุ่มยืนยันทำรายการ
        click((680, 646), delay=5, description="กดปุ่มยืนยันทำรายการ")
        log_handler("automation_test", log_level="INFO", log_message="กดปุ่มยืนยันทำรายการสำเร็จ")

        # ตรวจสอบภาพตามจำนวนเงิน
        if amount > 30000:
            if not monitor_image_display("test2.png", timeout=3):
                log_handler("automation_test", log_level="CRITICAL", log_message=f"ไม่สามารถชำระยอด {amount} ได้")
                return
        elif 0.1 <= amount <= 0.99:
            if not monitor_image_display("test1.png", timeout=3):
                log_handler("automation_test", log_level="CRITICAL", log_message=f"ไม่สามารถชำระยอด {amount} ได้")
                return
        elif amount % 1 not in [0.00, 0.25, 0.50, 0.75]:
            if not monitor_image_display("test3.png", timeout=3):
                log_handler("automation_test", log_level="CRITICAL", log_message=f"รับได้เฉพาะจำนวนเงินที่เป็นทศนิยมที่ลงตัวเท่านั้น")
                return
        else:
            log_handler("automation_test", log_level="WARNING", log_message=f"จำนวนเงิน {amount} ไม่อยู่ในเงื่อนไขที่รองรับ")
            return
        click((740, 651), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        log_handler("automation_test", log_level="INFO", log_message="กดปุ่มยืนยันทำรายการสำเร็จ")

        # คลิกปุ่มยืนยัน
        click((690, 651), delay=6, description="กดปุ่มชำระเงิน")
        log_handler("automation_test", log_level="INFO", log_message="กดปุ่มชำระเงินสำเร็จ")

        # คลิกปุ่มรับพอดี
        click((574, 652), delay=8, description="กดปุ่มรับพอดี")
        log_handler("automation_test", log_level="INFO", log_message="กดปุ่มรับพอดีสำเร็จ")

        # คลิกปุ่มยืนยันการชำระเงิน
        click((470, 425), delay=4, description="กดปุ่มยืนยันชำระเงิน")
        log_handler("automation_test", log_level="INFO", log_message="การชำระเงินเสร็จสมบูรณ์")

        log_handler("automation_test", log_level="INFO", log_message="การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        log_handler("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        raise

if __name__ == "__main__":
    main()
