from behave import given, when, then

@given('que el usuario ingresa "{valor}" en el campo de grados Celsius')
def step_impl(context, valor):
    context.celsius = float(valor)

@when('el usuario presiona el botón de calcular conversión')
def step_impl(context):
    context.fahrenheit = (context.celsius * 9/5) + 32
    context.kelvin = context.celsius + 273.15

@then('el sistema debe mostrar "{resultado_f}" en el resultado de Fahrenheit')
def step_impl(context, resultado_f):
    assert f"{context.fahrenheit:.2f} °F" == resultado_f

@then('el sistema debe mostrar "{resultado_k}" en el resultado de Kelvin')
def step_impl(context, resultado_k):
    assert f"{context.kelvin:.2f} K" == resultado_k