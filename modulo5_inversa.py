import tkinter as tk
from tkinter import ttk
import numpy as np
import fractions
def crear_inversa(ventana):
    def guardar_valores():
        try:
            filas = int(entry_filas.get())
            columnas = int(entry_columnas.get())
        except ValueError:
            mostrar_error("Error: Ingrese valores numéricos para filas y columnas.")
            return

        matriz = obtener_matriz(entry_matriz, filas, columnas)

        if matriz is not None:
            resultado_inversa = obtener_inversa(matriz)

            if resultado_inversa is not None:
                mostrar_resultado(resultado_inversa)
            else:
                mostrar_error("Error: La matriz no es invertible.")

    def obtener_matriz(entry_matriz, filas, columnas):
        matriz = []
        entrada_texto = entry_matriz.get()
        valores = entrada_texto.split(',')

        if len(valores) != columnas * filas:
            mostrar_error(f"Error: Ingrese {filas * columnas} valores para la matriz.")
            return None

        for i in range(filas):
            fila = []
            for j in range(columnas):
                try:
                    valor = fractions.Fraction(valores[i * columnas + j])
                    fila.append(valor)
                except ValueError:
                    mostrar_error("Error: Ingrese valores numéricos para la matriz.")
                    return None
            matriz.append(fila)
        return matriz

    def mostrar_resultado(resultado):
        ventana_resultado = tk.Toplevel(ventana)
        ventana_resultado.title("Resultado de la Operación")

        frame_resultado = tk.Frame(ventana_resultado, width=400, height=550)
        frame_resultado.pack()
     
        label_resultado = ttk.Label(frame_resultado, text="Resultado de la Operación", font=("Bold", 15))
        label_resultado.grid(row=0, column=0, columnspan=len(resultado[0]) * 2, pady=20)

       # Crear el Treeview para mostrar el resultado en formato tabular
        treeview = ttk.Treeview(frame_resultado)
        treeview.grid(row=1, column=0, columnspan=len(resultado[0]) * 2, padx=10)

        # Configurar las columnas del Treeview
        columnas = [f"Columna {i+1}" for i in range(len(resultado[0]))]
        treeview["columns"] = columnas
        treeview.heading("#0", text="Fila")
        for i, columna in enumerate(columnas):
            treeview.heading(columna, text=columna)

        # Mostrar el resultado de la multiplicación en el Treeview
        for i, fila in enumerate(resultado):
            treeview.insert("", "end", text=f"Fila {i+1}", values=tuple(fila))

    def obtener_inversa(matriz):
        try:
            matriz_np = np.array(matriz, dtype=float)
            matriz_inversa_np = np.linalg.inv(matriz_np)
            matriz_inversa = matriz_inversa_np.tolist()
            return matriz_inversa
        except np.linalg.LinAlgError:
            mostrar_error("Error: La matriz no es invertible.")
            return None

    def mostrar_error(mensaje):
        error_label.config(text=mensaje)

    frame_inversa = ttk.Frame(ventana, style="TFrame", width=550, height=550)
    frame_inversa.pack(expand=True, fill=tk.BOTH)

    label_inversa = ttk.Label(frame_inversa, text="Operación: Inversa", font=("Bold", 15))
    label_inversa.grid(row=0, column=2, columnspan=1, pady=20, sticky='n')

    label_filas = ttk.Label(frame_inversa, text="Filas:")
    label_filas.grid(row=1, column=1, pady=10, sticky='n')
    entry_filas = ttk.Entry(frame_inversa, width=5)
    entry_filas.grid(row=2, column=1, pady=10, padx=20, sticky='n')

    label_columnas = ttk.Label(frame_inversa, text="Columnas:")
    label_columnas.grid(row=1, column=3, pady=10, sticky='n')
    entry_columnas = ttk.Entry(frame_inversa, width=5)
    entry_columnas.grid(row=2, column=3, pady=10, padx=20, sticky='n')

    label_matriz = ttk.Label(frame_inversa, text="Matriz:")
    label_matriz.grid(row=3, column=2, pady=10, columnspan=1, sticky='n')
    entry_matriz = ttk.Entry(frame_inversa, width=25)
    entry_matriz.grid(row=4, column=2, columnspan=1, pady=10, sticky='n')

    error_label = ttk.Label(frame_inversa)
    error_label.grid(row=6, column=2, pady=10, sticky='n')

    boton_guardar = ttk.Button(frame_inversa, text="Calcular Inversa", command=guardar_valores)
    boton_guardar.grid(row=5, column=2, columnspan=1, pady=20, sticky='n')

    def reset_entries():
        entry_filas.delete(0, 'end')
        entry_columnas.delete(0, 'end')
        entry_matriz.delete(0, 'end')
        error_label.config(text="")

    boton_reset = ttk.Button(frame_inversa, text="Resetear Entradas", command=reset_entries)
    boton_reset.grid(row=5, column=4, columnspan=3, pady=20)

    return frame_inversa
