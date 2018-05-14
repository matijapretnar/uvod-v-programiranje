import tkinter as tk

def odzdravi(pozdrav):
    print('{}, človek!'.format(pozdrav))

okno = tk.Tk()
tk.Button(okno, text='GOR', command=lambda: odzdravi('Živjo')).pack()
tk.Button(okno, text='DOL', command=lambda: odzdravi('Dober dan')).pack()
tk.Button(okno, text='LEVO', command=lambda: odzdravi('V redu')).pack()
tk.Button(okno, text='DESNO', command=lambda: odzdravi('Živjo')).pack()

okno.mainloop()
