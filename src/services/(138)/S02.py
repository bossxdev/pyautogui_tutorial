import pyautogui
import time
from pygetwindow import getWindowsWithTitle


def main():
    """
    ฟังก์ชันหลักที่ใช้ในการควบคุมการทำงานของ Automated Test
    """
    try:
        setup_environment()
        run_test_case()
    except Exception as e:
        print(f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")


def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าการทดสอบ เช่น เปิดแอปพลิเคชันหรือเตรียมหน้าต่าง
    """
    print("เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    print("การตั้งค่าเสร็จสิ้น")


def check_click_and_verify(x, y, target_image, description):
    """
    คลิกที่ตำแหน่งและตรวจสอบว่าภาพเป้าหมายปรากฏ
    """
    try:
        pyautogui.moveTo(x, y, duration=0.5)
        pyautogui.click(button="left")
        print(f"คลิกสำเร็จ: {description}")
        time.sleep(2)

        if pyautogui.locateOnScreen(target_image, confidence=0.8):
            print(f"ตรวจสอบสำเร็จ: {description}")
        else:
            print(f"ข้อผิดพลาด: {description} - ไม่พบภาพเป้าหมาย")
    except Exception as e:
        print(f"ไม่สามารถคลิกที่ {description} ได้: {e}")


def check_screen_change(description):
    """
    ตรวจสอบว่าหน้าจอเปลี่ยนแปลง
    """
    try:
        screenshot_before = pyautogui.screenshot()
        time.sleep(1)  # ให้เวลาสำหรับระบบในการตอบสนอง
        screenshot_after = pyautogui.screenshot()

        if screenshot_before != screenshot_after:
            print(f"หน้าจอเปลี่ยนแปลงสำเร็จ: {description}")
        else:
            print(f"หน้าจอไม่เปลี่ยนแปลง: {description}")
    except Exception as e:
        print(f"ไม่สามารถตรวจสอบหน้าจอได้: {e}")


def check_window_title(expected_title, description):
    """
    ตรวจสอบว่าหน้าต่างที่เปิดมีชื่อที่ตรงกับเป้าหมาย
    """
    try:
        windows = getWindowsWithTitle(expected_title)
        if windows:
            print(f"พบหน้าต่าง {expected_title}: {description}")
        else:
            print(f"ไม่พบหน้าต่าง {expected_title}: {description}")
    except Exception as e:
        print(f"ไม่สามารถตรวจสอบหน้าต่างได้: {e}")


def run_test_case():
    """
    ขั้นตอนการทดสอบ
    """
    print("เริ่มการทดสอบ...")

    # ขั้นตอนที่ 1: คลิกที่ตำแหน่งและตรวจสอบผลลัพธ์
    check_click_and_verify(740, 149, "expected_image1.png", "เปิดเมนูหลัก")
    time.sleep(8)

    # ขั้นตอนที่ 2: กดปุ่ม Enter และตรวจสอบหน้าจอ
    pyautogui.keyDown('shift')
    pyautogui.press('\\')
    pyautogui.keyUp('shift')
    pyautogui.write("0107542000011")
    time.sleep(2)
    pyautogui.press('enter')
    check_screen_change("กรอกข้อมูลสำเร็จ")
    time.sleep(8)

    # ขั้นตอนที่ 3: คลิกปุ่มอื่น ๆ และตรวจสอบหน้าต่าง
    check_click_and_verify(516, 528, "expected_image2.png", "กดปุ่มดำเนินการ")
    time.sleep(4)

    check_click_and_verify(418, 336, "expected_image3.png", "เปิดหน้าต่างใหม่")
    time.sleep(6)

    pyautogui.write("200")
    time.sleep(4)

    # ขั้นตอนที่ 4: ตรวจสอบปุ่มบันทึก
    check_click_and_verify(680, 646, "save_button.png", "กดปุ่มบันทึก")
    time.sleep(5)

    check_click_and_verify(740, 651, "confirmation_button.png", "ยืนยันการบันทึก")
    time.sleep(5)

    print("การทดสอบเสร็จสมบูรณ์")


if __name__ == "__main__":
    main()
