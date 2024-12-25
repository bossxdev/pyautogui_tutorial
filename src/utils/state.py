import logging

import os
import pyautogui
from datetime import datetime

from src.constants.constant import PATH


def critical_level_validate(script_name: str):
    log_image = f"{PATH['LOG']}{script_name}"
    os.makedirs(log_image, exist_ok=True)

    screenshot = pyautogui.screenshot()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    screenshot.save(f"{log_image}/{script_name}_image-file_{timestamp}.png")


def state(script_name: str, level: str = "DEBUG", message: str = None):
    """
    ฟังก์ชันสำหรับสร้าง Log โดยรับพารามิเตอร์ script_name, level, และ message
    :param script_name: ชื่อของ log
    :param level: ระดับของ log เช่น 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
    :param message: ข้อความที่ต้องการบันทึกเมื่อสร้าง log เสร็จ
    """

    log_folder = f"{PATH['LOG']}{script_name}"
    os.makedirs(log_folder, exist_ok=True)

    # แปลงระดับ log ที่รับเข้ามาเป็นค่าที่สามารถใช้ได้
    levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR, # input error
        "CRITICAL": logging.CRITICAL, # program hang
    }

    level = levels.get(level.upper(), logging.DEBUG)

    log = logging.getLogger(script_name)

    # ตรวจสอบว่ามี handler อยู่แล้วหรือไม่
    if not log.hasHandlers():

        if level == logging.CRITICAL:
            critical_level_validate(script_name)
            log.setLevel(level)
        else:
            log.setLevel(level)

        # สร้าง StreamHandler สำหรับแสดงผลใน console
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        )
        log.addHandler(stream_handler)

        # สร้างชื่อไฟล์ log ตามวันที่และเวลา
        log_filename = f"{log_folder}/{script_name}_logfile.log"

        # สร้าง FileHandler สำหรับบันทึก log ลงไฟล์
        file_handler = logging.FileHandler(log_filename, encoding="utf-8")
        file_handler.setLevel(level)  # ใช้ log level ที่ได้จากพารามิเตอร์
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        )
        log.addHandler(file_handler)

    # บันทึก log message ถ้ามีการระบุ
    if message: log.log(level, message)
