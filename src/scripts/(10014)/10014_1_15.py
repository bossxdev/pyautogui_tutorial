import pyautogui
import time
from src.utils.utility_func import click, write_text
from src.utils.log_handler import log_handler

def main():
    """
    ฟังก์ชันหลักสำหรับการควบคุมการทำงานของ Automated Test
    """
    try:
        log_handler("automation_test", log_level="DEBUG", log_message="เริ่มต้นการทำงาน Automated Test")
        setup_environment()
        run_test_case()
    except Exception as e:
        log_handler("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        print(f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")

def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าระบบก่อนเริ่มการทดสอบ
    """
    try:
        log_handler("automation_test", log_level="INFO", log_message="เริ่มต้นการตั้งค่าระบบ...")
        time.sleep(2)
        log_handler("automation_test", log_level="INFO", log_message="การตั้งค่าเสร็จสิ้น")
    except Exception as e:
        log_handler("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดระหว่างการตั้งค่าระบบ: {e}")
        raise

def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกฟอร์ม หรือดำเนินการชำระเงิน
    """
    try:
        log_handler("automation_test", log_level="INFO", log_message="เริ่มการทดสอบ...")

        # คลิกปุ่มกรอกบาร์โค้ด
        try:
            click((740, 149), delay=5, description="คลิกปุ่มกรอกบาร์โค้ด")
            log_handler("automation_test", log_level="INFO", log_message="คลิกปุ่มกรอกบาร์โค้ดสำเร็จ")
        except pyautogui.FailSafeException as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"ข้อผิดพลาดจากการคลิกปุ่มกรอกบาร์โค้ด: {e}")
            raise
        except Exception as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดในการคลิกปุ่มกรอกบาร์โค้ด: {e}")
            raise

        # กรอกรหัสบาร์โค้ด
        try:
            pyautogui.keyDown('shift')
            pyautogui.press('\\')
            pyautogui.keyUp('shift')
            write_text("010753700137401", delay=2, description="กรอกรหัสบาร์โค้ด")
            pyautogui.press('enter')
            log_handler("automation_test", log_level="INFO", log_message="กรอกรหัสบาร์โค้ดสำเร็จ")
        except pyautogui.FailSafeException as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"ข้อผิดพลาดจากการกรอกรหัสบาร์โค้ด: {e}")
            raise
        except Exception as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดในการกรอกรหัสบาร์โค้ด: {e}")
            raise

        time.sleep(5)

        # กรอกรหัสลูกค้า
        try:
            write_text("123456789", delay=4, description="กรอกรหัสลูกค้า")
            log_handler("automation_test", log_level="INFO", log_message="กรอกรหัสลูกค้าสำเร็จ")
            pyautogui.press('enter')
        except pyautogui.FailSafeException as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"ข้อผิดพลาดจากการกรอกรหัสลูกค้า: {e}")
            raise
        except Exception as e:
            if "กรุณาคีย์ รหัสลูกค้า" in str(e):
                log_handler("automation_test", log_level="ERROR", log_message=f"กรุณาคีย์ รหัสลูกค้า: {e}")
            else:
                log_handler("automation_test", log_level="ERROR", log_message=f"ข้อมูลไม่ถูกต้อง: {e}")
            raise

        # กรอกเลขผู้เสียภาษี
        try:
            write_text("1234567893434", delay=4, description="กรอกเลขผู้เสียภาษี")
            log_handler("automation_test", log_level="INFO", log_message="กรอกเลขผู้เสียภาษีสำเร็จ")
            pyautogui.press('enter')
        except pyautogui.FailSafeException as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"ข้อผิดพลาดจากการกรอกเลขผู้เสียภาษี: {e}")
            
        except Exception as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"ข้อมูลไม่ถูกต้อง: {e}")
            raise

        time.sleep(20)

        # กรอกจำนวนเงิน
        try:
            write_text("30000", delay=4, description="กรอกจำนวนเงิน")
            log_handler("automation_test", log_level="INFO", log_message="กรอกจำนวนเงินสำเร็จ")
        except pyautogui.FailSafeException as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"ข้อผิดพลาดจากการกรอกจำนวนเงิน: {e}")
            raise
        except Exception as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดในการกรอกจำนวนเงิน: {e}")
            raise

        # คลิกปุ่มยืนยันทำรายการ
        try:
            click((680, 646), delay=5, description="กดปุ่มยืนยันทำรายการ")
            click((740, 651), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
            log_handler("automation_test", log_level="INFO", log_message="กดปุ่มยืนยันทำรายการสำเร็จ")
        except pyautogui.FailSafeException as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"ข้อผิดพลาดจากการคลิกปุ่มยืนยันทำรายการ: {e}")
            raise
        except Exception as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดในการยืนยันทำรายการ: {e}")
            raise

        # คลิกปุ่มยืนยันชำระเงิน
        try:
            click((690, 651), delay=6, description="กดปุ่มยืนยันชำระเงิน")
            log_handler("automation_test", log_level="INFO", log_message="กดปุ่มชำระเงินสำเร็จ")
        except pyautogui.FailSafeException as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"ข้อผิดพลาดจากการคลิกปุ่มยืนยันชำระเงิน: {e}")
            raise
        except Exception as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดในการยืนยันชำระเงิน: {e}")
            raise

        # คลิกปุ่มรับพอดี
        try:
            click((574, 652), delay=8, description="กดปุ่มรับพอดี")
            log_handler("automation_test", log_level="INFO", log_message="กดปุ่มรับพอดีสำเร็จ")
        except pyautogui.FailSafeException as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"ข้อผิดพลาดจากการคลิกปุ่มรับพอดี: {e}")
        except Exception as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดในการคลิกปุ่มรับพอดี: {e}")
            raise

        # คลิกปุ่มยืนยันการชำระเงิน
        try:
            click((522, 454), delay=4, description="กดปุ่มยืนยันการชำระเงิน")
            log_handler("automation_test", log_level="INFO", log_message="การชำระเงินเสร็จสมบูรณ์")
        except pyautogui.FailSafeException as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"ข้อผิดพลาดจากการคลิกปุ่มยืนยันการชำระเงิน: {e}")
            raise
        except Exception as e:
            log_handler("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดในการยืนยันการชำระเงิน: {e}")
            raise

        log_handler("automation_test", log_level="INFO", log_message="การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        log_handler("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        raise

if __name__ == "__main__":
    main()
