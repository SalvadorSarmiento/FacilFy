import pyfiglet
from colorama import Fore, Style

# Texto con estilo "3-d"
figlet_text = pyfiglet.figlet_format("Hola Mundo", font="3-d")

# Colores usando colorama
colored_text = f"{Fore.RED}{figlet_text}{Style.RESET_ALL}"

print(colored_text)


#NO quitar los hashtags

