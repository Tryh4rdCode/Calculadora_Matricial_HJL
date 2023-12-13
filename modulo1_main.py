import tkinter as tk
from tkinter import ttk

from modulo2_home import crear_home
from modulo3_suma import crear_suma
from modulo4_resta import crear_resta
from modulo5_inversa import crear_inversa
from modulo6_multiplica import crear_multiplica
from modulo7_traspuesta import crear_traspuesta
from modulo8_determina import crear_determinante

def abrir_frame(crear_frame):
    global frame_actual
    if frame_actual:
        frame_actual.pack_forget()

    frame_actual = crear_frame(ventana)
    frame_actual.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

def mostrar_resultado(resultado):
    ventana_resultado = tk.Toplevel(ventana)
    ventana_resultado.title("Resultado de la Operación")

    frame_resultado = ttk.Frame(ventana, style="TFrame", width=550, height=550)
    frame_resultado.pack()

    label_resultado = ttk.Label(frame_resultado, text="Resultado de la Operación", font=("Bold", 15))
    label_resultado.grid(row=0, column=0, columnspan=len(resultado[0]) * 2, pady=20)

    for i, fila in enumerate(resultado):
        for j, valor in enumerate(fila):
            label_valor = ttk.Label(frame_resultado, text=str(valor))
            label_valor.grid(row=i + 1, column=j * 2, padx=5)
        ttk.Label(frame_resultado, text="|").grid(row=i + 1, column=len(fila) * 2 - 1)

def mostrar_ventana_ayuda():
    global ventana_ayuda
    if ventana_ayuda is None:
        ventana_ayuda = tk.Toplevel(ventana)
        ventana_ayuda.title("Ayuda")
        ventana_ayuda.protocol("WM_DELETE_WINDOW", ocultar_ventana_ayuda)
        ventana_ayuda.attributes("-topmost", True)
        ventana_ayuda.geometry("+{}+{}".format(ventana.winfo_rootx() + ventana.winfo_width() // 2 - ventana_ayuda.winfo_width() // 2,
                                               ventana.winfo_rooty() + ventana.winfo_height() // 2 - ventana_ayuda.winfo_height() // 2))
        frame_ayuda = ttk.Frame(ventana_ayuda)
        frame_ayuda.pack(padx=20, pady=20)
        label_ayuda = ttk.Label(frame_ayuda, text="Instrucciones de Uso - Calculadora Matricial HJL:\n\n"
        "1. Selección de Operación: - Utiliza los botones de la barra de opciones para seleccionar la \noperación matricial deseada (SUMA, RESTA, INVERSA, MULTIPLICA, TRASPUESTA).\n\n"
        "2. Ingreso de Valores: - Ingresa los valores de las matrices en las secciones correspondientes. \nLos valores deben estar separados por comas.Ejemplo: Para una matriz 2x2, ingresa los valores como 1, 2, 3, 4.\n\n"
        "3. Reglas para los Valores: - Ingresa solo valores numéricos.\n- Utiliza comas para separar los valores.\n-Asegúrate de respetar las reglas aritméticas al ingresar los datos.\n\n"
        "4. Realización de la Operación:- Después de ingresar los valores, haz clic en el botón \ncorrespondiente para realizar la operación seleccionada.\n\n"
        "5. Resultado de la Operación: - El resultado se mostrará en una nueva ventana.\n-Examina cuidadosamente el resultado y verifica que cumple con las expectativas.\n\n")
        label_ayuda.pack(pady=10)
    ventana_ayuda.deiconify()
    ventana_ayuda.lift()

def ocultar_ventana_ayuda():
    global ventana_ayuda
    if ventana_ayuda is not None:
        ventana_ayuda.withdraw()
        ventana_ayuda = None

def abrir_home():
    global frame_actual
    if frame_actual:
        frame_actual.pack_forget()

    frame_actual = crear_home(ventana)
    frame_actual.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

def boton_guardar():
    pass

def guardar_resultado(resultado):
    pass

frame_actual = None

ventana = tk.Tk()
ventana.geometry("700x550")
ventana.title("Calculadora Matricial")
ventana.resizable(0, 0)
ventana_ayuda = None

frame_ayuda = ttk.Frame(ventana)
frame_ayuda.pack(padx=20, pady=20)

frame_opciones = ttk.Frame(ventana, style="TFrame", width=550, height=550)
frame_opciones.pack(side=tk.LEFT)
frame_opciones.pack_propagate(False)
frame_opciones.config(width="150", height="550")

barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

menu_archivo = tk.Menu(barra_menu, tearoff=0)
menu_ayuda = tk.Menu(barra_menu, tearoff=0)
menu_info = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Ayuda", menu=menu_ayuda)
barra_menu.add_cascade(label="Acerca de", menu=menu_info)

# Add "About" button to the menu bar
def mostrar_ventana_about():
    ventana_about = tk.Toplevel(ventana)
    ventana_about.title("About")
    ventana_about.geometry("500x500")
    
    frame_about = ttk.Frame(ventana_about)
    frame_about.pack(expand=True)
    
    label_about = ttk.Label(frame_about, text="Nombre de la Aplicación: Calculadora Matricial HJL\n\nVersión: 4.8\n\nDesarrolladores:\n\n- Lancelot Castro Bobadilla\n\n- Hernan Espinoza Castillo\n\n- Jonathan Medalla Aliste\n\nColaboradores:\n\n- Carolina Gomez Bravo\n\n- Alejandro Cuevas Rivero\n\n- Ernesto Vivanco Tapia\n\n\nFecha de Lanzamiento: 07/12/2023\n\n© 2023 Calculadora Matricial HJL. Todos los derechos reservados.")
    label_about.pack(pady=50)

menu_info.add_command(label="About", command=mostrar_ventana_about)
menu_ayuda.add_command(label="Instrucciones", command=mostrar_ventana_ayuda)

boton_home = ttk.Button(frame_opciones, text="HOME",  command=abrir_home)
boton_home.pack(pady=20)

boton_suma = ttk.Button(frame_opciones, text="SUMA", command=lambda: abrir_frame(crear_suma))
boton_suma.pack(pady=20)

boton_resta = ttk.Button(frame_opciones, text="RESTA",  command=lambda: abrir_frame(crear_resta))
boton_resta.pack(pady=20)

boton_inversa = ttk.Button(frame_opciones, text="INVERSA",  command=lambda: abrir_frame(crear_inversa))
boton_inversa.pack(pady=20)

boton_multiplica = ttk.Button(frame_opciones, text="MULTIPLICA",  command=lambda: abrir_frame(crear_multiplica))
boton_multiplica.pack(pady=20)

boton_traspuesta = ttk.Button(frame_opciones, text="TRASPUESTA",  command=lambda: abrir_frame(crear_traspuesta))
boton_traspuesta.pack(pady=20)

boton_determinante = ttk.Button(frame_opciones, text="DETERMINANTE", command=lambda: abrir_frame(crear_determinante))
boton_determinante.pack(pady=20)

abrir_home()  # Run frame_home by default

ventana.mainloop()
