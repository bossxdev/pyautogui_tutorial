import logging
import os
import pyautogui

import os
import pyautogui
from datetime import datetime


def critical_level_validate(log_name: str):
    log_image = f"../logs/{log_name}"
    os.makedirs(log_image, exist_ok=True)

    screenshot = pyautogui.screenshot()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    screenshot.save(f"{log_image}/{log_name}_image-file_{timestamp}.png")


def log_handler(log_name: str, log_level: str = "DEBUG", log_message: str = None):
    """
    ฟังก์ชันสำหรับสร้าง Log โดยรับพารามิเตอร์ log_name, level, และ log_message
    :param log_name: ชื่อของ log
    :param log_level: ระดับของ log เช่น 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
    :param log_message: ข้อความที่ต้องการบันทึกเมื่อสร้าง log เสร็จ
    """

    log_folder = f"../logs/{log_name}"
    os.makedirs(log_folder, exist_ok=True)

    # แปลงระดับ log ที่รับเข้ามาเป็นค่าที่สามารถใช้ได้
    log_levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL,
    }

    log_level = log_levels.get(log_level.upper(), logging.DEBUG)

    log = logging.getLogger(log_name)

    # ตรวจสอบว่ามี handler อยู่แล้วหรือไม่
    if not log.hasHandlers():

        if log_level == logging.CRITICAL:
            critical_level_validate(log_name)
            log.setLevel(log_level)
        else:
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
