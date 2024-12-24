from openpyxl import load_workbook
from datetime import datetime
import os

from src.constants.constant import NSS_COMMENT_COLUMN, PATH, NSS_EXCEL_FILE


class ExcelEditor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.wb = None
        self.sheet = None

    def load_workbook(self):
        try:
            self.wb = load_workbook(self.file_path)
            self.sheet = self.wb.active
            return True
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการโหลดไฟล์ Excel อาจมีการเสียหายหรือไม่สมบูรณ์: {str(e)}")
            return False

    def update_multiple_cells(self, updates):
        try:
            if not self.wb:
                if not self.load_workbook():
                    return False

            for update in updates:
                self.sheet.cell(
                    row=update["row"],
                    column=update["column"],
                    value=update["value"]
                )
            return True
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการอัพเดทข้อมูล: {str(e)}")
            return False

    def export_excel(self, export_path=None):
        try:
            if not self.wb:
                if not self.load_workbook():
                    return False

            if not export_path:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                file_name = os.path.splitext(os.path.basename(self.file_path))[0]
                export_path = f"{file_name}_exported_{timestamp}.xlsx"

            export_dir = f"{PATH['EXPORT']}"
            if not os.path.exists(export_dir):
                os.makedirs(export_dir)

            full_export_path = os.path.join(export_dir, export_path)

            self.wb.save(full_export_path)
            print(f"ไฟล์ถูก export ไปยัง: {full_export_path}")
            return True

        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการ export ไฟล์: {str(e)}")
            return False

    def save_and_close(self):
        try:
            if self.wb:
                # self.wb.save(self.file_path)
                self.wb.close()
                print(f"บันทึกการเปลี่ยนแปลงในไฟล์ {self.file_path} เรียบร้อยแล้ว")
                return True
        except Exception as e:
            print(f"เกิดข้อผิดพลาดในการบันทึกไฟล์: {str(e)}")
            return False


if __name__ == "__main__":
    file_path = f"{PATH['ASSET']}{NSS_EXCEL_FILE}"
    excel_ops = ExcelEditor(file_path)
    updates = [
        {"row": 667, "column": NSS_COMMENT_COLUMN, "value": "Test_Comment_1"},
        {"row": 740, "column": NSS_COMMENT_COLUMN, "value": "Test_Comment_2"},
    ]
    if excel_ops.update_multiple_cells(updates):
        excel_ops.export_excel()
        excel_ops.save_and_close()
