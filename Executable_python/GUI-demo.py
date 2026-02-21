import tkinter as tk

root = tk.Tk()
root.title("Mi App")
root.geometry("300x150")

label = tk.Label(root, text="Hola mundo", font=("Arial", 16))
label.pack(expand=True)

root.mainloop()