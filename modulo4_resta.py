import tkinter as tk
from tkinter import ttk
import numpy as np

error_label = None  # Define error_label in a wider scope

def crear_resta(ventana):
    def guardar_valores():
        filas_valor = entry_filas.get()
        columnas_valor = entry_columnas.get()
        
        if error_label is not None:
            error_label.config(text="")  # Reset error label
        
        if not filas_valor.isdigit() or not columnas_valor.isdigit():
            if not filas_valor.isdigit() or not columnas_valor.isdigit():
                if error_label is not None:
                    error_label.config(text="Error: Ingrese valores numéricos para las filas y columnas.")
                return
            else:
                if error_label is not None:
                    error_label.config(text="Error: Las matrices no pueden restarse debido a sus dimensiones.")

        filas_valor = int(filas_valor)
        columnas_valor = int(columnas_valor)

        matriz_A = obtener_matriz(entry_matriz_a, filas_valor, columnas_valor)
        matriz_B = obtener_matriz(entry_matriz_b, filas_valor, columnas_valor)

        if matriz_A is not None and matriz_B is not None:
            resultado = resta_matrices(matriz_A, matriz_B)
            if resultado is not None:
                mostrar_resultado(resultado)
            else:
                if error_label is not None:
                    error_label.config(text="Error: Las matrices no pueden restarse debido a sus dimensiones.")
    
    def obtener_matriz(entry_matriz, filas, columnas):
        matriz = []
        entrada_texto = entry_matriz.get()
        valores = entrada_texto.split(',')

        if len(valores) != columnas * filas:
            if error_label is not None:
                error_label.config(text=f"Error: Ingrese {filas * columnas} valores para la matriz.")
            return None

        for i in range(filas):
            fila = []
            for j in range(columnas):
                try:
                    valor = int(valores[i * columnas + j])
                    fila.append(valor)
                except ValueError:
                    if error_label is not None:
                        error_label.config(text="Error: Ingrese valores numéricos para la matriz.")
                    return None
            matriz.append(fila)
        return matriz
    

    def mostrar_resultado(resultado):
        ventana_resultado = tk.Toplevel(ventana)
        ventana_resultado.title("Resultado de la Resta")

        frame_resultado = ttk.Frame(ventana_resultado, width=440, height=600)
        frame_resultado.pack()

        label_resultado = ttk.Label(frame_resultado, text="Resultado de la Resta", font=("Bold", 15))
        label_resultado.grid(row=0, column=0, columnspan=len(resultado[0]) * 2, pady=20)

        treeview = ttk.Treeview(frame_resultado)
        treeview["columns"] = tuple(range(len(resultado[0])))

        for i, fila in enumerate(resultado):
            treeview.insert("", "end", text=f"Fila {i+1}", values=tuple(fila))

        for i, columna in enumerate(range(len(resultado[0]))):
            treeview.heading(columna, text=f"Columna {i+1}")

        treeview.grid(row=1, column=0, columnspan=len(resultado[0]), pady=10, padx=20)

    frame_resta = ttk.Frame(ventana, style="TFrame", width=550, height=550)
    frame_resta.pack()
    label_resta = ttk.Label(frame_resta, text="Operacion: Resta", font=("Bold", 15))
    label_resta.grid(row=0, column=1, columnspan=3, pady=20)

    label_filas = ttk.Label(frame_resta, text="n°Filas:")
    label_filas.grid(row=1, column=1, pady=10)
    entry_filas = ttk.Entry(frame_resta, width=5)
    entry_filas.grid(row=2, column=1, pady=10, padx=20)

    label_columnas = ttk.Label(frame_resta, text="n°Columnas:")
    label_columnas.grid(row=1, column=3, pady=10)
    entry_columnas = ttk.Entry(frame_resta, width=5)
    entry_columnas.grid(row=2, column=3, pady=10, padx=20)

    label_matriz_a = ttk.Label(frame_resta, text="Matriz A:")
    label_matriz_a.grid(row=3, column=1, pady=10)
    entry_matriz_a = ttk.Entry(frame_resta, width=25)
    entry_matriz_a.grid(row=4, column=1, pady=10, padx=20)

    label_matriz_b = ttk.Label(frame_resta, text="Matriz B:")
    label_matriz_b.grid(row=3, column=3, pady=10)
    entry_matriz_b = ttk.Entry(frame_resta, width=25)
    entry_matriz_b.grid(row=4, column=3, pady=10, padx=20)

    error_label = ttk.Label(frame_resta, text="", foreground="red")
    error_label.grid(row=5, column=1, columnspan=3, pady=10)

    boton_guardar = ttk.Button(frame_resta, text="Calcular Resta", command=guardar_valores)
    boton_guardar.grid(row=5, column=1, columnspan=3, pady=20)

    def reset_entries():
        entry_filas.delete(0, 'end')
        entry_columnas.delete(0, 'end')
        entry_matriz_a.delete(0, 'end')
        entry_matriz_b.delete(0, 'end')
        if error_label is not None:
            error_label.config(text="")  # Reset error label

    boton_reset = ttk.Button(frame_resta, text="Resetear Entradas", command=reset_entries)
    boton_reset.grid(row=5, column=4, columnspan=3, pady=20)

    return frame_resta

def resta_matrices(matriz_A, matriz_B):
    return [[a - b for a, b in zip(fila_A, fila_B)] for fila_A, fila_B in zip(matriz_A, matriz_B)]

frame_actual = None
