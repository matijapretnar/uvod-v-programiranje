import tkinter as tk

okno = tk.Tk()
vhod = tk.Entry(okno)
vhod.pack()
def odzdravi():
    print('Dober dan, {}!'.format(
        vhod.get()))
gumb = tk.Button(okno,
                 text='Živjo, Python!',
                 command=odzdravi)
gumb.pack()
