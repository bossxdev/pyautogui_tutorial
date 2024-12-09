import logging
from datetime import datetime
import os

def log_handler(logger_name: str, level: str = "DEBUG", log_message: str = None):
    """
    ฟังก์ชันสำหรับสร้าง Logger โดยรับพารามิเตอร์ logger_name, level, และ log_message
    :param logger_name: ชื่อของ logger
    :param level: ระดับของ log เช่น 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
    :param log_message: ข้อความที่ต้องการบันทึกเมื่อสร้าง logger เสร็จ
    :return: logger ที่ตั้งค่าเรียบร้อยแล้ว
    """
    # กำหนดเส้นทางโฟลเดอร์เก็บ log
    os.makedirs("../logs/", exist_ok=True)

    # แปลงระดับ log ที่รับเข้ามาเป็นค่าที่สามารถใช้ได้
    log_levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }

    # ตั้งค่าระดับของ logger
    log_level = log_levels.get(level.upper(), logging.DEBUG)

    # สร้าง logger
    logger = logging.getLogger(logger_name)

    # ตรวจสอบว่ามี handler อยู่แล้วหรือไม่
    if not logger.hasHandlers():
        logger.setLevel(log_level)

        # สร้าง StreamHandler สำหรับแสดงผลใน console
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(log_level)
        stream_handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s")
        )
        logger.addHandler(stream_handler)

        # สร้างชื่อไฟล์ log ตามวันที่และเวลา
        current_time = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
        log_filename = f"../logs/{logger_name}_logfile.log"

        # สร้าง FileHandler สำหรับบันทึก log ลงไฟล์
        file_handler = logging.FileHandler(log_filename, encoding="utf-8")
        file_handler.setLevel(log_level)  # ใช้ log level ที่ได้จากพารามิเตอร์
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s")
        )
        logger.addHandler(file_handler)

    # บันทึก log message ถ้ามีการระบุ
    if log_message: logger.log(log_level, log_message)

    return logger