import tkinter as tk
from tkinter import ttk 
import numpy as np
import tkinter as tk
from tkinter import ttk

def crear_traspuesta(ventana):
    def guardar_valores():
        # Obtener los valores de las entradas y guardarlos en las variables
        try:
            filas_valor = int(entry_filas.get())
            columnas_valor = int(entry_columnas.get())
        except ValueError:
            error_label.config(text="Error: Ingrese valores numéricos para las filas y columnas.")
            return

        try:
            # Obtener la matriz A
            matriz_A = obtener_matriz(entry_matriz_a, filas_valor, columnas_valor)

            if matriz_A is not None:
                # Calcular la matriz traspuesta
                matriz_traspuesta = np.transpose(matriz_A).tolist()

                # Mostrar la matriz traspuesta en el mismo formato
                mostrar_matriz_traspuesta(matriz_traspuesta)
            else:
                error_label.config(text="Error: Ingrese valores numéricos para la matriz.")
        except ValueError:
            error_label.config(text="Error: Ingrese valores numéricos para la matriz.")

    def obtener_matriz(entry_matriz, filas, columnas):
        matriz = []
        entrada_texto = entry_matriz.get()
        valores = entrada_texto.split(',')

        # Validar que el número de valores ingresados sea igual a las columnas
        if len(valores) != columnas * filas:
            return None

        for i in range(filas):
            fila = []
            for j in range(columnas):
                try:
                    valor = float(valores[i * columnas + j])
                    fila.append(valor)
                except ValueError:
                    return None
            matriz.append(fila)
        return matriz


    def mostrar_matriz_traspuesta(matriz_traspuesta):
        # Crear una nueva ventana para mostrar la matriz traspuesta
        ventana_traspuesta = tk.Toplevel()
        ventana_traspuesta.title("Matriz Traspuesta")

        # Crear un frame para la matriz traspuesta
        frame_traspuesta = ttk.Frame(ventana_traspuesta, width=400, height=550)
        frame_traspuesta.pack()

        # Etiqueta para la matriz traspuesta
        label_traspuesta = ttk.Label(frame_traspuesta, text="Matriz Traspuesta", font=("Bold", 15))
        label_traspuesta.grid(row=0, column=0, columnspan=len(matriz_traspuesta[0]) * 2, pady=20)

        # Crear el Treeview para mostrar la matriz traspuesta
        treeview = ttk.Treeview(frame_traspuesta)
        treeview.grid(row=1, column=0, columnspan=len(matriz_traspuesta[0]) * 2, padx=10)

        # Configurar las columnas del Treeview
        column_names = [f"Columna {i+1}" for i in range(len(matriz_traspuesta[0]))]
        treeview["columns"] = column_names
        treeview.heading("#0", text="Fila")
        for i, column_name in enumerate(column_names):
            treeview.heading(column_name, text=column_name)

        # Insertar los datos en el Treeview
        for i, fila in enumerate(matriz_traspuesta):
            treeview.insert("", "end", text=f"Fila {i+1}", values=tuple(fila))


    frame_traspuesta = tk.Frame(ventana, width=540, height=600)
    label_traspuesta = ttk.Label(frame_traspuesta, text="Operacion: Traspuesta", font=("Bold", 15))
    label_traspuesta.grid(row=0, column=2, columnspan=1, pady=20)

    # Etiqueta y entrada para la cantidad de filas
    label_filas = ttk.Label(frame_traspuesta, text="n°Filas:")
    label_filas.grid(row=1, column=1, pady=10) 
    entry_filas = ttk.Entry(frame_traspuesta, width=5)
    entry_filas.grid(row=2, column=1, pady=10, padx=20)

    # Etiqueta y entrada para la cantidad de columnas
    label_columnas = ttk.Label(frame_traspuesta, text="n°Columnas:")
    label_columnas.grid(row=1, column=3, pady=10)
    entry_columnas = ttk.Entry(frame_traspuesta, width=5)
    entry_columnas.grid(row=2, column=3, pady=10, padx=20)

    # Etiqueta y entrada de la matriz A
    label_matriz_a = ttk.Label(frame_traspuesta, text="Matriz A:")
    label_matriz_a.grid(row=3, column=2, pady=10, columnspan=1)
    entry_matriz_a = ttk.Entry(frame_traspuesta, width=30)
    entry_matriz_a.grid(row=4, column=2, columnspan=1, pady=10)

    # Botón para guardar los valores y mostrar la matriz traspuesta
    boton_guardar = ttk.Button(frame_traspuesta, text="Calcular Traspuesta", command=guardar_valores)
    boton_guardar.grid(row=5, column=2, columnspan=1, pady=20)
    
    def reset_entries():
            nonlocal error_label  # Use the nonlocal keyword to access the error_label variable
            error_label.config(text="")
            entry_filas.delete(0, 'end')
            entry_columnas.delete(0, 'end')
            entry_matriz_a.delete(0, 'end')

        ## S3.9 - Este Botón resetea las entradas
    boton_reset = ttk.Button(frame_traspuesta, text="Resetear Entradas", command=reset_entries)
    boton_reset.grid(row=5, column=4, columnspan=3, pady=20)


    # Etiqueta para mostrar errores
    error_label = tk.Label(frame_traspuesta, text="", fg="red")
    error_label.grid(row=6, column=2, pady=10)

    return frame_traspuesta