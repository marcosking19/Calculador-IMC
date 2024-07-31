import tkinter as tk
from tkinter import messagebox
import csv
from tkinter import PhotoImage

def calcular_imc():
    try:
        nombre = entry_nombre.get()
        peso = float(entry_peso.get())
        altura = float(entry_altura.get()) / 100  # Convertir altura a metros
        edad = int(entry_edad.get())
        sexo = var_sexo.get()
        
        if sexo == "Hombre":
            ks = 1.0
        elif sexo == "Mujer":
            ks = 1.1
        else:
            raise ValueError("Sexo no válido")
        ka = 1 + 0.01 * (edad - 25)
        imc = (peso / (altura ** 2)) * ks * ka
        mostrar_resultado(imc)
    except ValueError as e:
        messagebox.showerror("Error de entrada", str(e))

def mostrar_resultado(imc):
    resultado_ventana = tk.Toplevel(root)
    resultado_ventana.title("Resultado del IMC")

    # Mostrar el resultado del IMC
    tk.Label(resultado_ventana, text=f"IMC: {imc:.2f}", font=('Arial', 14)).pack(pady=10)

    # Tabla de categorías de IMC
    categorias = [
        ("Categoría", "IMC"),
        ("Bajo peso", "Menos de 18.5"),
        ("Normal", "18.5–24.9"),
        ("Sobrepeso", "25–29.9"),
        ("Obesidad", "30 o más")
    ]
    
    for categoria, valor in categorias:
        frame_categoria = tk.Frame(resultado_ventana)
        frame_categoria.pack(pady=2)
        tk.Label(frame_categoria, text=categoria, borderwidth=2, relief='solid').pack(side="left", padx=5)
        tk.Label(frame_categoria, text=valor, borderwidth=2, relief='solid').pack(side="left", padx=5)
    
    # Indicar si el IMC es alto, bajo o normal
    if imc < 18.5:
        mensaje = "Bajo peso"
    elif 18.5 <= imc < 25:
        mensaje = "Peso normal"
    elif 25 <= imc < 30:
        mensaje = "Sobrepeso"
    else:
        mensaje = "Obesidad"
    
    tk.Label(resultado_ventana, text=f"Categoría: {mensaje}", font=('Arial', 12, 'bold')).pack(pady=10)

def guardar_datos():
    nombre = entry_nombre.get()
    if not nombre:
        messagebox.showerror("Error de entrada", "El nombre del paciente no puede estar vacío.")
        return
    try:
        peso = float(entry_peso.get())
        altura = float(entry_altura.get()) / 100  # Convertir altura a metros
        edad = int(entry_edad.get())
        sexo = var_sexo.get()
        
        if sexo == "Hombre":
            ks = 1.0
        elif sexo == "Mujer":
            ks = 1.1
        else:
            raise ValueError("Sexo no válido")
        ka = 1 + 0.01 * (edad - 25)
        imc = (peso / (altura ** 2)) * ks * ka
        with open(f"{nombre}.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Nombre", "Peso", "Altura", "Edad", "Sexo", "IMC"])
            writer.writerow([nombre, peso, altura, edad, sexo, imc])
        messagebox.showinfo("Datos guardados", f"Los datos han sido guardados en {nombre}.csv")
        
    except ValueError as e:
        messagebox.showerror("Error de entrada", str(e))

# Crear la ventana principal
root = tk.Tk()
root.title("Calculadora de IMC")
root.geometry("400x300")  # Establecer el tamaño de la ventana principal

# Crear un Canvas para la ventana principal
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)

# Cargar la imagen de fondo y colocarla en el Canvas
bg_image = PhotoImage(file="C:\\Users\\marco\\Desktop\\examen\\BOTONES\\fondo.png")
canvas.create_image(0, 0, anchor="nw", image=bg_image)

# Crear y colocar los widgets sobre el Canvas
canvas.create_text(100, 50, text="Nombre:", anchor="w", font=("Helvetica", 10, "bold"))
entry_nombre = tk.Entry(root, bg="#D3D3D3")
canvas.create_window(200, 50, window=entry_nombre, anchor="w")
#state

canvas.create_text(100, 90, text="Peso (kg):", anchor="w", font=("Helvetica", 10, "bold"))
entry_peso = tk.Entry(root, width=10, bg="#D3D3D3")
canvas.create_window(200, 90, window=entry_peso, anchor="w")

canvas.create_text(100, 130, text="Altura (cm):", anchor="w", font=("Helvetica", 10, "bold"))
entry_altura = tk.Entry(root, width=10, bg="#D3D3D3")
canvas.create_window(200, 130, window=entry_altura, anchor="w")

canvas.create_text(100, 170, text="Edad (años):", anchor="w", font=("Helvetica", 10, "bold"))
entry_edad = tk.Entry(root, width=10, bg="#D3D3D3")
canvas.create_window(200, 170, window=entry_edad, anchor="w")

# Establecer el color de fondo de tu aplicación
bg_color = "#f0f0f0"  # Puedes ajustar este color según el color de fondo de tu aplicación

# Crear y colocar los widgets sobre el Canvas sin fondo
canvas.create_text(100, 210, text="Sexo biológico:", anchor="w", fill="black", font=("Helvetica", 10, "bold"))  
var_sexo = tk.StringVar(value="Hombre")
radio_hombre = tk.Radiobutton(root, text="Hombre", variable=var_sexo, value="Hombre", bg="white", borderwidth=0, font=("Helvetica", 10, "bold"))
canvas.create_window(200, 210, window=radio_hombre, anchor="w")
radio_mujer = tk.Radiobutton(root, text="Mujer", variable=var_sexo, value="Mujer", bg="white", borderwidth=0, font=("Helvetica", 10, "bold"))
canvas.create_window(300, 210, window=radio_mujer, anchor="w")


# Cargar las imágenes y ajustar el tamaño
imagen_calcular = PhotoImage(file="C:\\Users\\marco\\Desktop\\examen\\BOTONES\\BOTONTIPOIMS.png").subsample(10, 10)  # Ajusta el factor de subsample para reducir el tamaño
button_calcular = tk.Button(root, image=imagen_calcular, command=calcular_imc, bg="white", borderwidth=0, cursor="hand2")
canvas.create_window(130, 250, window=button_calcular, anchor="w")  # Cambié la coordenada x de 150 a 130

imagen_guardar = PhotoImage(file="C:\\Users\\marco\\Desktop\\examen\\BOTONES\\BOTONGUARDAR.png").subsample(10, 10)  # Ajusta el factor de subsample para reducir el tamaño
button_guardar = tk.Button(root, image=imagen_guardar, command=guardar_datos, bg="white", borderwidth=0, cursor="hand2")
canvas.create_window(270, 250, window=button_guardar, anchor="w")  # Cambié la coordenada x de 250 a 270

# Necesitamos mantener una referencia de la imagen para que no sea recolectada por el garbage collector
root.bg_image = bg_image

# Iniciar el bucle principal
root.mainloop()
