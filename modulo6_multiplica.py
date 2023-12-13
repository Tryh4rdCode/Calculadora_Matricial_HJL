import tkinter as tk
from tkinter import ttk 
import numpy as np
import tkinter as tk
from tkinter import ttk

def crear_multiplica(ventana):
    error_label = None  # Define the error_label variable outside the function

    def guardar_valores():
        nonlocal error_label  # Use the nonlocal keyword to access the error_label variable

        # Obtener los valores de las entradas y guardarlos en las variables
        try:
            filas_A = int(entry_filas_A.get())
            columnas_A = int(entry_columnas_A.get())
            filas_B = int(entry_filas_B.get())
            columnas_B = int(entry_columnas_B.get())
        except ValueError:
            error_label = ttk.Label(frame_multiplicacion, text="Error: Ingrese valores numéricos para las filas y columnas.")
            error_label.grid(row=8, column=1, columnspan=3, pady=10)
            return

        # Obtener las matrices A y B
        matriz_A = obtener_matriz(entry_matriz_A, filas_A, columnas_A)
        matriz_B = obtener_matriz(entry_matriz_B, filas_B, columnas_B)

        # Check if matrices are valid
        if matriz_A is None or matriz_B is None:
            error_label = ttk.Label(frame_multiplicacion, text="Error: Las matrices no son válidas.")
            error_label.grid(row=8, column=1, columnspan=3, pady=10)
            return

        if matriz_A is not None and matriz_B is not None:
            # Realizar la multiplicación de matrices o cualquier otra operación que desees
            resultado = multiplicar_matrices(matriz_A, matriz_B)
            if resultado is not None:
                # Mostrar el resultado en la interfaz gráfica
                mostrar_resultado(resultado)
            else:
                error_label = ttk.Label(frame_multiplicacion, text="Error: Las matrices no pueden multiplicarse debido a sus dimensiones.")
                error_label.grid(row=6, column=1, columnspan=3, pady=10)

    def obtener_matriz(entry_matriz, filas, columnas):
        nonlocal error_label  # Use the nonlocal keyword to access the error_label variable

        matriz = []
        entrada_texto = entry_matriz.get()
        valores = entrada_texto.split(',')

        # Validar que el número de valores ingresados sea igual a las columnas
        if len(valores) != columnas * filas:
            error_label = ttk.Label(frame_multiplicacion, text=f"Error: Ingrese {filas * columnas} valores para la matriz.")
            error_label.grid(row=8, column=1, columnspan=3, pady=10)
            return None

        for i in range(filas):
            fila = []
            for j in range(columnas):
                try:
                    valor = int(valores[i * columnas + j])
                    fila.append(valor)
                except ValueError:
                    error_label = ttk.Label(frame_multiplicacion, text="Error: Ingrese valores numéricos para la matriz.")
                    error_label.grid(row=8, column=1, columnspan=3, pady=10)
                    return None
            matriz.append(fila)
        return matriz


    def mostrar_resultado(resultado):
        # Crear una nueva ventana para mostrar el resultado de la multiplicación
        ventana_resultado = tk.Toplevel(ventana)
        ventana_resultado.title("Resultado de la Multiplicación")

        # Crear un frame para el resultado de la multiplicación
        frame_resultado = tk.Frame(ventana_resultado, width=400, height=550)
        frame_resultado.pack()

        # Etiqueta para el resultado de la multiplicación
        label_resultado = ttk.Label(frame_resultado, text="Resultado de la Multiplicación", font=("Bold", 15))
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

    frame_multiplicacion = ttk.Frame(ventana, style="TFrame", width=550, height=550)    
    frame_multiplicacion.pack()

    label_multiplicacion = ttk.Label(frame_multiplicacion, text="Operacion: Multiplicación", font=("Bold", 15))
    label_multiplicacion.grid(row=0, column=1, columnspan=3, pady=20)

    # Etiqueta y entrada para la cantidad de filas de A
    label_filas_A = ttk.Label(frame_multiplicacion, text="Filas A:")
    label_filas_A.grid(row=1, column=1, pady=10)
    entry_filas_A = ttk.Entry(frame_multiplicacion, width=5)
    entry_filas_A.grid(row=2, column=1, pady=10, padx=20)

    # Etiqueta y entrada para la cantidad de columnas de A
    label_columnas_A = ttk.Label(frame_multiplicacion, text="Columnas A:")
    label_columnas_A.grid(row=1, column=3, pady=10)
    entry_columnas_A = ttk.Entry(frame_multiplicacion, width=5)
    entry_columnas_A.grid(row=2, column=3, pady=10, padx=20)

    # Etiqueta y entrada para la cantidad de filas de B
    label_filas_B = ttk.Label(frame_multiplicacion, text="Filas B:")
    label_filas_B.grid(row=3, column=1, pady=10)
    entry_filas_B = ttk.Entry(frame_multiplicacion, width=5)
    entry_filas_B.grid(row=4, column=1, pady=10, padx=20)

    # Etiqueta y entrada para la cantidad de columnas de B
    label_columnas_B = ttk.Label(frame_multiplicacion, text="Columnas B:")
    label_columnas_B.grid(row=3, column=3, pady=10)
    entry_columnas_B = ttk.Entry(frame_multiplicacion, width=5)
    entry_columnas_B.grid(row=4, column=3, pady=10, padx=20)

    # Etiqueta y entrada de la matriz A
    label_matriz_A = ttk.Label(frame_multiplicacion, text="Matriz A:")
    label_matriz_A.grid(row=5, column=1, pady=10)
    entry_matriz_A = ttk.Entry(frame_multiplicacion, width=25)
    entry_matriz_A.grid(row=6, column=1, pady=10, padx=20)

    # Etiqueta y entrada de la matriz B
    label_matriz_B = ttk.Label(frame_multiplicacion, text="Matriz B:")
    label_matriz_B.grid(row=5, column=3, pady=10)
    entry_matriz_B = ttk.Entry(frame_multiplicacion, width=25)
    entry_matriz_B.grid(row=6, column=3, pady=10, padx=20)

    # Botón para guardar los valores
    boton_guardar = ttk.Button(frame_multiplicacion, text="Calcular Multiplicación", command=guardar_valores)
    boton_guardar.grid(row=7, column=1, columnspan=3, pady=20)

    def reset_entries():
        nonlocal error_label  # Use the nonlocal keyword to access the error_label variable
        error_label.config(text="")
        entry_filas_A.delete(0, 'end')
        entry_columnas_A.delete(0, 'end')
        entry_filas_B.delete(0, 'end')
        entry_columnas_B.delete(0, 'end')
        entry_matriz_A.delete(0, 'end')
        entry_matriz_B.delete(0, 'end')

    ## S3.9 - Este Botón resetea las entradas
    boton_reset = ttk.Button(frame_multiplicacion, text="Resetear Entradas", command=reset_entries)
    boton_reset.grid(row=7, column=4, columnspan=3, pady=20)

    return frame_multiplicacion

# Función ficticia para la multiplicación de matrices (reemplázala con tu propia implementación)
def multiplicar_matrices(matriz_A, matriz_B):
    # Utiliza numpy para realizar la multiplicación de matrices
    resultado_np = np.dot(matriz_A, matriz_B)
    # Convierte el resultado de numpy a una lista de listas
    resultado = resultado_np.tolist()
    return resultado
