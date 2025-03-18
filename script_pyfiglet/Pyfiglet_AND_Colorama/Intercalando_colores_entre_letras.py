import pyfiglet
from colorama import Fore, Style

# Definir colores 
COLORS = [Fore.LIGHTRED_EX, Fore.YELLOW, Fore.RED]  # Naranja, Amarillo, Marrón (Rojo oscuro porque no hay marro :c )

# Texto base
texto = "Hola Mundo"

# Convertir cada letra en ASCII con pyfiglet
figlet_letters = [pyfiglet.figlet_format(char) for char in texto]

# Separar en líneas individuales (para mantener la estructura)
figlet_lines = [letter.split("\n") for letter in figlet_letters]

# Encontrar la cantidad de líneas en cada letra ASCII
max_lines = max(len(lines) for lines in figlet_lines)

# Unir cada letra por línea con su color correspondiente
colored_output = ""
for i in range(max_lines):
    for index, lines in enumerate(figlet_lines):
        color = COLORS[index % len(COLORS)]  # Aplicar color a cada letra
        if i < len(lines):  # Verificar si la línea existe en la letra
            colored_output += color + lines[i] + "  "  # Espacio entre letras
    colored_output += "\n"

# Imprimir resultado con colores
print(colored_output + Style.RESET_ALL)
