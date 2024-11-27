import pyautogui
import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab

class MousePositionTracker:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mouse Position Tracker")
        self.root.geometry("400x300")
        
        # ป้องกันการเกิด fail-safe
        pyautogui.FAILSAFE = True
        
        # สร้าง UI
        self.create_widgets()
        
        # เริ่ม tracking
        self.tracking = True
        self.update_position()
        
        self.saved_positions = []
    
    def create_widgets(self):
        # แสดงพิกัดปัจจุบัน
        self.pos_frame = ttk.LabelFrame(self.root, text="ตำแหน่งเมาส์ปัจจุบัน")
        self.pos_frame.pack(pady=10, padx=10, fill="x")
        
        self.pos_label = ttk.Label(self.pos_frame, text="X: 0, Y: 0")
        self.pos_label.pack(pady=5)
        
        self.color_label = ttk.Label(self.pos_frame, text="สี RGB: (0, 0, 0)")
        self.color_label.pack(pady=5)
        
        # ปุ่มบันทึกตำแหน่ง
        self.save_button = ttk.Button(self.root, text="บันทึกตำแหน่งปัจจุบัน", 
                                    command=self.save_position)
        self.save_button.pack(pady=5)
        
        # แสดงตำแหน่งที่บันทึกไว้
        self.saved_frame = ttk.LabelFrame(self.root, text="ตำแหน่งที่บันทึกไว้")
        self.saved_frame.pack(pady=10, padx=10, fill="both", expand=True)
        
        self.saved_text = tk.Text(self.saved_frame, height=5)
        self.saved_text.pack(pady=5, padx=5, fill="both", expand=True)
        
        # ปุ่มหยุด/เริ่ม tracking
        self.toggle_button = ttk.Button(self.root, text="หยุด Tracking", 
                                      command=self.toggle_tracking)
        self.toggle_button.pack(pady=5)
    
    def update_position(self):
        if self.tracking:
            # อ่านพิกัดเมาส์
            x, y = pyautogui.position()
            
            # อ่านสีของพิกเซลที่ตำแหน่งเมาส์
            try:
                screen = ImageGrab.grab(bbox=(x, y, x+1, y+1))
                color = screen.getpixel((0, 0))
                color_text = f"สี RGB: {color}"
            except:
                color_text = "ไม่สามารถอ่านสีได้"
            
            # อัพเดท UI
            self.pos_label.config(text=f"X: {x}, Y: {y}")
            self.color_label.config(text=color_text)
            
            # อัพเดททุก 100ms
            self.root.after(100, self.update_position)
    
    def save_position(self):
        x, y = pyautogui.position()
        position_text = f"X: {x}, Y: {y}\n"
        self.saved_text.insert(tk.END, position_text)
        self.saved_positions.append((x, y))
    
    def toggle_tracking(self):
        self.tracking = not self.tracking
        if self.tracking:
            self.toggle_button.config(text="หยุด Tracking")
            self.update_position()
        else:
            self.toggle_button.config(text="เริ่ม Tracking")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MousePositionTracker()
    app.run()