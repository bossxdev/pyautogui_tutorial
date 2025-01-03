import logging

import os
import pyautogui
from datetime import datetime

from src.constants.constant import PATH, NSS_COMMENT_COLUMN
from src.utils.excel_editor import excel_editor


def critical_level_validate(script_name: str):
    """
    ฟังก์ชันสำหรับตรวจสอบและบันทึกภาพหน้าจอในกรณีที่เกิดข้อผิดพลาดระดับวิกฤติ
    โดยจะสร้างโฟลเดอร์สำหรับบันทึกภาพหน้าจอและบันทึกภาพพร้อมใส่ Timestamp

    Parameters:
    script_name (str): ชื่อสคริปต์ที่ใช้สำหรับตั้งชื่อไฟล์ภาพหน้าจอ
    """
    # สร้างเส้นทางโฟลเดอร์สำหรับเก็บไฟล์ภาพหน้าจอ
    log_image = f"{PATH['LOG']}{script_name}"
    os.makedirs(log_image, exist_ok=True)

    # จับภาพหน้าจอปัจจุบัน
    screenshot = pyautogui.screenshot()

    # สร้าง Timestamp สำหรับเพิ่มในชื่อไฟล์ภาพ
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # บันทึกภาพหน้าจอไปยังโฟลเดอร์ที่กำหนด
    screenshot.save(f"{log_image}/{script_name}_image-file_{timestamp}.png")

    result = {
        "row": script_name,
        "column": NSS_COMMENT_COLUMN,
        "value": "TEST_COMMENT"
    }

    excel_editor(result)


def state(script_name: str, level: str = "DEBUG", message: str = None):
    """
    ฟังก์ชันสำหรับสร้าง Log โดยรับพารามิเตอร์ script_name, level, และ message
    :param script_name: ชื่อของ log
    :param level: ระดับของ log เช่น 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
    :param message: ข้อความที่ต้องการบันทึกเมื่อสร้าง log เสร็จ
    """
    log_folder = f"{PATH['LOG']}{script_name}"
    os.makedirs(log_folder, exist_ok=True)

    try:
        # สร้าง logger
        logger = logging.getLogger(script_name)

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
        logger.setLevel(log_level)

        if log_level == logging.CRITICAL:
            critical_level_validate(script_name)

        # สร้าง StreamHandler สำหรับแสดงผลใน console
        # stream_handler = logging.StreamHandler()
        # stream_handler.setLevel(log_level)
        # stream_handler.setFormatter(
        #     logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        # )
        # log.addHandler(stream_handler)

        # สร้างชื่อไฟล์ log ตามวันที่และเวลา
        log_filename = f"{log_folder}/{script_name}.log"

        # สร้าง FileHandler สำหรับบันทึก log ลงไฟล์
        file_handler = logging.FileHandler(log_filename, encoding="utf-8")
        file_handler.setLevel(log_level)  # ใช้ log level ที่ได้จากพารามิเตอร์
        file_handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)s]  %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
        )
        if not logger.handlers:
            logger.addHandler(file_handler)

        # บันทึก log message ถ้ามีการระบุ
        if message:
            logger.log(log_level, message)

        return logger

    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการสร้าง Logger: {str(e)}")
        return None
