import random
import tkinter as tk

def omikuzi():
  kuzi = ["大吉", "中吉", "吉", "末吉", "凶", "大凶"]
  lbl.configure(text = random.choice(kuzi))

root = tk.Tk()
root.geometry("200x100")

lbl = tk.Label(text="label")
btn = tk.Button(text="Push", command=omikuzi)

lbl.pack()
btn.pack()
tk.mainloop()