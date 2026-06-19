import pytest

# Funciones puras de conversión (aisladas de la interfaz gráfica)
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_a_kelvin(celsius):
    return celsius + 273.15

# --- PRUEBAS UNITARIAS ---

def test_conversiones_punto_congelacion():
    # Testeamos el punto de congelación del agua (0 °C)
    assert celsius_a_fahrenheit(0) == 32.0
    assert celsius_a_kelvin(0) == 273.15

def test_conversiones_valores_negativos():
    # Testeamos que soporte temperaturas bajo cero
    assert celsius_a_fahrenheit(-40) == -40.0
    assert celsius_a_kelvin(-100) == 173.15