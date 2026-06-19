# language: es
Característica: Conversión de escalas de temperatura

  Escenario: Conversión exitosa de Celsius a Fahrenheit y Kelvin
    Dado que el usuario ingresa "100" en el campo de grados Celsius
    Cuando el usuario presiona el botón de calcular conversión
    Entonces el sistema debe mostrar "212.00 °F" en el resultado de Fahrenheit
    Y el sistema debe mostrar "373.15 K" en el resultado de Kelvin