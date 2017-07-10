import tkinter as tk
from tkinter import Menu


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        # self.pack()
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        dRow =0
        self.lblHostname = tk.Label(self)
        self.lblHostname['text']="Dato a buscar: "
        self.lblHostname.grid(row=dRow, column=0)
        self.entHostname = tk.Entry(self)

        self.entHostname.grid(row=dRow, column=1, columnspan=3)
        self.btnBuscar = tk.Button(self)
        self.btnBuscar["text"] = "Buscar"
        self.btnBuscar["command"] = self.funcBuscar
        self.btnBuscar.grid(row=dRow, column=4)
        dRow = dRow + 1

        self.cerrar = tk.Button(self, text="Cerrar", fg="red",
                              command=root.destroy)
        self.cerrar.grid(row=dRow, column=4)

    def funcBuscar(self):
        self.btnBuscar["text"] ="Esto cambia al hacer click"
        print(self.btnBuscar["text"])

# Centramos la aplicación
def center(toplevel):
    toplevel.update_idletasks()
    w = toplevel.winfo_screenwidth()
    h = toplevel.winfo_screenheight()
    size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

# Construimos el menú
def create_menu(toplevel):
    menuBar = Menu()
    toplevel.config(menu=menuBar)
    filemenu = Menu(menuBar, tearoff = 0)
    filemenu.add_command(label="Buscar" )
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command = _quit)
    menuBar.add_cascade(label="Archivo", menu = filemenu)

def _quit():
    root.quit()
    root.destroy()
    exit()
    
root = tk.Tk()
root.title('Busqueda en logs')
root.minsize(width=400, height=300)
center(root)
create_menu(root)
app = Application(master=root)
# app.master.geometry("600x400")
app.mainloop()