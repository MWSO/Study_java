import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image
import PIL.ImageTk

def photo(path):
  new_image = PIL.Image.open(path).resize((300,300))
  image_data = PIL.ImageTk.PhotoImage(new_image)
  image_label.configure(image = image_data)
  image_label.image = image_data

def open_file():
  fpath = fd.askopenfilename()
  if fpath:
    photo(fpath)

root = tk.Tk()
root.geometry("400x350")

btn = tk.Button(text="ファイルを開く", command=open_file)
image_label = tk.Label()

btn.pack()
image_label.pack()
tk.mainloop()