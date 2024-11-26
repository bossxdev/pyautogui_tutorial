---

# **Automated Test Template with PyAutoGUI**

เทมเพลตนี้ถูกออกแบบมาเพื่อช่วยให้คุณเริ่มต้นเขียน Automated Test ด้วย PyAutoGUI ได้ง่ายและเป็นระเบียบ เหมาะสำหรับผู้ที่ต้องการทดสอบ GUI ของแอปพลิเคชันอย่างมีประสิทธิภาพ

---

## **โครงสร้างของเทมเพลต**

เทมเพลตนี้มี 4 ส่วนสำคัญที่ช่วยให้การเขียนโค้ดมีความชัดเจนและเป็นระบบ ดังนี้:

### 1. **การตั้งค่าเบื้องต้น (setup_environment)**
ฟังก์ชันสำหรับเตรียมสภาพแวดล้อม เช่น:
- เปิดโปรแกรมที่ต้องการทดสอบ
- จัดเรียงหน้าต่างหรือ UI ให้พร้อมก่อนเริ่มกระบวนการทดสอบ

### 2. **การดำเนินการทดสอบ (run_test_case)**
ฟังก์ชันนี้รวมทุกขั้นตอนที่ต้องการทดสอบ เช่น:
- การเลื่อนเมาส์
- คลิกปุ่ม
- พิมพ์ข้อความ
- การโต้ตอบกับหน้าจอในรูปแบบต่างๆ

### 3. **การตรวจสอบผลลัพธ์ (verify_results)**
ฟังก์ชันที่ใช้ยืนยันผลลัพธ์การทดสอบ เช่น:
- การจับภาพหน้าจอ
- การเปรียบเทียบข้อมูลหรือข้อความที่แสดงผล

### 4. **การคืนค่าระบบ (cleanup)**
ฟังก์ชันสำหรับคืนค่าสภาพแวดล้อมหลังการทดสอบ เช่น:
- ปิดโปรแกรมหรือหน้าต่าง
- คืนค่าหน้าจอให้เหมือนเดิม

---

## **วิธีการติดตั้ง**

### 1. **สร้าง Virtual Environment**
ในการเริ่มต้น ควรสร้าง Virtual Environment เพื่อแยกการทำงานของไลบรารีต่างๆ ออกจากระบบหลัก:
```bash
python -m venv venv
```

### 2. **เปิดใช้งาน Virtual Environment**
- **Windows**:
    ```bash
    venv\Scripts\activate
    ```
- **macOS/Linux**:
    ```bash
    source venv/bin/activate
    ```

### 3. **ติดตั้งไลบรารีที่จำเป็น**
ติดตั้ง PyAutoGUI ใน Virtual Environment:
```bash
pip install pyautogui
```

---

## **วิธีใช้งาน**

1. **แก้ไขโค้ดตามความต้องการ**  
   - กำหนดพิกัด (x, y) ที่เหมาะสมสำหรับ UI ของแอปพลิเคชันของคุณ
   - เพิ่มขั้นตอนการทดสอบที่เฉพาะเจาะจงในฟังก์ชัน `run_test_case`

2. **รันสคริปต์**  
   ใช้คำสั่งเพื่อเริ่มต้นการทดสอบ:
   ```bash
   python your_script_name.py
   ```

3. **ปิด Virtual Environment**  
   เมื่อใช้งานเสร็จสิ้น ให้ปิด Virtual Environment:
   ```bash
   deactivate
   ```

---

## **ลิงก์เอกสารของ PyAutoGUI**
สำหรับข้อมูลเพิ่มเติมเกี่ยวกับ PyAutoGUI และวิธีการใช้งานคำสั่งต่างๆ สามารถศึกษาได้ที่ลิงก์ด้านล่าง:
- [PyAutoGUI Documentation (ภาษาอังกฤษ)](https://pyautogui.readthedocs.io/en/latest/)

---

## **ตัวอย่างโค้ด**
```python
# นำเข้าไลบรารีที่จำเป็น
import pyautogui
import time

def setup_environment():
    print("เริ่มต้นการตั้งค่าระบบ...")
    # ตั้งค่าการเปิดแอปพลิเคชัน
    time.sleep(2)
    print("การตั้งค่าเสร็จสิ้น")

def run_test_case():
    print("เริ่มการทดสอบ...")
    pyautogui.moveTo(500, 500)
    pyautogui.click()
    pyautogui.write("ทดสอบการพิมพ์ข้อความ", interval=0.1)
    pyautogui.press('enter')
    print("การทดสอบเสร็จสมบูรณ์")

def verify_results():
    print("เริ่มการตรวจสอบผลลัพธ์...")
    screenshot = pyautogui.screenshot()
    screenshot.save("test_result.png")
    print("การตรวจสอบเสร็จสิ้น")

def cleanup():
    print("คืนค่าระบบ...")
    print("กระบวนการคืนค่าระบบเสร็จสิ้น")

if __name__ == "__main__":
    try:
        setup_environment()
        run_test_case()
        verify_results()
    except Exception as e:
        print(f"เกิดข้อผิดพลาด: {e}")
    finally:
        cleanup()
```

---

## **คำแนะนำเพิ่มเติม**
- ปรับค่า `time.sleep()` เพื่อให้เหมาะสมกับเวลาโหลดของระบบที่คุณทดสอบ
- ใช้ `pyautogui.position()` เพื่อตรวจสอบพิกัด (x, y) ของ UI
- จับภาพหน้าจอเพื่อช่วยในการตรวจสอบผลลัพธ์อย่างละเอียด

---

## **License**
โปรเจกต์นี้เผยแพร่ภายใต้ [MIT License](LICENSE)

---
