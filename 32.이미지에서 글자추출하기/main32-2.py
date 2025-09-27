import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract
import os

# macOS에서 Tesseract 경로 설정
pytesseract.pytesseract.tesseract_cmd = '/opt/homebrew/bin/tesseract'

class OCRGUI:
    def __init__(self, master):
        self.master = master
        master.title('OCR 프로그램')
        master.geometry('700x700')
        
        self.image_path = ''
        self.lang = 'eng'
        
        self.label = tk.Label(master, text='이미지 선택', font=('Arial', 16))
        self.label.pack(pady=20)
        
        self.select_button = tk.Button(master, text='이미지 선택', command=self.select_image)
        self.select_button.pack(pady=10)
        
        self.lang_label = tk.Label(master, text='추출할 언어 선택', font=('Arial', 16))
        self.lang_label.pack(pady=20)
        
        self.lang_eng_button = tk.Button(master, text='영어', command=lambda: self.set_lang('eng'))
        self.lang_eng_button.pack(pady=10)
        
        self.lang_kor_button = tk.Button(master, text='한국어', command=lambda: self.set_lang('kor'))
        self.lang_kor_button.pack(pady=10)
        
        self.extract_button = tk.Button(master, text='텍스트 추출', command=self.extract_text)
        self.extract_button.pack(pady=20)
        
        self.text_label = tk.Label(master, text='', font=('Arial', 14))
        self.text_label.pack(pady=20)
    
    def select_image(self):
        self.image_path = filedialog.askopenfilename()
        
    def set_lang(self, lang):
        self.lang = lang
        
    def extract_text(self):
        if not self.image_path:
            self.text_label.config(text='이미지를 선택하세요.')
            messagebox.showwarning("경고", "이미지를 선택하세요.")
            return
        
        try:
            image = Image.open(self.image_path)
            text = pytesseract.image_to_string(image, lang=self.lang)
            
            if text.strip():
                self.text_label.config(text=text)
                messagebox.showinfo("완료", "텍스트 추출이 완료되었습니다!")
            else:
                self.text_label.config(text="텍스트를 찾을 수 없습니다.")
                messagebox.showinfo("알림", "이미지에서 텍스트를 찾을 수 없습니다.")
                
        except Exception as e:
            error_msg = f"텍스트 추출 중 오류가 발생했습니다:\n{str(e)}"
            self.text_label.config(text=error_msg)
            messagebox.showerror("오류", error_msg)

root = tk.Tk()
app = OCRGUI(root)
root.mainloop()
