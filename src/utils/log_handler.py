import logging
import os

def log_handler(log_name: str, log_level: str = "DEBUG", log_message: str = None):
    """
    ฟังก์ชันสำหรับสร้าง Log โดยรับพารามิเตอร์ log_name, level, และ log_message
    :param log_name: ชื่อของ log
    :param log_level: ระดับของ log เช่น 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
    :param log_message: ข้อความที่ต้องการบันทึกเมื่อสร้าง log เสร็จ
    """

    # กำหนดเส้นทางโฟลเดอร์เก็บ log
    log_folder = f"../logs/{log_name}"
    os.makedirs(log_folder, exist_ok=True)  # สร้างโฟลเดอร์ใหม่ถ้ายังไม่มี

    # แปลงระดับ log ที่รับเข้ามาเป็นค่าที่สามารถใช้ได้
    log_levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }

    # ตั้งค่าระดับของ log
    log_level = log_levels.get(log_level.upper(), logging.DEBUG)

    # สร้าง log
    log = logging.getLogger(log_name)

    # ตรวจสอบว่ามี handler อยู่แล้วหรือไม่
    if not log.hasHandlers():
        log.setLevel(log_level)

        # สร้าง StreamHandler สำหรับแสดงผลใน console
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(log_level)
        stream_handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        )
        log.addHandler(stream_handler)

        # สร้างชื่อไฟล์ log ตามวันที่และเวลา
        log_filename = f"{log_folder}/{log_name}_logfile.log"

        # สร้าง FileHandler สำหรับบันทึก log ลงไฟล์
        file_handler = logging.FileHandler(log_filename, encoding="utf-8")
        file_handler.setLevel(log_level)  # ใช้ log level ที่ได้จากพารามิเตอร์
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        )
        log.addHandler(file_handler)

    # บันทึก log message ถ้ามีการระบุ
    if log_message: log.log(log_level, log_message)
