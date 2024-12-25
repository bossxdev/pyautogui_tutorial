import pyautogui
import time
from src.utils.utility_func import click, write_text
from src.utils.state import state


def main():
    """
    ฟังก์ชันหลักสำหรับการควบคุมการทำงานของ Automated Test
    """
    try:
        state("automation_test", log_level="DEBUG", message="เริ่มต้นการทำงาน Automated Testdddd")
        setup_environment()
        run_test_case()
        
    except Exception as e:
        state("automation_test", log_level="ERROR", message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        print(f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")


def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าระบบก่อนเริ่มการทดสอบ
    """
    state("automation_test", log_level="INFO", message="เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    state("automation_test", log_level="INFO", message="การตั้งค่าเสร็จสิ้น")


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
                state("automation_test", log_level="INFO", message="พบภาพที่คาดหวังแล้ว")
                return True  # พบภาพที่ต้องการแล้ว
        except Exception as e:
            state("automation_test", log_level="ERROR", message=f"เกิดข้อผิดพลาดในการตรวจสอบภาพ: {e}")
            return False  # หากเกิดข้อผิดพลาดในการจับภาพ

        time.sleep(0.5)  # หน่วงเวลาเล็กน้อยก่อนตรวจสอบครั้งถัดไป

    # หากครบเวลาและยังไม่พบภาพ
    state("automation_test", log_level="WARNING", message="ไม่พบภาพที่ต้องการภายในเวลาที่กำหนด")
    return False


def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกฟอร์ม หรือจำลองการทำงาน
    """
    try:
        
        state("automation_test", log_level="INFO", message="เริ่มการทดสอบ...")
        # คลิกปุ่มกรอกบาร์โค้ด
        click((740, 149), delay=5, description="คลิกปุ่มกรอกบาร์โค้ด")
        state("automation_test", log_level="INFO", message="คลิกปุ่มกรอกบาร์โค้ดสำเร็จ")

        # กรอกรหัสบาร์โค้ด
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("0105544096014", delay=3, description="กรอกบาร์โค้ด")
        pyautogui.press('enter')

        state("automation_test", log_level="INFO", message="กรอกรหัสบาร์โค้ดสำเร็จ")

        time.sleep(20)

        if not monitor_image_display("EDC1.png"):  # ตรวจสอบภาพหลังจากกรอกบาร์โค้ด
            state("automation_test", log_level="ERROR", message="ข้อมูลไม่ถูกต้อง")
            return
         
        click((361, 339), delay=5, description="คลิกเลือกประกันอีซี่")
        state("automation_test", log_level="INFO", message="คลิกเลือกประกันอีซี่สำเร็จ")
        time.sleep(10)
        
        click((414, 553), delay=5, description="คลิกเลือกคีย์เลขที่บัตร")
        state("automation_test", log_level="INFO", message="คลิกเลือกคีย์เลขที่บัตรสำเร็จ")

        click((404, 539), delay=5, description="คลิกเลือกกรอกบัตรประชาชน")
        state("automation_test", log_level="INFO", message="คลิกเลือกกรอกบัตรประชาชนสำเร็จ")
        time.sleep(20)
        write_text("0997317465", delay=3, description="กรอกหมายเลขโทรศัพท์")
        state("automation_test", log_level="INFO", message="กรอกหมายเลขโทรศัพท์")
        pyautogui.press('enter')

        time.sleep(5)
    
        write_text("100", delay=5, description="กรอกจำนวนเงิน")
        state("automation_test", log_level="INFO", message="กรอกจำนวนเงินสำเร็จ")

        click((680, 646), delay=5, description="กดปุ่มยืนยันทำรายการ")
        click((740, 651), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        state("automation_test", log_level="INFO", message="กดปุ่มยืนยันทำรายการสำเร็จ")

        click((690, 651), delay=6, description="กดปุ่มยืนยันชำระเงิน")
        state("automation_test", log_level="INFO", message="กดปุ่มชำระเงินสำเร็จ")

        # คลิกปุ่มรับพอดี
        click((574, 652), delay=8, description="กดปุ่มรับพอดี")
        state("automation_test", log_level="INFO", message="กดปุ่มรับพอดีสำเร็จ")

        # คลิกปุ่มยืนยันการชำระเงิน
        click((522, 454), delay=4, description="กดปุ่มยืนยันการชำระเงิน")

        state("automation_test", log_level="INFO", message="การชำระเงินเสร็จสมบูรณ์")

        state("automation_test", log_level="INFO", message="การทดสอบเสร็จสมบูรณ์")
    except Exception as e:
        state("automation_test", log_level="ERROR", message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        raise


if __name__ == "__main__":
    main()
