import pyfiglet
from colorama import Fore, Style

# Definir colores (Rojo,Rojo Oscuro,Amarillo,Amarillo Claro)
COLORS = [Fore.RED, Fore.YELLOW, Fore.LIGHTYELLOW_EX]

# Generar texto con pyfiglet
texto = "SweetShop"
figlet_text = pyfiglet.figlet_format(texto)

# Aplicar colores intercalados
colored_text = ""
color_index = 0

for char in figlet_text:
    if char != " ":  # Para evitar colorear entre espacios
        colored_text += COLORS[color_index % len(COLORS)] + char
        color_index += 1
    else:
        colored_text += char  # Mantener los espacios aun si se ignoran

# Mostrar el texto con colores
print(colored_text + Style.RESET_ALL)
