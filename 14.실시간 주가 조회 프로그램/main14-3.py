import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

def get_stock_price():
    code = code_entry.get().strip()
    if not code:
        messagebox.showwarning("경고", "종목 번호를 입력해주세요.")
        return
    
    try:
        url = f'https://finance.naver.com/item/main.nhn?code={code}'
        res = requests.get(url)
        res.raise_for_status()
        soup = BeautifulSoup(res.content, 'html.parser')
        
        # 여러 가능한 CSS 선택자 시도
        price_selectors = [
            '.no_today .blind',  # 현재 주가
            '#_nowVal',  # 현재가
            '.no_today',  # 오늘의 가격
            '.today .blind',  # 오늘 가격
            'p.no_today .blind'  # 현재가 (더 구체적)
        ]
        
        price = None
        for selector in price_selectors:
            price_element = soup.select_one(selector)
            if price_element:
                price = price_element
                break
        
        if price:
            result_label.config(text=f"현재 {code} 주가는 {price.text}원입니다.")
        else:
            result_label.config(text=f"종목 코드 {code}의 주가 정보를 찾을 수 없습니다.")
            messagebox.showinfo("알림", "주가 정보를 찾을 수 없습니다.\n다른 종목 코드를 시도해보세요.\n(예: 005930 - 삼성전자)")
            
    except requests.exceptions.RequestException as e:
        result_label.config(text="네트워크 오류가 발생했습니다.")
        messagebox.showerror("오류", f"네트워크 오류: {e}")
    except Exception as e:
        result_label.config(text="오류가 발생했습니다.")
        messagebox.showerror("오류", f"오류: {e}")

root = tk.Tk()
root.title("주식 가격 조회 프로그램")

label = tk.Label(root, text="종목 번호를 입력하세요:")
label.pack()

code_entry = tk.Entry(root)
code_entry.pack()

button = tk.Button(root, text="조회", command=get_stock_price)
button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
