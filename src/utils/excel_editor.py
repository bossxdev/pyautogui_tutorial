from openpyxl import load_workbook
from datetime import datetime
import os

from src.constants.constant import NSS_COMMENT_COLUMN, PATH, NSS_EXCEL_FILE


def load_workbook_file(file_path):
    """
    โหลดไฟล์ Excel และส่งคืน workbook กับ sheet
    """
    try:
        wb = load_workbook(file_path)
        sheet = wb.active
        return wb, sheet
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการโหลดไฟล์ Excel: {str(e)}")
        return None, None


def update_multiple_cells(file_path, updates):
    """
    อัพเดทข้อมูลหลายเซลล์ในไฟล์ Excel
    """
    wb, sheet = load_workbook_file(file_path)
    if not wb:
        return False

    try:
        for update in updates:
            sheet.cell(row=update["row"], column=update["column"], value=update["value"])
        return wb
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการอัพเดทข้อมูล: {str(e)}")
        return None


def export_excel(wb, file_path, export_path=None):
    """
    Export ไฟล์ Excel พร้อมระบุชื่อไฟล์
    """
    try:
        if not export_path:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            export_path = f"{file_name}_exported_{timestamp}.xlsx"

        export_dir = f"{PATH['EXPORT']}"
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)

        full_export_path = os.path.join(export_dir, export_path)

        wb.save(full_export_path)
        print(f"ไฟล์ถูก export ไปยัง: {full_export_path}")
        return True
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการ export ไฟล์: {str(e)}")
        return False


def save_and_close(wb):
    """
    บันทึกการเปลี่ยนแปลงและปิดไฟล์
    """
    try:
        if wb:
            # wb.save(file_path)  # ถ้าต้องการบันทึกในไฟล์เดิม
            wb.close()
            print(f"บันทึกการเปลี่ยนแปลงและปิดไฟล์เรียบร้อยแล้ว")
            return True
    except Exception as e:
        print(f"เกิดข้อผิดพลาดในการบันทึกไฟล์: {str(e)}")
        return False


if __name__ == "__main__":
    file_path = f"{PATH['ASSET']}{NSS_EXCEL_FILE}"
    updates = [
        {"row": 667, "column": NSS_COMMENT_COLUMN, "value": "Test_Comment_1"},
        {"row": 740, "column": NSS_COMMENT_COLUMN, "value": "Test_Comment_2"},
    ]

    wb = update_multiple_cells(file_path, updates)
    if wb:
        if export_excel(wb, file_path):
            save_and_close(wb)
