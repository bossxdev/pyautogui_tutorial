import pyautogui
import time

def main():
    try:
        setup_environment()
        run_test_case()
    except Exception as e:
        print(f"[ERROR] เกิดข้อผิดพลาดในโปรแกรมหลัก: {e}")

def setup_environment():
    print("[INFO] เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    print("[INFO] การตั้งค่าเสร็จสิ้น")

def log_action(action, details):
    print(f"[LOG] {action}: {details}")

def click(position, delay=2, button="left", description=""):
    try:
        log_action("Click", f"ตำแหน่ง {position} {description}")
        pyautogui.click(*position, button=button)
        time.sleep(delay)
    except Exception as e:
        log_action("Error", f"เกิดข้อผิดพลาดในการคลิกตำแหน่ง {position}: {e}")
        raise

def write_text(text, delay=2, description=""):
    try:
        log_action("Write", f"พิมพ์ข้อความ: {text} {description}")
        pyautogui.write(text)
        time.sleep(delay)
    except Exception as e:
        log_action("Error", f"เกิดข้อผิดพลาดในการพิมพ์ข้อความ {text}: {e}")
        raise

def run_test_case():
    try:
        print("[INFO] เริ่มการทดสอบ...")

        click((746, 134), delay=3, description="คลิกปุ่มกรอกบาร์โค้ด")

        log_action("Write", "พิมพ์อักษรพิเศษ | ")
        pyautogui.keyDown('shift')
        pyautogui.press('\\')
        pyautogui.keyUp('shift')
        write_text("0993000070241", delay=2, description="กรอกบาร์โค้ด")

        click((479, 456), delay=10, description="คลิกปุ่มยืนยัน pop up บาร์โค้ด")

        click((370, 275), delay=20, description="คลิกเลือก service")

        write_text("5000", delay=3, description="กรอกจำนวนเงิน")

        click((668, 637), delay=5, description="กดปุ่มยืนยันทำรายการ")
        
        click((750, 636), delay=5, description="กดปุ่มยืนยันหน้าทวนข้อมูล")
        
        click((675, 636), delay=5, description="กดปุ่มชำระเงิน")
        
        click((558, 633), delay=5, description="กดปุ่มรับพอดี")
        
        click((490, 430), delay=5, description="กดปุ่มยืนยันชำระเงิน")

        print("[INFO] การทดสอบเสร็จสมบูรณ์")

    except Exception as e:
        log_action("Error", f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")
        raise

if __name__ == "__main__":
    main()
