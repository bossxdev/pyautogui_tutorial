# นำเข้าไลบรารีที่จำเป็น
import pyautogui
import time  # ใช้สำหรับหน่วงเวลา (delay)
import os  # ใช้สำหรับจัดการโฟลเดอร์

# ฟังก์ชันหลักสำหรับทดสอบระบบ
def main():
    """
    ฟังก์ชันหลักที่ใช้ในการควบคุมการทำงานของ Automated Test
    """
    try:
        # 1. การตั้งค่าเบื้องต้น
        setup_environment()

        # 2. ขั้นตอนการทดสอบ
        run_test_case()

    except Exception as e:
        print(f"เกิดข้อผิดพลาดระหว่างการทดสอบ: {e}")

# ฟังก์ชันสำหรับการตั้งค่าเริ่มต้น
def setup_environment():
    """
    ฟังก์ชันสำหรับตั้งค่าการทดสอบ เช่น เปิดแอปพลิเคชันหรือเตรียมหน้าต่าง
    """
    print("เริ่มต้นการตั้งค่าระบบ...")
    time.sleep(2)
    print("การตั้งค่าเสร็จสิ้น")

# ฟังก์ชันสำหรับถ่ายสกรีนช็อตและบันทึก
def take_screenshot(step_name):
    """
    ถ่ายสกรีนช็อตหน้าจอปัจจุบันและบันทึกลงในโฟลเดอร์
    :param step_name: ชื่อขั้นตอนสำหรับตั้งชื่อไฟล์
    """
    # สร้างโฟลเดอร์สำหรับเก็บสกรีนช็อต
    folder_name = "screenshots"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # ตั้งชื่อไฟล์
    file_path = os.path.join(folder_name, f"{step_name}.png")

    # ถ่ายภาพหน้าจอ
    screenshot = pyautogui.screenshot()
    screenshot.save(file_path)

    print(f"บันทึกสกรีนช็อต: {file_path}")

# ฟังก์ชันสำหรับขั้นตอนการทดสอบ
def run_test_case():
    """
    ฟังก์ชันสำหรับรันขั้นตอนการทดสอบ เช่น คลิกปุ่ม กรอกฟอร์ม หรือจำลองการทำงาน
    """
    print("เริ่มการทดสอบ...")

    # Step 1: คลิกที่พิกัดแรก
    pyautogui.moveTo(746, 134)
    pyautogui.click(button="left")
    take_screenshot("step_1_click_first_coordinate")
    time.sleep(3)

    # Step 2: พิมพ์ข้อความ
    pyautogui.keyDown('shift')
    pyautogui.press('\\')
    pyautogui.keyUp('shift')
    pyautogui.write("0993000177967")
    take_screenshot("step_2_input_text")
    time.sleep(2)

    # Step 3: คลิกพิกัดที่สอง
    pyautogui.click(479, 456, button="left")
    take_screenshot("step_3_click_second_coordinate")
    time.sleep(20)

    # Step 4: คลิกและกรอกจำนวนเงิน
    pyautogui.click(377, 559, button="left")
    pyautogui.write("3500")
    take_screenshot("step_4_input_amount")
    time.sleep(3)

    # Steps 5-8: คลิกที่พิกัดต่างๆ
    pyautogui.click(679, 641, button="left")
    take_screenshot("step_5_click_coordinate_1")
    time.sleep(5)

    pyautogui.click(729, 646, button="left")
    take_screenshot("step_6_click_coordinate_2")
    time.sleep(5)

    pyautogui.click(671, 644, button="left")
    take_screenshot("step_7_click_coordinate_3")
    time.sleep(5)

    pyautogui.click(560, 639, button="left")
    take_screenshot("step_8_click_coordinate_4")
    time.sleep(5)

    # Step 9: คลิกปุ่มสุดท้าย
    pyautogui.click(486, 427, button="left")
    take_screenshot("step_9_final_click")

    print("การทดสอบเสร็จสมบูรณ์")

if __name__ == "__main__":
    main()
