import pyfiglet

# Generar el texto con pyfiglet
texto = "SweetShop"
figlet_text = pyfiglet.figlet_format(texto)

# Reemplazar espacios en blanco con un carácter de relleno
relleno = "#"  # Puedes cambiarlo a cualquier otro signo
texto_relleno = figlet_text.replace(" ", relleno)

print(texto_relleno)
