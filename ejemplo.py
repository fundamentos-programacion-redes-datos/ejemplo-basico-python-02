"""
Generar un solución que permita calcular y mostrar el valor de la planilla de teléfono 
de un casa. Se debe ingresar el costo por minutos, el número de minutos consumidos en el mes, 
la dirección del domicilio, el nombre completo del dueño de la línea telefónica. 
Finalmente presentar el siguiente reporte

Reporte:
Nombres completos: Luis Alberto Carvajal Ludeña
Dirección: Calle primera entre segunda y décima
Costo por minuto: $1.5
Número de minutos consumidos: 50
Valor a cancelar: $75

"""
# Inicio

# Declaración de variables en Python (no se especifica el tipo de dato explícitamente)
# Se capturan los valores mediante entrada de usuario
nombre_completo = input("Ingrese los nombres completos del dueño de la línea telefónica: ")  
direccion = input("Ingrese la dirección del domicilio: ")  

# Captura de valores numéricos
costo_por_minuto = input("Ingrese el costo por minuto: ")  
costo_por_minuto = float(costo_por_minuto)  # Conversión a decimal (float) para permitir valores con decimales

minutos_consumidos = input("Ingrese el número de minutos consumidos en el mes: ")  
minutos_consumidos = int(minutos_consumidos)  # Conversión a entero (int), ya que son minutos enteros

# Cálculo del valor a cancelar
valor_cancelar = costo_por_minuto * minutos_consumidos  # Se multiplica el costo por los minutos consumidos

# Mostrar el reporte de la planilla

#  Se utiliza una variable de tipo cadena (`cadena_final`) para acumular toda la información del reporte.
#  Esto permite organizar los datos en una única estructura antes de imprimirlos.
#  Se usa `f-strings` para formatear los valores dentro de la cadena de texto.

#  Se usan **tres comillas triples (`"""` o `'''`)** para definir la cadena de texto multilínea de manera legible.
#  Esto evita la necesidad de usar múltiples `\n` o concatenaciones con `+`.
#  Las cadenas entre comillas triples pueden mantener el formato original con espacios y saltos de línea.

cadena_final = f"""
Reporte:
Nombres completos: {nombre_completo}
Dirección: {direccion}
Costo por minuto: ${costo_por_minuto:.2f}
Número de minutos consumidos: {minutos_consumidos}
Valor a cancelar: ${valor_cancelar:.2f}
"""

# Finalmente, se imprime el contenido de `cadena_final`
print(cadena_final)

# Fin
