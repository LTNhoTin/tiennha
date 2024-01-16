import tkinter as tk
from tkinter import ttk

room = 2
member = 3
Rent = 5500000
Wifi = 245000
Bike = 150000

def calculate_cost():
    try:
        Electricity = float(entry_electricity.get().replace(',', ''))
        Condominium = float(entry_condo.get().replace(',', ''))
        Parking = float(entry_par.get().replace(',', ''))
        Park = Parking - Bike
        Cod = Condominium - Parking
        Costperroom = ((Rent + Cod + Wifi) / room) + Bike + (Electricity * 2 / member)
        AmountToSend = (Rent / room) - (Park + (Cod / room) + (Electricity / member) + (Wifi / room))
        label_costperroom.config(text=f"Chi phí trung bình cho phòng mình: {Costperroom:,.0f} VND", foreground="pink")
        label_amountToSend.config(text=f"Số tiền cần gửi cho chị phòng bên: {AmountToSend:,.0f} VND", foreground="green")
    except ValueError:
        label_costperroom.config(text="Vui lòng nhập số hợp lệ cho tiền điện và phí quản lý.", foreground="red")
        label_amountToSend.config(text="", foreground="red")

# Tạo cửa sổ
window = tk.Tk()
window.title("Tính Chi Phí Thuê Nhà")
window.geometry("350x350")  # Đặt kích thước cửa sổ

# Hàm tạo và định vị các widget
def create_label_entry_pair(label_text, row, column):
    label = ttk.Label(window, text=label_text, foreground="black", font=('Helvetica', 12, 'bold'))
    label.grid(row=row, column=column, padx=10, pady=10, sticky="e")
    entry = ttk.Entry(window, font=('Helvetica', 12))
    entry.grid(row=row, column=column+1, padx=10, pady=10, sticky="w")
    return entry

entry_electricity = create_label_entry_pair("Nhập tổng tiền điện (VND):", 0, 0)
entry_condo = create_label_entry_pair("Nhập tổng phí quản lý (VND):", 1, 0)
entry_par = create_label_entry_pair("Nhập tổng phí giữ xe  (VND):", 2, 0)

button_calculate = ttk.Button(window, text="Tính Toán", command=calculate_cost, style='TButton')
button_calculate.grid(row=3, column=0, columnspan=2, pady=10)

style = ttk.Style()
style.configure('TButton', font=('Helvetica', 12, 'bold'), foreground="white", background="green", padding=10)

label_costperroom = ttk.Label(window, text="", foreground="red", font=('Helvetica', 12, 'bold'))
label_costperroom.grid(row=4, column=0, columnspan=2, pady=10)

label_amountToSend = ttk.Label(window, text="", foreground="green", font=('Helvetica', 12, 'bold'))
label_amountToSend.grid(row=5, column=0, columnspan=2, pady=10)

# Chạy vòng lặp sự kiện

window.mainloop()
