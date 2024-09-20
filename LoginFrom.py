import tkinter as tk
from tkinter import messagebox

# Hàm để xử lý đăng nhập
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    if username == "admin" and password == "password":
        messagebox.showinfo("Login Success", "Welcome, admin!")
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Login Form")
root.geometry("300x250")
root.configure(bg="#2c3e50")

# Tạo tiêu đề
title_label = tk.Label(root, text="Login", font=("Helvetica", 16, "bold"), bg="#2c3e50", fg="#ecf0f1")
title_label.pack(pady=10)

# Tạo và bố trí nhãn và ô nhập liệu cho username
label_username = tk.Label(root, text="Username", font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1")
label_username.pack(pady=5)

entry_username = tk.Entry(root, font=("Helvetica", 12))
entry_username.pack(pady=5)

# Tạo và bố trí nhãn và ô nhập liệu cho password
label_password = tk.Label(root, text="Password", font=("Helvetica", 12), bg="#2c3e50", fg="#ecf0f1")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*", font=("Helvetica", 12))
entry_password.pack(pady=5)

# Tạo và bố trí nút đăng nhập
button_login = tk.Button(root, text="Login", font=("Helvetica", 12, "bold"), bg="#e74c3c", fg="#ecf0f1", command=login)
button_login.pack(pady=20)

# Chạy vòng lặp chính
root.mainloop()
