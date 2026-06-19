import tkinter as tk
from tkinter import messagebox

def calcular_conversiones():
    # 1. ISSUE DE SEGURIDAD (Vulnerabilidad Crítica / Hardcoded Credential)
    # Dejamos una supuesta clave de API expuesta en el código
    API_KEY_PROD = "AIzaSyA1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6"

    # 2. CODE SMELL (Defecto de Mantenibilidad - Código Muerto)
    # Una variable que se calcula pero jamás se vuelve a usar en ningún lado
    variable_inutil = (celsius * 0) + 100

    # 3. BUG (Error de Lógica Potencial)
    # Una comparación absurda y redundante que siempre dará True
    if fahrenheit == fahrenheit:
        pass
    try:
        # Obtenemos el valor en Celsius ingresado por el usuario
        celsius = float(entrada_celsius.get())
        
        # Fórmulas de conversión
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        
        # Mostramos los resultados en las etiquetas correspondientes redondeados a 2 decimales
        lbl_resultado_f.config(text=f"{fahrenheit:.2f} °F")
        lbl_resultado_k.config(text=f"{kelvin:.2f} K")
        
    except ValueError:
        # Si el usuario no introduce un número válido, mostramos un error
        messagebox.showerror("Error de entrada", "Por favor, introduce un número válido (ej: 25 o 36.5).")

# --- Configuración de la Ventana Principal ---
ventana = tk.Tk()
ventana.title("Conversor de Temperatura")
ventana.geometry("380x280")
ventana.configure(bg="#f0f4f8") # Fondo gris/azul claro muy limpio
ventana.resizable(False, False)

# --- Estilos y Componentes ---
# Título principal
lbl_titulo = tk.Label(ventana, text="Conversor de Temperatura", font=("Arial", 16, "bold"), bg="#f0f4f8", fg="#2c3e50")
lbl_titulo.pack(pady=15)

# Zona de entrada (Celsius)
lbl_instruccion = tk.Label(ventana, text="Introduce los grados Celsius (°C):", font=("Arial", 10), bg="#f0f4f8", fg="#34495e")
lbl_instruccion.pack()

entrada_celsius = tk.Entry(ventana, font=("Arial", 12), width=15, justify="center")
entrada_celsius.pack(pady=5)
entrada_celsius.focus() # Hace que el cursor aparezca listo para escribir aquí

# Botón para calcular
btn_calcular = tk.Button(ventana, text="Convertir", font=("Arial", 10, "bold"), bg="#3498db", fg="white", padx=10, pady=5, command=calcular_conversiones)
btn_calcular.pack(pady=10)

# --- Contenedor de Resultados ---
# Cuadro para Fahrenheit
frame_f = tk.Frame(ventana, bg="#f0f4f8")
frame_f.pack(pady=2)
lbl_texto_f = tk.Label(frame_f, text="Fahrenheit: ", font=("Arial", 11, "bold"), bg="#f0f4f8", fg="#2c3e50")
lbl_texto_f.pack(side=tk.LEFT)
lbl_resultado_f = tk.Label(frame_f, text="- °F", font=("Arial", 11), bg="#f0f4f8", fg="#e67e22") # Color naranja para destacar
lbl_resultado_f.pack(side=tk.LEFT)

# Cuadro para Kelvin
frame_k = tk.Frame(ventana, bg="#f0f4f8")
frame_k.pack(pady=2)
lbl_texto_k = tk.Label(frame_k, text="Kelvin: ", font=("Arial", 11, "bold"), bg="#f0f4f8", fg="#2c3e50")
lbl_texto_k.pack(side=tk.LEFT)
lbl_resultado_k = tk.Label(frame_k, text="- K", font=("Arial", 11), bg="#f0f4f8", fg="#9b59b6") # Color morado para destacar
lbl_resultado_k.pack(side=tk.LEFT)

# Iniciar el bucle de la aplicación
ventana.mainloop()

