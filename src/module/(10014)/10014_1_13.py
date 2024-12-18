import pyautogui
import time
from src.utils.utility_func import click, write_text
from src.utils.log_handler import log_handler
from pip._vendor.rich import traceback
import traceback  # นำเข้าโมดูล traceback
import os
import cv2

def monitor_image_display(image_path):
    # เริ่มต้นนับเวลา
    start_time = time.time()
    timeout = 20  # เวลารอสูงสุด 20 วินาที

    while time.time() - start_time < timeout:
        print("กำลังตรวจสอบภาพหน้าจอ...")
        try:
            # ใช้ pyautogui.locateOnScreen เพื่อจับภาพหน้าจอและตรวจสอบ
            if pyautogui.locateOnScreen(image_path, confidence=0.8):  # เพิ่มค่าความมั่นใจหรือลดให้เหมาะสม
             log_handler("automation_test", log_level="INFO", log_message=f"เกิดข้อผิดพลาดในการตรวจสอบภาพ: {e}")
 
            return True  # พบภาพที่ต้องการแล้ว
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการจับภาพหน้าจอ: {e}")
            log_handler("automation_test", log_level="ERROR", log_message=f"เกิดข้อผิดพลาดในการตรวจสอบภาพ: {e}")
            return False  # หากเกิดข้อผิดพลาดในการจับภาพ

        time.sleep(1)  # รอ 1 วินาทีแล้วตรวจสอบใหม่

    # หากหมดเวลา 20 วินาทีโดยไม่มีการแสดงผล
    print("ข้อมูลไม่ถูกต้อง หรือหน้าจอไม่แสดงผลลัพธ์ที่คาดหวัง")
    log_handler("automation_test", log_level="ERROR", log_message="ไม่พบภาพที่คาดหวังภายใน 20 วินาที")
    return False

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
    log_handler("automation_test", log_level="INFO", log_message="เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    log_handler("automation_test", log_level="INFO", log_message="การตั้งค่าเสร็จสิ้น")

def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกฟอร์ม หรือดำเนินการชำระเงิน
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
        write_text("0107537001374", delay=2, description="กรอกรหัสบาร์โค้ด")

         # ตรวจสอบภาพหลังจากกรอกรหัสบาร์โค้ด
        if not monitor_image_display("EDC.png"):  # ตรวจสอบภาพหลังจากกรอกบาร์โค้ด
            log_handler("automation_test", log_level="ERROR", log_message="ข้อมูลไม่ถูกต้อง")
            return
        # กดยืนยันบาร์โค้ด
        pyautogui.press('enter')
        log_handler("automation_test", log_level="INFO", log_message="กรอกรหัสบาร์โค้ดสำเร็จ")

        time.sleep(10)
 
        click((361, 339), delay=5, description="คลิกเลือกค่าสินค้าร้านค้า")
        log_handler("S02_15test", log_level="INFO", log_message="คลิกเลือกค่าสินค้าร้านค้า")
        pyautogui.press('enter')
        
        write_text("123456789", delay=4, description="กรอกรหัสลูกค้า")
        log_handler("automation_test", log_level="INFO", log_message="กรอกรหัสลูกค้าสำเร็จ")
        pyautogui.press('enter')

        write_text("1234567893434", delay=4, description="กรอกเลขผู้เสียภาษาษี")
        log_handler("automation_test", log_level="INFO", log_message="กรอกเลขผู้เสียภาษาษีสำเร็จ")
 
        time.sleep(20)

        # กรอกจำนวนเงิน
        write_text("30000", delay=4, description="กรอกจำนวนเงิน")
        log_handler("automation_test", log_level="INFO", log_message="กรอกจำนวนเงินสำเร็จ")

        # คลิกปุ่มยืนยันทำรายการ
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
        # แสดงข้อผิดพลาดที่เกิดขึ้นพร้อมรายละเอียด
        error_message = f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {str(e)}"
        log_handler("automation_test", log_level="ERROR", log_message=error_message)
        
        # แสดง stack trace เพื่อหาสาเหตุของข้อผิดพลาด
        traceback_message = traceback.format_exc()
        log_handler("automation_test", log_level="ERROR", log_message=f"Stack Trace: {traceback_message}")
        
        print(error_message) 
        raise 


if __name__ == "__main__":
    main()
