from libreriaDeNotificaciones import Notificador

# Asocia un número y un nombre que son de tipo de notificador
number_notificador_name_association = {
    1: "Correo",
    2: "Facebook",
    3: "SMS",
    4: "Empresarial",
}

# Muestra los tipos de notificador en una lista para decirle al usuario cual escoger 
print("""
1. Correo
2. Facebook
3. SMS
4. Empresarial""")

notificadors_type_raw = input("Elija los tipos de notificación.\nEscriba todos los números seleccionados sin ninguna separación:\n")
notificadores_data = {}
# Recorre todos los notificadores seleccionados, pide sus destinatarios y los agrega al notificador
for n in notificadors_type_raw:
    destinatarios = input("Elija los destinatarios para {} separados por un espacio: ".format(number_notificador_name_association.get(int(n))))
    destinatarios = destinatarios.split(' ') # Convierte los destinatarios a una lista
    notificadores_data.update({int(n) - 1: destinatarios})

notificador = Notificador(notificadores_data)
mensaje_raw = input("Esciba el mensaje a enviar: ")

# Envía el mensaje
notificador.send(mensaje_raw)

