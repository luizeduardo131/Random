from PIL import ImageGrab
import time
import cv2
import tkinter as tk

HEIGHT = 0
WIDTH = 0
root = tk.Tk()

root.title('Screenshot Saver')

def closeWindow():
    root.destroy()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

label = tk.Label(text='Vá para a área de trabalho e depois clique em fechar programa', bg='gray',height=1, width=50)
label.pack()
label = tk.Label(text='Não esqueça de tirar a imagem da pasta do script', bg='gray',height=2, width=50)
label.pack()

root.mainloop()
time.sleep(2)
x = ImageGrab.grab() 
x.save('Screenshot.jpg')
x.show()

