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


def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าระบบก่อนเริ่มการทดสอบ
    """
    log_handler("automation_test", log_level="INFO", log_message="เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    log_handler("automation_test", log_level="INFO", log_message="การตั้งค่าเสร็จสิ้น")


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
            if pyautogui.locateOnScreen(image_path, confidence=0.6):
                log_handler("automation_test", log_level="INFO", log_message="พบภาพที่คาดหวังแล้ว")
                return True  # พบภาพที่ต้องการแล้ว
        except Exception as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดในการตรวจสอบภาพ: {e}")
            return False  # หากเกิดข้อผิดพลาดในการจับภาพ

        time.sleep(0.5)  # หน่วงเวลาเล็กน้อยก่อนตรวจสอบครั้งถัดไป

    # หากครบเวลาและยังไม่พบภาพ
    log_handler("automation_test", log_level="WARNING", log_message="ไม่พบภาพที่ต้องการภายในเวลาที่กำหนด")
    return False


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

        if not monitor_image_display("EDC1.png"):  # ตรวจสอบภาพหลังจากกรอกบาร์โค้ด
            log_handler("automation_test", log_level="ERROR", log_message="ข้อมูลไม่ถูกต้อง")
            return
         
        click((361, 339), delay=5, description="คลิกเลือกประกันอีซี่")
        log_handler("automation_test", log_level="INFO", log_message="คลิกเลือกประกันอีซี่สำเร็จ")
        time.sleep(10)
        
        click((414, 553), delay=5, description="คลิกเลือกคีย์เลขที่บัตร")
        log_handler("automation_test", log_level="INFO", log_message="คลิกเลือกคีย์เลขที่บัตรสำเร็จ")

        click((404, 539), delay=5, description="คลิกเลือกกรอกบัตรประชาชน")
        log_handler("automation_test", log_level="INFO", log_message="คลิกเลือกกรอกบัตรประชาชนสำเร็จ")
        time.sleep(20)
        write_text("0997317465", delay=3, description="กรอกหมายเลขโทรศัพท์")
        log_handler("automation_test", log_level="INFO", log_message="กรอกหมายเลขโทรศัพท์")
        pyautogui.press('enter')

        time.sleep(5)
    
        write_text("100", delay=5, description="กรอกจำนวนเงิน")
        log_handler("automation_test", log_level="INFO", log_message="กรอกจำนวนเงินสำเร็จ")

        click((680, 646), delay=5, description="กดปุ่มยืนยันทำรายการ")
        click((740, 651), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        log_handler("automation_test", log_level="INFO", log_message="กดปุ่มยืนยันทำรายการสำเร็จ")

        click((690, 651), delay=6, description="กดปุ่มยืนยันชำระเงิน")
        log_handler("automation_test", log_level="INFO", log_message="กดปุ่มชำระเงินสำเร็จ")

        # คลิกปุ่มรับพอดี
        click((574, 652), delay=8, description="กดปุ่มรับพอดี")
        log_handler("automation_test", log_level="INFO", log_message="กดปุ่มรับพอดีสำเร็จ")

        # คลิกปุ่มยืนยันการชำระเงิน
        click((522, 454), delay=4, description="กดปุ่มยืนยันการชำระเงิน")

        log_handler("automation_test", log_level="INFO", log_message="การชำระเงินเสร็จสมบูรณ์")

        log_handler("automation_test", log_level="INFO", log_message="การทดสอบเสร็จสมบูรณ์")
    except Exception as e:
        log_handler("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        raise


if __name__ == "__main__":
    main()