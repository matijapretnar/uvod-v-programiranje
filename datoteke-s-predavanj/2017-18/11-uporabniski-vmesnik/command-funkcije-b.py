import tkinter as tk

def odzdravi(pozdrav):
    def funkcija_pozdrava():
        print('{}, človek!'.format(pozdrav))
    return funkcija_pozdrava

okno = tk.Tk()
tk.Button(okno, text='Živjo, Python!', command=odzdravi('Živjo')).pack()
tk.Button(okno, text='Dober dan, Python!', command=odzdravi('Dober dan')).pack()
tk.Button(okno, text='Kako si, Python?', command=odzdravi('V redu')).pack()

okno.mainloop()
