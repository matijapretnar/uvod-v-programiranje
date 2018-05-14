import tkinter as tk

okno = tk.Tk()
platno = tk.Canvas(okno, height=500, width=500)
platno.pack()

stari_x, stari_y = None, None

def narisi_crto(event):
    # POZOR, GLOBALNIH SPREMENLJIVK NE UPORABLJAJTE!
    global stari_x, stari_y
    x = event.x
    y = event.y
    if stari_x != None and stari_y != None:
        platno.create_line(stari_x, stari_y, x, y)
    stari_x = x
    stari_y = y

def koncaj_crto(event):
    # POZOR, GLOBALNIH SPREMENLJIVK NE UPORABLJAJTE!
    global stari_x, stari_y
    stari_x = None
    stari_y = None


okno.bind('<B1-Motion>', narisi_crto)
okno.bind('<ButtonRelease-1>', koncaj_crto)

okno.mainloop()
