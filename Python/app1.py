import tkinter as tk

def label_text():
  lbl.configure(text="こんにちは！")

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="LABEL")
btn = tk.Button(text="Push", command = label_text)

lbl.pack()
btn.pack()
tk.mainloop()