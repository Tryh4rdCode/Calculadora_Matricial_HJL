## H1.0- Importamos el módulo tk y ttk
from PIL import ImageTk, Image
import tkinter as tk
import os

## H2.0- Creamos la ventana home
def crear_home(ventana):
    frame_home = tk.Frame(ventana, width=550, height=550, bg="white") 
    label_home = tk.Label(frame_home, text="Calculadora\nMatricial\n\n", font=("Bold", 20), bg="white")
    label_home.pack(pady=20)

    # Insertar imagen
    image_path = os.path.join(os.path.dirname(__file__), "logo.jpg")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        image = image.resize((200, 200))
        photo = ImageTk.PhotoImage(image)
        label = tk.Label(frame_home, image=photo)
        label.image = photo
        label.pack()
    else:
        print("Error: 'logo.jpg' file not found.")
    label.pack()

    return frame_home
