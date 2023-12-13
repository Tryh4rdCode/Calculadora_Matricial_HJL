import tkinter as tk
from tkinter import ttk 
import numpy as np

error_label = None  # Define the error_label variable outside the function
label_inversa = None  # Define the label_inversa variable outside the function



def crear_determinante(ventana):
    def guardar_valores():
        global error_label, label_inversa  # Use the global keyword to access the error_label and label_inversa variables
        error_label.config(text=(""))  # Modify the error_label variable

        try:
            filas = int(entry_filas.get())
            columnas = int(entry_columnas.get())
        except ValueError:
            error_label.config(text=("Error: Ingrese valores numéricos para filas y columnas."))
            error_label.grid(row=6, column=2, pady=10, sticky='n')  # Add this line
            return
        
        label_resultado = ttk.Label(frame_determina)  # Define the label_resultado variable
        matriz = obtener_matriz(entry_matriz, filas, columnas)

        if matriz is not None:
            resultado_determinante = obtener_determinante(matriz)
            label_resultado.config(text="resultado: " + str(resultado_determinante))
            if resultado_determinante == 0:
                label_inversa = ttk.Label(frame_determina, text="Es inversa", font=("Bold", 15))
                label_inversa.grid(row=11, column=2, columnspan=1, pady=20, sticky='n')
            else:
                label_inversa = ttk.Label(frame_determina, text="No es inversa", font=("Bold", 15))
                label_inversa.grid(row=11, column=2, columnspan=1, pady=20, sticky='n')

    def obtener_matriz(entry_matriz, filas, columnas):
        global error_label  # Use the global keyword to access the error_label variable
        error_label.config(text=(""))  # Modify the error_label variable

        matriz = []
        entrada_texto = entry_matriz.get()
        valores = entrada_texto.split(',')

        if len(valores) != columnas * filas:
            error_label.config(text=(f"Error: Ingrese {filas * columnas} valores para la matriz."))
            error_label.grid(row=6, column=2, pady=10, sticky='n')  # Add this line
            return None

        for i in range(filas):
            fila = []
            for j in range(columnas):
                try:
                    valor = int(valores[i * columnas + j])
                    fila.append(valor)
                except ValueError:
                    error_label.config(text=("Error: Ingrese valores numéricos para la matriz."))
                    return None
            matriz.append(fila)
        return matriz

    frame_determina = ttk.Frame(ventana, style="TFrame", width=550, height=550)
    frame_determina.pack(expand=True, fill=tk.BOTH)

    label_determina = ttk.Label(frame_determina, text="Operación: Determinante", font=("Bold", 15))
    label_determina.grid(row=0, column=2, columnspan=1, pady=20, sticky='n')

    label_filas = ttk.Label(frame_determina, text="Filas:")
    label_filas.grid(row=1, column=1, pady=10, sticky='n')
    entry_filas = ttk.Entry(frame_determina, width=5)
    entry_filas.grid(row=2, column=1, pady=10, padx=20, sticky='n')

    label_columnas = ttk.Label(frame_determina, text="Columnas:")
    label_columnas.grid(row=1, column=3, pady=10, sticky='n')
    entry_columnas = ttk.Entry(frame_determina, width=5)
    entry_columnas.grid(row=2, column=3, pady=10, padx=20, sticky='n')

    label_matriz = ttk.Label(frame_determina, text="Matriz:")
    label_matriz.grid(row=3, column=2, pady=10, columnspan=1, sticky='n')
    entry_matriz = ttk.Entry(frame_determina, width=25)
    entry_matriz.grid(row=4, column=2, columnspan=1, pady=10, sticky='n')

    button_calcular = ttk.Button(frame_determina, text="Calcular Determinante", command=guardar_valores)
    button_calcular.grid(row=5, column=2, pady=10)

    global error_label  # Use the global keyword to access the error_label variable
    error_label = ttk.Label(frame_determina)  # Initialize the error_label variable
    label_inversa = None  # Define the label_inversa variable

    def reset_entries():
        global error_label, label_inversa  # Use the global keyword to access the error_label and label_inversa variables
        error_label.config(text="")
        entry_filas.delete(0, 'end')
        entry_columnas.delete(0, 'end')
        entry_matriz.delete(0, 'end')
        label_inversa.config(text="")  # Modify the label_inversa variable


    ## S3.9 - Este Botón resetea las entradas
    boton_reset = ttk.Button(frame_determina, text="Resetear Entradas", command=reset_entries)
    boton_reset.grid(row=5, column=4, columnspan=3, pady=20)

    def obtener_determinante(matriz):
        global error_label  # Use the global keyword to access the error_label variable
        error_label.config(text=(""))  # Modify the error_label variable

        try:
            determinante = np.linalg.det(matriz)
            return determinante
        except np.linalg.LinAlgError:
            error_label.config(text=("Error: La matriz no es cuadrada."))
            return None

    return frame_determina
