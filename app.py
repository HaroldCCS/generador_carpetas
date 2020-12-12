'''--------------------- LIBRERIAS -----------------------'''
import pandas as pd
import os

from tkinter import Label, Tk, Button, filedialog, Frame

'''--------------------- FUNCIONES -----------------------'''

def buscarArchivo():
    file1 = filedialog.askopenfilenames(filetypes=[('Archivos CSV', '*.csv')])
    leerCSV(file1[0])

def limpiar(varFrame):
    Button(varFrame, text="Limpiar contenido", width="50", fg="black",
           font=("Verdana", 10), command=varFrame.destroy).pack()

def leerCSV(nombre_csv):
    frame2 = Frame(ventana)
    frame2.pack()
    try:
        crear_carpetas(nombre_csv, frame2)

    except:
        Label(text="No se ha encontrado un archivo.csv").pack()
    limpiar(frame2)


def crear_carpetas(nombre_csv, varFrame):
    datos = pd.read_csv(nombre_csv, sep=';')
    df = pd.DataFrame(datos)

    for i in df.index:
        carpetas = ''
        for x in df.columns:
            carpetas = carpetas + '/' + df[x][i]
        try:
            os.makedirs(carpetas[1:])
            Label(varFrame, text="Carpetas creadas correctamente").pack()
        except:
            Label(varFrame, text="Error: Las carpetas ya existen").pack()

'''--------------------- INTERFAZ -----------------------'''

ventana = Tk()

ventana.title("Generador de carpetas")
ventana.resizable(0, 0)
ventana.geometry("650x1000")

Label(text="Software creador de carpetas segun columnas de excel", width=650, height=2,
      fg="white", bg="#00A11D", font=("Verdana bold", 10)).pack()

frame = Frame(ventana, bg="#D6D6D6", width=650, height=300)
frame.pack()

Label(frame, text="Ingrese un archivo .csv", width=650, height=2, bg="#D6D6D6",
      fg="black", font=("Verdana", 10)).pack(pady=5)

Button(frame, text="Buscar Archivo", width="50", fg="black", font=("Verdana", 10),
       command=buscarArchivo).pack(pady=5)
ventana.mainloop()

