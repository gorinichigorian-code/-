import tkinter as tk
 
root = tk.Tk()
root.title("Учебное заведение")
root.geometry("640x480")
root.configure(bg="#f9f1e5")

root.mainloop()


label = tk.Label(root, text="Привет")
label.pack()


Bg = "#f9f1e5"
FIELD_BG = "#ffffff"
FIELD_FG = "#22262b"
PRIMARY_BG = "#1e5fd0"
PRIMARY_FG = "#ffffff"
SECOND_BG = "#e5e7eb"
SECOND_FG = "#111827"

FONT_TITLE = ("Arial", 16, "bold")
FONT_LABEL = ("Arial", 11, "bold")
FONT_BUTTON = ("Arial", 12, "bold")


tk.Button(container, text="Войти").pack(fill="x")
tk.Button(container, text="Войти").pack(fill="x", ipday=6)


label.pack(fill="x", pady=(0, 10))
Button.pack(side="left", padx=(0, 6))


tk.Label(container, text="Логин").grid(row=0, column=0, sticky="w", pady=5)
tk.Entry(container).grid(row=0, column=1, sticky="ew", pady=5)


entry = tk.Entry(root)
entry.pack()

text = entry.get()
entry.delete(0, "end")
entry.insert(0, "admin")


def open_admin():
    print("открыли админку")

btn = tk.Button(root, text="Админка", command=open_admin)
btn = tk.Button(root, text="Админка", command=open_admin())
