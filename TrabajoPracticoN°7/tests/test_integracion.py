import pytest
import tkinter as tk

# Traemos la lógica del circuito de conversión
def procesar_circuito_conversion(entrada_widget, lbl_f, lbl_k):
    try:
        celsius = float(entrada_widget.get())
        fahrenheit = (celsius * 9/5) + 32
        kelvin = celsius + 273.15
        
        lbl_f.config(text=f"{fahrenheit:.2f} °F")
        lbl_k.config(text=f"{kelvin:.2f} K")
    except ValueError:
        lbl_f.config(text="Error")
        lbl_k.config(text="Error")

# --- PRUEBA DE INTEGRACIÓN ---

def test_circuito_completo_conversion():
    # 1. Creamos el entorno de componentes de la interfaz en memoria
    ventana_test = tk.Tk()
    entrada = tk.Entry(ventana_test)
    lbl_f = tk.Label(ventana_test, text="- °F")
    lbl_k = tk.Label(ventana_test, text="- K")
    
    # 2. Simulamos la acción del usuario: Ingresa 25 °C en el campo de texto
    entrada.insert(0, "25")
    
    # 3. Se ejecuta el circuito operativo completo
    procesar_circuito_conversion(entrada, lbl_f, lbl_k)
    
    # 4. Verificamos la integración: ¿Los labels cambiaron al valor correcto esperado?
    assert lbl_f.cget("text") == "77.00 °F"
    assert lbl_k.cget("text") == "298.15 K"
    
    # Limpieza de la ventana de prueba
    ventana_test.destroy()